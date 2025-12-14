"""
Script to load book documents into the RAG system and create embeddings
"""
import asyncio
import os
import sys
from pathlib import Path

# Add the rag/src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'rag', 'src'))

from services.document_loader import UniversalDocLoader
from services.text_chunker import async_chunk_documents
from services.embedding_service import EmbeddingService
from core.qdrant_client import qdrant_store

async def load_book_documents():
    """
    Load, chunk, and embed the book documents into Qdrant
    """
    print("Starting document processing pipeline...")
    
    # Initialize services
    loader = UniversalDocLoader()
    embed_service = EmbeddingService()
    
    # Path to the book documents (Docusaurus docs)
    docs_path = os.path.join(os.path.dirname(__file__), '..', 'website', 'docs')
    
    if not os.path.exists(docs_path):
        print(f"Documents path not found: {docs_path}")
        return
    
    print(f"Loading documents from: {docs_path}")
    
    try:
        # 1. Load documents
        print("Step 1: Loading documents...")
        documents = await loader.load_from_path(docs_path)
        
        print(f"Loaded {len(documents)} documents:")
        for i, doc in enumerate(documents):
            print(f"  {i+1}. {doc['metadata']['source']} ({len(doc['content'])} chars)")
        
        if not documents:
            print("No documents found to process!")
            return
        
        # 2. Chunk documents
        print("\nStep 2: Chunking documents...")
        chunks = await async_chunk_documents(documents, chunk_size=512, overlap=50)
        
        print(f"Created {len(chunks)} text chunks")
        
        # 3. Generate embeddings and store in Qdrant
        print("\nStep 3: Generating embeddings and storing in Qdrant...")
        points = await embed_service.embed_chunks(chunks)
        
        # Add metadata to distinguish book content
        for point in points:
            # Add a content_type field to identify book content
            point.payload["content_type"] = "course_book"
            # Extract chapter/module info from source path
            source = point.payload["metadata"]["source"]
            if "module-1" in source:
                point.payload["metadata"]["module"] = "module-1"
            elif "module-2" in source:
                point.payload["metadata"]["module"] = "module-2"
            # Add chapter info
            import re
            chapter_match = re.search(r'chapter-\d+', source)
            if chapter_match:
                point.payload["metadata"]["chapter"] = chapter_match.group(0)
        
        # Insert points into Qdrant
        qdrant_store.insert_points(points)
        
        print(f"Successfully stored {len(points)} embeddings in Qdrant collection '{qdrant_store.collection_name}'")
        
        # Show collection info
        info = qdrant_store.get_collection_info()
        print(f"\nCollection info: {info}")
        
    except Exception as e:
        print(f"Error processing documents: {str(e)}")
        import traceback
        traceback.print_exc()


async def query_example():
    """
    Example of how to query the RAG system
    """
    print("\n" + "="*50)
    print("Example Query Test")
    print("="*50)
    
    from services.embedding_service import EmbeddingService
    from core.qdrant_client import qdrant_store
    from core.config import settings
    
    embed_service = EmbeddingService()
    
    # Example query
    query = "What is the introduction to Physical AI and Humanoid Robotics?"
    
    print(f"Query: {query}")
    
    try:
        # Generate embedding for query
        query_embedding = await embed_service.embed_query(query)
        
        # Search Qdrant
        search_results = qdrant_store.search(
            query_vector=query_embedding,
            top_k=3,
            score_threshold=0.5
        )
        
        print(f"\nFound {len(search_results)} relevant results:")
        for i, result in enumerate(search_results):
            print(f"\n{i+1}. Score: {result['score']:.3f}")
            print(f"   Source: {result['payload']['metadata']['source']}")
            content_preview = result['payload']['content'][:200] + "..." if len(result['payload']['content']) > 200 else result['payload']['content']
            print(f"   Content: {content_preview}")
        
    except Exception as e:
        print(f"Error querying: {str(e)}")


if __name__ == "__main__":
    asyncio.run(load_book_documents())
    asyncio.run(query_example())