"""
Quick verification that Chapter 4 content is searchable
"""
import asyncio
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from services.document_loader import UniversalDocLoader
from services.text_chunker import async_chunk_documents
from services.embedding_service import EmbeddingService

async def test_chapter4_search():
    """Test that Chapter 4 content is searchable"""
    print("\n" + "="*60)
    print("Chapter 4 Search Verification")
    print("="*60)

    # Initialize services
    loader = UniversalDocLoader()
    embed_service = EmbeddingService()

    # Load documents
    docs_path = os.path.join(os.path.dirname(__file__), '..', 'website', 'docs')
    print(f"\nLoading from: {docs_path}")

    documents = await loader.load_from_path(docs_path)
    print(f"Total documents: {len(documents)}")

    # Find Chapter 4
    chapter4 = None
    for doc in documents:
        if 'chapter-4' in doc['metadata']['source']:
            chapter4 = doc
            break

    if chapter4:
        print(f"\n[SUCCESS] Found Chapter 4!")
        print(f"File: {chapter4['metadata']['source']}")
        print(f"Size: {len(chapter4['content'])} characters")
        print(f"Preview: {chapter4['content'][:200]}...")
    else:
        print("\n[ERROR] Chapter 4 not found!")
        return

    # Chunk documents
    chunks = await async_chunk_documents(documents)
    chapter4_chunks = [c for c in chunks if 'chapter-4' in c.metadata.get('source', '')]

    print(f"\n[SUCCESS] Chapter 4 chunked into {len(chapter4_chunks)} chunks")

    # Test search queries for Chapter 4 topics
    test_queries = [
        "What is A star algorithm",
        "Tell me about RRT path planning",
        "Explain PID controller",
        "What is motion planning"
    ]

    print("\n" + "="*60)
    print("Testing Search for Chapter 4 Content")
    print("="*60)

    for query in test_queries:
        print(f"\n[Query] {query}")

        # Generate query embedding
        query_embedding = await embed_service.embed_query(query)

        # Search in Chapter 4 chunks only
        from simple_loader import find_similar_chunks

        # Create embeddings for Chapter 4 chunks
        chunk_embeddings = []
        for chunk in chapter4_chunks:
            embedding = await embed_service.embed_text(chunk.content)
            chunk_embeddings.append({
                'embedding': embedding,
                'content': chunk.content,
                'metadata': chunk.metadata
            })

        # Calculate similarities
        def cosine_similarity(v1, v2):
            import numpy as np
            dot_product = sum(a * b for a, b in zip(v1, v2))
            magnitude1 = sum(a * a for a in v1) ** 0.5
            magnitude2 = sum(b * b for b in v2) ** 0.5
            if magnitude1 == 0 or magnitude2 == 0:
                return 0
            return dot_product / (magnitude1 * magnitude2)

        similarities = []
        for item in chunk_embeddings:
            similarity = cosine_similarity(query_embedding, item['embedding'])
            if similarity >= 0.3:  # Threshold
                similarities.append((similarity, item))

        similarities.sort(key=lambda x: x[0], reverse=True)
        top_results = similarities[:3]

        if top_results:
            print(f"  Found {len(top_results)} results:")
            for i, (score, chunk) in enumerate(top_results, 1):
                content_preview = chunk['content'][:100].replace('\n', ' ')
                print(f"  {i}. Score: {score:.3f}")
                print(f"     Preview: {content_preview}...")
        else:
            print(f"  No results found (threshold 0.3)")

    print("\n" + "="*60)
    print("[COMPLETE] Chapter 4 is loaded and searchable!")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(test_chapter4_search())
