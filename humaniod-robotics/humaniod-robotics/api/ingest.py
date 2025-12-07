"""Document ingestion script to embed book content into Qdrant."""
import os
import re
import hashlib
from pathlib import Path
from typing import List, Dict
from openai import OpenAI
from .config import settings
from .database import vector_db


class DocumentIngestion:
    """Handle document processing and embedding."""

    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.vector_db = vector_db

    def extract_markdown_files(self, docs_dir: str) -> List[Dict[str, str]]:
        """
        Extract all markdown files from the docs directory.

        Args:
            docs_dir: Path to the docs directory

        Returns:
            List of dicts with file path and content
        """
        markdown_files = []
        docs_path = Path(docs_dir)

        for md_file in docs_path.rglob("*.md"):
            if md_file.is_file():
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()

                # Get relative path for source tracking
                rel_path = md_file.relative_to(docs_path)

                markdown_files.append({
                    "path": str(rel_path),
                    "content": content,
                    "title": self.extract_title(content)
                })

        return markdown_files

    def extract_title(self, content: str) -> str:
        """Extract title from markdown content."""
        # Try to find the first H1 heading
        match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if match:
            return match.group(1).strip()

        # Try to find title in frontmatter
        frontmatter_match = re.search(
            r"^---\s+title:\s+(.+?)\s+",
            content,
            re.MULTILINE
        )
        if frontmatter_match:
            return frontmatter_match.group(1).strip()

        return "Untitled"

    def chunk_text(self, text: str, chunk_size: int = None, overlap: int = None) -> List[str]:
        """
        Split text into chunks with overlap.

        Args:
            text: Text to chunk
            chunk_size: Size of each chunk
            overlap: Overlap between chunks

        Returns:
            List of text chunks
        """
        if chunk_size is None:
            chunk_size = settings.CHUNK_SIZE
        if overlap is None:
            overlap = settings.CHUNK_OVERLAP

        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]

            # Try to break at sentence boundary
            if end < len(text):
                last_period = chunk.rfind(". ")
                last_newline = chunk.rfind("\n")
                break_point = max(last_period, last_newline)

                if break_point > chunk_size * 0.5:  # Only break if we're past halfway
                    chunk = chunk[:break_point + 1]

            chunks.append(chunk.strip())
            start += len(chunk) - overlap

        return chunks

    def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Create embeddings for a list of texts.

        Args:
            texts: List of texts to embed

        Returns:
            List of embedding vectors
        """
        response = self.client.embeddings.create(
            model=settings.EMBEDDING_MODEL,
            input=texts
        )

        return [data.embedding for data in response.data]

    def generate_id(self, text: str, source: str) -> str:
        """Generate a unique ID for a text chunk."""
        content = f"{source}:{text}"
        return hashlib.md5(content.encode()).hexdigest()

    def ingest_documents(self, docs_dir: str):
        """
        Main ingestion method to process and embed all documents.

        Args:
            docs_dir: Path to the docs directory
        """
        print("[START] Starting document ingestion...")

        # Ensure collection exists
        self.vector_db.create_collection()

        # Extract markdown files
        print("[EXTRACT] Extracting markdown files...")
        documents = self.extract_markdown_files(docs_dir)
        print(f"[INFO] Found {len(documents)} documents")

        # Process documents in batches to avoid memory issues
        batch_size = 50  # Process 50 chunks at a time
        total_chunks_processed = 0

        for doc_idx, doc in enumerate(documents, 1):
            print(f"[PROCESS] ({doc_idx}/{len(documents)}) {doc['path']}")

            # Chunk the document
            chunks = self.chunk_text(doc["content"])

            # Process chunks in batches
            for start_idx in range(0, len(chunks), batch_size):
                end_idx = min(start_idx + batch_size, len(chunks))
                batch_chunks = chunks[start_idx:end_idx]

                # Prepare batch data
                batch_ids = []
                batch_texts = []
                batch_payloads = []

                for i, chunk in enumerate(batch_chunks, start=start_idx):
                    chunk_id = self.generate_id(chunk, doc["path"])
                    batch_ids.append(chunk_id)
                    batch_texts.append(chunk)
                    batch_payloads.append({
                        "text": chunk,
                        "source": doc["path"],
                        "title": doc["title"],
                        "chunk_index": i,
                        "total_chunks": len(chunks)
                    })

                # Create embeddings
                print(f"  [EMBED] Creating embeddings for batch ({start_idx + 1}-{end_idx}/{len(chunks)} chunks)...")
                embeddings = self.create_embeddings(batch_texts)

                # Upload to Qdrant
                self.vector_db.upsert_vectors(
                    ids=batch_ids,
                    vectors=embeddings,
                    payloads=batch_payloads
                )

                total_chunks_processed += len(batch_texts)
                print(f"  [UPLOAD] Uploaded ({total_chunks_processed} total chunks processed)")

        print(f"[CHUNK] Total chunks created and uploaded: {total_chunks_processed}")

        print("[SUCCESS] Document ingestion complete!")


# Script entry point
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m api.ingest <path_to_docs_dir>")
        sys.exit(1)

    docs_dir = sys.argv[1]

    if not os.path.exists(docs_dir):
        print(f"Error: Directory {docs_dir} does not exist")
        sys.exit(1)

    ingestion = DocumentIngestion()
    ingestion.ingest_documents(docs_dir)
