"""Database connections and models."""
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from typing import List, Dict, Any, Optional
from .config import settings

try:
    import psycopg2
    from psycopg2.extras import RealDictCursor
    POSTGRES_AVAILABLE = True
except ImportError:
    POSTGRES_AVAILABLE = False


class PostgresDB:
    """Neon Postgres database handler."""

    def __init__(self):
        self.conn = None
        self.enabled = POSTGRES_AVAILABLE and settings.DATABASE_URL is not None

    def connect(self):
        """Establish connection to Neon Postgres."""
        if not self.enabled:
            return None
        if not self.conn or self.conn.closed:
            self.conn = psycopg2.connect(
                settings.DATABASE_URL,
                cursor_factory=RealDictCursor
            )
        return self.conn

    def create_tables(self):
        """Create necessary tables for chat history."""
        if not self.enabled:
            return
        conn = self.connect()
        if not conn:
            return
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS chat_sessions (
                    id SERIAL PRIMARY KEY,
                    session_id VARCHAR(255) UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS chat_messages (
                    id SERIAL PRIMARY KEY,
                    session_id VARCHAR(255) NOT NULL,
                    role VARCHAR(50) NOT NULL,
                    content TEXT NOT NULL,
                    context_used TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (session_id) REFERENCES chat_sessions(session_id)
                )
            """)

            conn.commit()

    def save_message(
        self,
        session_id: str,
        role: str,
        content: str,
        context_used: str = None
    ):
        """Save a chat message to the database."""
        if not self.enabled:
            return
        conn = self.connect()
        if not conn:
            return
        with conn.cursor() as cur:
            # Ensure session exists
            cur.execute("""
                INSERT INTO chat_sessions (session_id)
                VALUES (%s)
                ON CONFLICT (session_id) DO UPDATE
                SET updated_at = CURRENT_TIMESTAMP
            """, (session_id,))

            # Insert message
            cur.execute("""
                INSERT INTO chat_messages (session_id, role, content, context_used)
                VALUES (%s, %s, %s, %s)
            """, (session_id, role, content, context_used))

            conn.commit()

    def get_chat_history(self, session_id: str, limit: int = 10) -> List[Dict]:
        """Retrieve chat history for a session."""
        if not self.enabled:
            return []
        conn = self.connect()
        if not conn:
            return []
        with conn.cursor() as cur:
            cur.execute("""
                SELECT role, content, created_at
                FROM chat_messages
                WHERE session_id = %s
                ORDER BY created_at DESC
                LIMIT %s
            """, (session_id, limit))

            return list(reversed(cur.fetchall()))

    def close(self):
        """Close the database connection."""
        if self.conn and not self.conn.closed:
            self.conn.close()


class VectorDB:
    """Qdrant vector database handler."""

    def __init__(self):
        self.client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
        self.collection_name = settings.QDRANT_COLLECTION

    def create_collection(self, vector_size: int = 1536):
        """Create collection if it doesn't exist."""
        try:
            self.client.get_collection(self.collection_name)
        except Exception:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE
                )
            )

    def upsert_vectors(
        self,
        ids: List[str],
        vectors: List[List[float]],
        payloads: List[Dict[str, Any]]
    ):
        """Insert or update vectors in the collection."""
        points = [
            PointStruct(id=id_, vector=vector, payload=payload)
            for id_, vector, payload in zip(ids, vectors, payloads)
        ]

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

    def search(
        self,
        query_vector: List[float],
        limit: int = 5,
        score_threshold: float = 0.7
    ) -> List[Dict]:
        """Search for similar vectors."""
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=limit,
            score_threshold=score_threshold
        )

        return [
            {
                "id": hit.id,
                "score": hit.score,
                "payload": hit.payload
            }
            for hit in results
        ]


# Global database instances
postgres_db = PostgresDB()
vector_db = VectorDB()
