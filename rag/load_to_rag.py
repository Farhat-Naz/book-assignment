"""
Load documents into the RAG service via API endpoints
This script loads documents from the website/docs directory and stores them in the RAG system
"""
import asyncio
import os
import sys
import httpx

# Add the rag/src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from services.document_loader import UniversalDocLoader
from services.text_chunker import async_chunk_documents
from services.embedding_service import EmbeddingService
from core.qdrant_client import qdrant_store


async def load_documents_to_rag():
    """
    Load documents and store them in Qdrant via the RAG service
    """
    print("="*60)
    print("Loading Documents into RAG Service")
    print("="*60)

    # Initialize services
    loader = UniversalDocLoader()
    embed_service = EmbeddingService()

    # Path to the book documents (Docusaurus docs)
    docs_path = os.path.join(os.path.dirname(__file__), '..', 'website', 'docs')

    if not os.path.exists(docs_path):
        print(f"[ERROR] Documents path not found: {docs_path}")
        return

    print(f"\nLoading documents from: {docs_path}")

    try:
        # Step 1: Load documents
        print("\n[Step 1/4] Loading documents...")
        documents = await loader.load_from_path(docs_path)

        print(f"[OK] Loaded {len(documents)} documents")

        if not documents:
            print("[ERROR] No documents found to process!")
            return

        # Step 2: Chunk documents
        print("\n[Step 2/4] Chunking documents...")
        chunks = await async_chunk_documents(documents, chunk_size=512, overlap=50)
        print(f"[OK] Created {len(chunks)} text chunks")

        # Step 3: Generate embeddings
        print("\n[Step 3/4] Generating embeddings...")
        points = await embed_service.embed_chunks(chunks)
        print(f"[OK] Generated {len(points)} embeddings")

        # Step 4: Store in Qdrant
        print("\n[Step 4/4] Storing in Qdrant...")

        # Create collection if it doesn't exist
        try:
            qdrant_store.create_collection()
            print("[OK] Qdrant collection ready")
        except Exception as e:
            print(f"[WARN] Collection creation: {str(e)}")

        # Insert points
        try:
            qdrant_store.insert_points(points)
            print(f"[OK] Inserted {len(points)} vectors into Qdrant")
        except Exception as e:
            print(f"[ERROR] Error inserting points: {str(e)}")
            return

        # Get collection info
        try:
            info = qdrant_store.get_collection_info()
            print(f"\nCollection Statistics:")
            print(f"   Name: {info.get('name', 'N/A')}")
            print(f"   Points: {info.get('points_count', 0)}")
            print(f"   Vectors: {info.get('vectors_count', 0)}")
            print(f"   Status: {info.get('status', 'N/A')}")
        except Exception as e:
            print(f"[WARN] Could not retrieve collection info: {str(e)}")

        print("\n[SUCCESS] Document loading complete!")
        print(f"   Total documents: {len(documents)}")
        print(f"   Total chunks: {len(chunks)}")
        print(f"   Total embeddings: {len(points)}")

    except Exception as e:
        print(f"\n[ERROR] Error processing documents: {str(e)}")
        import traceback
        traceback.print_exc()


async def test_search():
    """
    Test the search functionality
    """
    print("\n" + "="*60)
    print("Testing Search Functionality")
    print("="*60)

    from services.embedding_service import EmbeddingService

    embed_service = EmbeddingService()

    # Test queries
    queries = [
        "What is Physical AI?",
        "Tell me about sensors in robotics",
        "What is ROS2?",
    ]

    for query in queries:
        print(f"\n[QUERY] {query}")

        try:
            # Generate embedding for query
            query_embedding = await embed_service.embed_query(query)

            # Search Qdrant
            results = qdrant_store.search(
                query_vector=query_embedding,
                top_k=3,
                score_threshold=0.5
            )

            if results:
                print(f"   Found {len(results)} results:")
                for i, result in enumerate(results[:3], 1):
                    score = result['score']
                    source = result['payload'].get('metadata', {}).get('source', 'Unknown')
                    content = result['payload'].get('content', '')[:100]
                    print(f"   {i}. Score: {score:.3f}")
                    print(f"      Source: {os.path.basename(source)}")
                    print(f"      Preview: {content}...")
            else:
                print("   No results found")

        except Exception as e:
            print(f"   [ERROR] Search error: {str(e)}")


if __name__ == "__main__":
    print("\nRAG Document Loader\n")
    asyncio.run(load_documents_to_rag())
    asyncio.run(test_search())
    print("\nDone!\n")
