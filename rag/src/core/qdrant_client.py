"""
Qdrant vector database client initialization and utilities
"""
from qdrant_client.models import Distance, VectorParams, PointStruct
from typing import List, Dict, Any, Optional
import logging
import sys
import os

# Add the rag directory to the path to import temp_qdrant_mock
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.core.config import settings

logger = logging.getLogger(__name__)


class QdrantVectorStore:
    """
    Wrapper class for Qdrant client operations
    """

    def __init__(self):
        """Initialize Qdrant client for either local or cloud"""
        # Check if using placeholder credentials
        is_placeholder = (
            'your-cluster-url' in settings.QDRANT_HOST or
            'your-actual-api-key' in settings.QDRANT_API_KEY or
            settings.QDRANT_API_KEY == 'your-actual-api-key'
        )

        if is_placeholder:
            logger.info("Using in-memory mock Qdrant (placeholder credentials detected)")
            from temp_qdrant_mock import mock_client
            self.client = mock_client
        else:
            try:
                from qdrant_client import QdrantClient

                # Determine if this is a cloud URL (contains 'qdrant' or 'https')
                if 'qdrant' in settings.QDRANT_HOST.lower() or settings.QDRANT_HOST.startswith('http'):
                    # For Qdrant Cloud, use URL and API key
                    self.client = QdrantClient(
                        url=settings.QDRANT_HOST,
                        api_key=settings.QDRANT_API_KEY,
                        https=True
                    )
                    logger.info(f"Qdrant Cloud client initialized: {settings.QDRANT_HOST}")
                else:
                    # For local Qdrant, use host and port
                    self.client = QdrantClient(
                        host=settings.QDRANT_HOST,
                        port=settings.QDRANT_PORT,
                    )
                    logger.info(f"Qdrant client initialized: {settings.QDRANT_HOST}:{settings.QDRANT_PORT}")

            except Exception as e:
                logger.warning(f"Could not connect to Qdrant: {str(e)}")
                logger.info("Using in-memory mock Qdrant for development")
                from temp_qdrant_mock import mock_client
                self.client = mock_client

        self.collection_name = settings.QDRANT_COLLECTION_NAME

    def create_collection(self, vector_size: int = None) -> None:
        """
        Create a new collection if it doesn't exist

        Args:
            vector_size: Dimension of vectors (default from settings)
        """
        vector_size = vector_size or settings.QDRANT_VECTOR_SIZE

        try:
            # Check if collection exists
            collections = self.client.get_collections().collections
            collection_names = [col.name for col in collections]

            if self.collection_name not in collection_names:
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(
                        size=vector_size,
                        distance=Distance.COSINE,
                    ),
                )
                logger.info(f"Created collection: {self.collection_name}")
            else:
                logger.info(f"Collection already exists: {self.collection_name}")

        except Exception as e:
            logger.error(f"Error creating collection: {str(e)}")
            raise

    def insert_points(self, points: List[PointStruct]) -> None:
        """
        Insert points into the collection

        Args:
            points: List of PointStruct objects with id, vector, and payload
        """
        try:
            self.client.upsert(
                collection_name=self.collection_name,
                points=points,
            )
            logger.info(f"Inserted {len(points)} points into {self.collection_name}")

        except Exception as e:
            logger.error(f"Error inserting points: {str(e)}")
            raise

    def search(
        self,
        query_vector: List[float],
        top_k: int = None,
        score_threshold: float = None,
        filter_dict: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Search for similar vectors in the collection

        Args:
            query_vector: Query embedding vector
            top_k: Number of results to return (default from settings)
            score_threshold: Minimum similarity score (default from settings)
            filter_dict: Optional filter conditions (e.g., {"chapter": "chapter-1"})

        Returns:
            List of search results with score, id, and payload
        """
        top_k = top_k or settings.RAG_TOP_K
        score_threshold = score_threshold or settings.RAG_SCORE_THRESHOLD

        try:
            from qdrant_client.models import Filter

            search_result = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_vector,
                limit=top_k,
                score_threshold=score_threshold,
                filter=self._convert_filter(filter_dict) if filter_dict else None,
            )

            results = []
            for hit in search_result:
                results.append({
                    "id": hit.id,
                    "score": hit.score,
                    "payload": hit.payload,
                })

            logger.info(f"Search returned {len(results)} results")
            return results

        except Exception as e:
            logger.error(f"Error searching: {str(e)}")
            raise

    def _convert_filter(self, filter_dict: Dict[str, Any]):
        """Convert simple filter dict to Qdrant Filter object"""
        from qdrant_client.models import Filter, FieldCondition, Match
        conditions = []

        for key, value in filter_dict.items():
            if isinstance(value, dict) and '$in' in value:
                # Handle "$in" queries
                conditions.append(
                    FieldCondition(
                        key=key,
                        match=Match(any=value['$in'])
                    )
                )
            else:
                # Handle simple equality
                conditions.append(
                    FieldCondition(
                        key=key,
                        match=Match(value=value)
                    )
                )

        return Filter(must=conditions)

    def delete_collection(self) -> None:
        """Delete the collection"""
        try:
            self.client.delete_collection(collection_name=self.collection_name)
            logger.info(f"Deleted collection: {self.collection_name}")

        except Exception as e:
            logger.error(f"Error deleting collection: {str(e)}")
            raise

    def get_collection_info(self) -> Dict[str, Any]:
        """Get collection information"""
        try:
            info = self.client.get_collection(collection_name=self.collection_name)
            return {
                "name": self.collection_name,
                "vectors_count": info.vectors_count,
                "points_count": info.points_count,
                "status": info.status,
            }

        except Exception as e:
            logger.error(f"Error getting collection info: {str(e)}")
            raise


# Global Qdrant client instance
qdrant_store = QdrantVectorStore()
