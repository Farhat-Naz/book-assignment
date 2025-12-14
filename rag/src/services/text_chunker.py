"""
Text chunking service for breaking down documents into manageable pieces
"""
import asyncio
from typing import List, Dict, Any
from dataclasses import dataclass
import logging
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class TextChunk:
    """Represents a chunk of text with metadata"""
    id: str
    content: str
    metadata: Dict[str, Any]
    chunk_index: int
    total_chunks: int


class TextChunker:
    """Service for chunking text documents into smaller pieces"""
    
    def __init__(self, chunk_size: int = 512, overlap: int = 50, separator: str = "\n\n"):
        """
        Initialize the text chunker
        
        Args:
            chunk_size: Maximum size of each chunk (in tokens/words/characters)
            overlap: Number of overlapping characters between chunks
            separator: Character(s) used to split text
        """
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.separator = separator
    
    def chunk_document(self, document: Dict[str, Any], doc_id: Optional[str] = None) -> List[TextChunk]:
        """
        Chunk a single document into smaller pieces
        
        Args:
            document: Dictionary with 'content' and 'metadata' keys
            doc_id: Optional ID to assign to document chunks
        
        Returns:
            List of TextChunk objects
        """
        content = document.get("content", "")
        original_metadata = document.get("metadata", {})
        doc_source = original_metadata.get("source", "unknown")
        
        # Split content by separator, but fallback to character-level splitting if that doesn't work
        chunks = []
        
        if self.separator in content:
            # Use separator-based splitting
            parts = content.split(self.separator)
            chunks = self._assemble_chunks(parts)
        else:
            # Fall back to character-based splitting
            chunks = self._split_by_length(content)
        
        # Create TextChunk objects with metadata
        text_chunks = []
        for idx, chunk_text in enumerate(chunks):
            if len(chunk_text.strip()) == 0:
                continue  # Skip empty chunks
                
            chunk_id = f"{doc_id}_{idx}" if doc_id else f"{hash(doc_source)}_{idx}"
            
            chunk_metadata = {
                **original_metadata,
                "chunk_index": idx,
                "total_chunks": len(chunks),
                "doc_id": doc_id or doc_source,
                "chunk_source": f"{doc_source}_chunk_{idx}",
            }
            
            text_chunk = TextChunk(
                id=chunk_id,
                content=chunk_text.strip(),
                metadata=chunk_metadata,
                chunk_index=idx,
                total_chunks=len(chunks)
            )
            
            text_chunks.append(text_chunk)
        
        logger.info(f"Chunked document {doc_source} into {len(text_chunks)} chunks")
        return text_chunks
    
    def _assemble_chunks(self, parts: List[str]) -> List[str]:
        """Assemble parts into chunks of approximately the right size"""
        chunks = []
        current_chunk = ""
        
        for part in parts:
            # If adding this part would exceed chunk size, start a new chunk
            if len(current_chunk) + len(part) > self.chunk_size and current_chunk:
                chunks.append(current_chunk.strip())
                # Add overlap from the end of the previous chunk
                overlap_start_idx = max(0, len(current_chunk) - self.overlap)
                current_chunk = current_chunk[overlap_start_idx:] + part
            else:
                current_chunk += self.separator + part
        
        # Add the final chunk if it contains content
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def _split_by_length(self, text: str) -> List[str]:
        """Split text by length with overlap"""
        if len(text) <= self.chunk_size:
            return [text]
        
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + self.chunk_size
            
            # If we're near the end, include everything
            if end >= len(text):
                chunks.append(text[start:])
                break
            
            # Add overlap to the next chunk
            chunk = text[start:end]
            chunks.append(chunk)
            
            # Move start forward by chunk_size minus overlap
            start = end - self.overlap
        
        return chunks
    
    def chunk_documents(self, documents: List[Dict[str, Any]]) -> List[TextChunk]:
        """
        Chunk multiple documents
        
        Args:
            documents: List of dictionaries with 'content' and 'metadata' keys
            
        Returns:
            List of TextChunk objects
        """
        all_chunks = []
        
        for idx, doc in enumerate(documents):
            doc_chunks = self.chunk_document(doc, doc_id=f"doc_{idx}")
            all_chunks.extend(doc_chunks)
        
        logger.info(f"Chunked {len(documents)} documents into {len(all_chunks)} total chunks")
        return all_chunks


# Async wrapper for the chunker
async def async_chunk_documents(documents: List[Dict[str, Any]], chunk_size: int = 512, overlap: int = 50) -> List[TextChunk]:
    """Async wrapper for chunking documents"""
    chunker = TextChunker(chunk_size=chunk_size, overlap=overlap)
    return chunker.chunk_documents(documents)