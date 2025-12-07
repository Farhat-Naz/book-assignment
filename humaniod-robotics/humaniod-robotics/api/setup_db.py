"""Setup script to initialize databases."""
import sys
from .database import postgres_db, vector_db
from .config import settings


def setup_postgres():
    """Initialize Postgres database with required tables."""
    print("[*] Setting up Neon Postgres database...")

    try:
        postgres_db.create_tables()
        print("[OK] Postgres tables created successfully!")
        return True
    except Exception as e:
        print(f"[ERROR] Error creating Postgres tables: {e}")
        return False


def setup_qdrant():
    """Initialize Qdrant collection."""
    print("[*] Setting up Qdrant Cloud collection...")

    try:
        # Get embedding size from settings
        # text-embedding-3-small produces 1536-dimensional vectors
        vector_size = 1536 if settings.EMBEDDING_MODEL == "text-embedding-3-small" else 1536

        vector_db.create_collection(vector_size=vector_size)
        print(f"[OK] Qdrant collection '{settings.QDRANT_COLLECTION}' created successfully!")
        return True
    except Exception as e:
        print(f"[ERROR] Error creating Qdrant collection: {e}")
        return False


def verify_connections():
    """Verify all database connections."""
    print("\n[*] Verifying connections...")

    all_good = True

    # Check Postgres (optional)
    if postgres_db.enabled:
        try:
            conn = postgres_db.connect()
            if conn:
                print("[OK] Neon Postgres connection successful")
                conn.close()
        except Exception as e:
            print(f"[WARN] Neon Postgres connection failed: {e}")
            print("[INFO] Chat history will not be saved (Postgres is optional)")
    else:
        print("[INFO] Neon Postgres not configured (optional - for chat history)")

    # Check Qdrant (required)
    try:
        collections = vector_db.client.get_collections()
        print(f"[OK] Qdrant Cloud connection successful")
    except Exception as e:
        print(f"[ERROR] Qdrant Cloud connection failed: {e}")
        all_good = False

    return all_good


def main():
    """Main setup function."""
    print("=" * 60)
    print("RAG Chatbot Database Setup")
    print("=" * 60)
    print()

    # Verify environment variables
    print("[CONFIG] Configuration:")
    print(f"  - OpenAI Model: {settings.OPENAI_MODEL}")
    print(f"  - Embedding Model: {settings.EMBEDDING_MODEL}")
    print(f"  - Qdrant Collection: {settings.QDRANT_COLLECTION}")
    print(f"  - Chunk Size: {settings.CHUNK_SIZE}")
    print(f"  - Top K Results: {settings.TOP_K_RESULTS}")
    print()

    # Verify connections first
    if not verify_connections():
        print("\n[ERROR] Connection verification failed. Please check your environment variables.")
        sys.exit(1)

    print()

    # Setup Postgres (optional)
    if postgres_db.enabled:
        if not setup_postgres():
            print("[WARN] Postgres setup failed, but continuing (it's optional)")
    else:
        print("[INFO] Skipping Postgres setup (not configured)")

    print()

    # Setup Qdrant (required)
    if not setup_qdrant():
        sys.exit(1)

    print()
    print("=" * 60)
    print("[SUCCESS] Setup Complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Run the ingestion script to load your book content:")
    print("   py -m api.ingest docs")
    print()
    print("2. Test the API locally:")
    print("   py -m uvicorn api.chat:app --reload")
    print()
    print("3. Deploy to Vercel:")
    print("   vercel --prod")
    print()


if __name__ == "__main__":
    main()
