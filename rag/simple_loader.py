
"""
Simplified document loader that works without Qdrant for testing
"""
import asyncio
import os
import sys
from pathlib import Path

# Add the rag/src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from services.document_loader import UniversalDocLoader
from services.text_chunker import async_chunk_documents
from services.embedding_service import EmbeddingService

# Global variable to store embeddings in memory
EMBEDDING_STORE = []

async def load_book_documents():
    """
    Load, chunk, and embed the book documents
    """
    print("Starting document processing pipeline (without Qdrant)...")
    
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
        
        # 3. Generate embeddings and store in memory
        print("\nStep 3: Generating embeddings and storing in memory...")
        global EMBEDDING_STORE
        for i, chunk in enumerate(chunks):
            # Generate embedding for the chunk
            embedding = await embed_service.embed_text(chunk.content)
            
            # Store the chunk with its embedding
            EMBEDDING_STORE.append({
                'id': chunk.id,
                'embedding': embedding,
                'content': chunk.content,
                'metadata': chunk.metadata
            })
            
            if (i + 1) % 5 == 0:  # Progress indicator
                print(f"  Processed {i + 1}/{len(chunks)} chunks")
        
        print(f"\nSuccessfully stored {len(EMBEDDING_STORE)} embeddings in memory")
        
        # Show a sample
        if EMBEDDING_STORE:
            print(f"Sample embedding dimension: {len(EMBEDDING_STORE[0]['embedding'])}")
            print(f"First chunk preview: {EMBEDDING_STORE[0]['content'][:100]}...")
        
    except Exception as e:
        print(f"Error processing documents: {str(e)}")
        import traceback
        traceback.print_exc()


def find_similar_chunks(query_embedding, top_k=3, threshold=0.5):
    """
    Find similar chunks using cosine similarity
    """
    if not EMBEDDING_STORE:
        return []
    
    def cosine_similarity(v1, v2):
        dot_product = sum(a * b for a, b in zip(v1, v2))
        magnitude1 = sum(a * a for a in v1) ** 0.5
        magnitude2 = sum(b * b for b in v2) ** 0.5
        if magnitude1 == 0 or magnitude2 == 0:
            return 0
        return dot_product / (magnitude1 * magnitude2)
    
    # Calculate similarities
    similarities = []
    for item in EMBEDDING_STORE:
        similarity = cosine_similarity(query_embedding, item['embedding'])
        if similarity >= threshold:
            similarities.append((similarity, item))
    
    # Sort by similarity and return top_k
    similarities.sort(key=lambda x: x[0], reverse=True)
    return similarities[:top_k]


async def query_example():
    """
    Example of how to query the embedding store
    """
    print("\n" + "="*50)
    print("Example Query Test")
    print("="*50)
    
    if not EMBEDDING_STORE:
        print("No embeddings loaded. Please run document loading first.")
        return
    
    from services.embedding_service import EmbeddingService
    
    embed_service = EmbeddingService()
    
    # Example query
    query = "What is the introduction to Physical AI and Humanoid Robotics?"
    
    print(f"Query: {query}")
    
    try:
        # Generate embedding for query
        query_embedding = await embed_service.embed_query(query)
        
        # Find similar chunks
        similar_chunks = find_similar_chunks(query_embedding, top_k=3)
        
        print(f"\nFound {len(similar_chunks)} relevant results:")
        for i, (score, chunk) in enumerate(similar_chunks):
            print(f"\n{i+1}. Score: {score:.3f}")
            print(f"   Source: {chunk['metadata']['source']}")
            content_preview = chunk['content'][:200] + "..." if len(chunk['content']) > 200 else chunk['content']
            # Handle encoding errors for console output
            content_safe = content_preview.encode('ascii', errors='replace').decode('ascii')
            print(f"   Content: {content_safe}")
        
    except Exception as e:
        print(f"Error querying: {str(e)}")


if __name__ == "__main__":
    asyncio.run(load_book_documents())
    asyncio.run(query_example())