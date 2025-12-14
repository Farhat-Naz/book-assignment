"""
Embedding service for generating vector representations of text
"""
import asyncio
from typing import List, Dict, Any
import numpy as np
from qdrant_client.http.models import PointStruct
import logging
from sentence_transformers import SentenceTransformer
from src.services.text_chunker import TextChunk

logger = logging.getLogger(__name__)


class EmbeddingService:
    """Service for generating embeddings using various models"""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedding service
        
        Args:
            model_name: Name of the sentence transformer model to use
        """
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
        logger.info(f"Initialized embedding service with model: {model_name}")
    
    async def embed_text(self, text: str) -> List[float]:
        """Generate embedding for a single text"""
        try:
            embedding = self.model.encode([text])[0].tolist()
            return embedding
        except Exception as e:
            logger.error(f"Error embedding text: {str(e)}")
            raise
    
    async def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts"""
        try:
            embeddings = self.model.encode(texts).tolist()
            return embeddings
        except Exception as e:
            logger.error(f"Error embedding texts: {str(e)}")
            raise
    
    async def embed_chunks(self, chunks: List[TextChunk]) -> List[PointStruct]:
        """Convert text chunks into Qdrant PointStruct objects with embeddings"""
        if not chunks:
            return []
        
        # Extract content from chunks to embed
        texts = [chunk.content for chunk in chunks]
        
        # Generate embeddings
        embeddings = await self.embed_texts(texts)
        
        # Create PointStruct objects
        points = []
        for i, chunk in enumerate(chunks):
            point = PointStruct(
                id=chunk.id,
                vector=embeddings[i],
                payload={
                    "content": chunk.content,
                    "metadata": chunk.metadata,
                    "doc_id": chunk.metadata.get("doc_id"),
                    "chunk_index": chunk.chunk_index,
                    "total_chunks": chunk.total_chunks,
                }
            )
            points.append(point)
        
        logger.info(f"Embedded {len(chunks)} chunks into {len(points)} Qdrant points")
        return points
    
    async def embed_query(self, query: str) -> List[float]:
        """Generate embedding for a query (used for semantic search)"""
        try:
            embedding = self.model.encode([query])[0].tolist()
            return embedding
        except Exception as e:
            logger.error(f"Error embedding query: {str(e)}")
            raise


# Example usage
async def test_embeddings():
    """Test function for embeddings"""
    service = EmbeddingService()
    
    # Test single text
    test_text = "This is a test sentence for embedding."
    embedding = await service.embed_text(test_text)
    print(f"Single text embedding shape: {len(embedding)}")
    
    # Test multiple texts
    test_texts = [
        "First test sentence.",
        "Second test sentence.",
        "Third test sentence."
    ]
    embeddings = await service.embed_texts(test_texts)
    print(f"Multiple texts embeddings shape: {len(embeddings)} texts, first has {len(embeddings[0])} dimensions")
    
    # Return the service for use
    return service