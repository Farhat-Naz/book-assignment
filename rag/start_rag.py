"""
Startup script for RAG service that loads documents and starts the server
"""
import asyncio
import subprocess
import os
import sys

# Add the rag/src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from services.document_loader import UniversalDocLoader
from services.text_chunker import async_chunk_documents
from services.embedding_service import EmbeddingService
from core.qdrant_client import qdrant_store


async def initialize_rag_system():
    """
    Initialize the RAG system by loading documents into Qdrant
    """
    print("\n" + "="*60)
    print("RAG Service Initialization")
    print("="*60)

    # Initialize services
    loader = UniversalDocLoader()
    embed_service = EmbeddingService()

    # Path to the book documents
    docs_path = os.path.join(os.path.dirname(__file__), '..', 'website', 'docs')

    if not os.path.exists(docs_path):
        print(f"\n[WARN] Documents path not found: {docs_path}")
        print("[INFO] Starting server without pre-loaded documents")
        return False

    print(f"\n[INFO] Loading documents from: {docs_path}")

    try:
        # Load documents
        print("[1/4] Loading documents...")
        documents = await loader.load_from_path(docs_path)
        print(f"      Loaded {len(documents)} documents")

        if not documents:
            print("[WARN] No documents found")
            return False

        # Chunk documents
        print("[2/4] Chunking documents...")
        chunks = await async_chunk_documents(documents, chunk_size=512, overlap=50)
        print(f"      Created {len(chunks)} chunks")

        # Generate embeddings
        print("[3/4] Generating embeddings...")
        points = await embed_service.embed_chunks(chunks)
        print(f"      Generated {len(points)} embeddings")

        # Store in Qdrant
        print("[4/4] Storing in vector database...")
        try:
            qdrant_store.create_collection()
            qdrant_store.insert_points(points)
            print(f"      Stored {len(points)} vectors")
        except Exception as e:
            print(f"[ERROR] Failed to store vectors: {str(e)}")
            return False

        # Get stats
        try:
            info = qdrant_store.get_collection_info()
            print(f"\n[SUCCESS] RAG system initialized!")
            print(f"          Collection: {info.get('name', 'N/A')}")
            print(f"          Vectors: {info.get('vectors_count', 0)}")
            print(f"          Status: {info.get('status', 'N/A')}")
        except Exception as e:
            print(f"[WARN] Could not retrieve stats: {str(e)}")

        return True

    except Exception as e:
        print(f"\n[ERROR] Initialization failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def start_server():
    """Start the uvicorn server"""
    print("\n" + "="*60)
    print("Starting FastAPI Server")
    print("="*60)
    print("\n[INFO] Server will be available at: http://localhost:8000")
    print("[INFO] API Documentation: http://localhost:8000/docs")
    print("[INFO] WebSocket Chat: ws://localhost:8000/ws/chat")
    print("\n[INFO] Press CTRL+C to stop the server\n")

    os.system("uvicorn src.main:app --host 0.0.0.0 --port 8000")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Physical AI RAG Service")
    print("="*60)

    # Initialize RAG system
    success = asyncio.run(initialize_rag_system())

    if success:
        print("\n[INFO] Starting server with pre-loaded documents...")
    else:
        print("\n[INFO] Starting server (documents can be loaded via API)...")

    # Small delay to show the status
    import time
    time.sleep(2)

    # Start the server
    start_server()
