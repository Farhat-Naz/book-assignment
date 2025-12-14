"""
RAG Service - FastAPI application for AI-powered chatbot with vector search
"""
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import settings
from src.core.qdrant_client import qdrant_store
from src.services.document_loader import UniversalDocLoader
from src.services.text_chunker import TextChunker, async_chunk_documents
from src.services.embedding_service import EmbeddingService
import logging
import json
from typing import Optional, Dict, Any
from anthropic import AsyncAnthropic

# Configure logging
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app instance
app = FastAPI(
    title="Physical AI RAG Service",
    description="AI-powered RAG chatbot with Qdrant vector search and Claude LLM",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
embedding_service = EmbeddingService()
doc_loader = UniversalDocLoader()
chunker = TextChunker()
anthropic_client = AsyncAnthropic(api_key=settings.CLAUDE_API_KEY)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Physical AI RAG Service",
        "version": "1.0.0",
        "status": "running",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "service": "rag"}


@app.websocket("/ws/chat")
async def chat_websocket(websocket: WebSocket):
    """
    WebSocket endpoint for real-time chat interaction

    Expected message format:
    {
        "query": "user question",
        "chapter_filter": ["chapter-1", "chapter-2"] (optional)
    }

    Response format:
    {
        "type": "chunk" | "complete" | "error",
        "content": "response text",
        "sources": [{"chapter": "...", "title": "...", "score": 0.95}],
        "error": "error message" (if type=error)
    }
    """
    await websocket.accept()
    logger.info("WebSocket connection established")

    try:
        while True:
            # Receive message from client
            data = await websocket.receive_json()
            query = data.get("query", "")
            chapter_filter = data.get("chapter_filter", None)

            if not query:
                await websocket.send_json({
                    "type": "error",
                    "error": "Query cannot be empty"
                })
                continue

            logger.info(f"Received query: {query}")

            try:
                # 1. Generate embedding for query
                query_embedding = await embedding_service.embed_query(query)

                # 2. Search Qdrant for relevant chunks with optional chapter filter
                filter_dict = None
                if chapter_filter:
                    # Filter by chapter if provided
                    filter_dict = {"chapter": {"$in": chapter_filter}}
                
                search_results = qdrant_store.search(
                    query_vector=query_embedding,
                    top_k=settings.RAG_TOP_K,
                    score_threshold=settings.RAG_SCORE_THRESHOLD,
                    filter_dict=filter_dict
                )

                if not search_results:
                    await websocket.send_json({
                        "type": "complete",
                        "content": "I couldn't find any relevant information in the course materials to answer your question. Could you try rephrasing or ask about a different topic?",
                        "sources": []
                    })
                    continue

                # 3. Construct context from search results
                context_parts = []
                sources = []
                
                for result in search_results:
                    payload = result["payload"]
                    content = payload.get("content", "")
                    metadata = payload.get("metadata", {})
                    
                    context_parts.append(content)
                    
                    sources.append({
                        "id": result["id"],
                        "score": result["score"],
                        "source": metadata.get("source", "Unknown"),
                        "chunk_index": metadata.get("chunk_index", 0),
                        "total_chunks": metadata.get("total_chunks", 1)
                    })

                context = "\n\n".join(context_parts)

                # 4. Generate response using Claude
                prompt = f"""
                You are a helpful assistant for the Physical AI & Humanoid Robotics course.
                Answer the user's question based on the provided context from course materials.
                
                Question: {query}
                
                Context: {context}
                
                Please provide a clear, concise answer based on the context provided.
                If the context doesn't contain enough information to answer the question, 
                let the user know and suggest they might want to check other course materials.
                """

                response = await anthropic_client.messages.create(
                    model=settings.CLAUDE_MODEL,
                    max_tokens=settings.CLAUDE_MAX_TOKENS,
                    messages=[{"role": "user", "content": prompt}]
                )

                claude_response = response.content[0].text if response.content else "I couldn't generate a response."

                # 5. Send response back to client
                await websocket.send_json({
                    "type": "complete",
                    "content": claude_response,
                    "sources": sources
                })

            except Exception as e:
                logger.error(f"Error processing query: {str(e)}")
                await websocket.send_json({
                    "type": "error",
                    "error": f"Error processing your request: {str(e)}"
                })

    except WebSocketDisconnect:
        logger.info("WebSocket connection closed")
    except Exception as e:
        logger.error(f"WebSocket error: {str(e)}")
        try:
            await websocket.send_json({
                "type": "error",
                "error": str(e)
            })
        except:
            pass


@app.post("/api/v1/documents/load")
async def load_documents_from_path(path: str):
    """Load documents from a specified path"""
    try:
        documents = await doc_loader.load_from_path(path)
        return {
            "status": "success",
            "documents_loaded": len(documents),
            "documents": documents
        }
    except Exception as e:
        logger.error(f"Error loading documents: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }


@app.post("/api/v1/documents/chunk")
async def chunk_documents(documents: list):
    """Chunk loaded documents"""
    try:
        chunks = await async_chunk_documents(documents)
        return {
            "status": "success",
            "chunks_created": len(chunks),
            "chunks": [{"id": c.id, "content": c.content[:100] + "..." if len(c.content) > 100 else c.content, "metadata": c.metadata} for c in chunks]
        }
    except Exception as e:
        logger.error(f"Error chunking documents: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }


@app.post("/api/v1/embeddings/create")
async def create_embeddings(documents: list):
    """Create embeddings for documents and store in Qdrant"""
    try:
        # First chunk the documents
        chunks = await async_chunk_documents(documents)
        
        # Then create embeddings for the chunks
        points = await embedding_service.embed_chunks(chunks)
        
        # Upsert to Qdrant
        qdrant_store.insert_points(points)
        
        return {
            "status": "success",
            "embeddings_created": len(points),
            "collection": qdrant_store.collection_name
        }
    except Exception as e:
        logger.error(f"Error creating embeddings: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }


@app.get("/api/v1/documents/info")
async def get_document_info():
    """Get information about the stored documents in Qdrant"""
    try:
        info = qdrant_store.get_collection_info()
        return info
    except Exception as e:
        logger.error(f"Error getting collection info: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }


# Create collection and load documents on startup
@app.on_event("startup")
async def startup_event():
    """Initialize Qdrant collection and load documents on startup"""
    try:
        # Create collection
        qdrant_store.create_collection()
        logger.info("Qdrant collection initialized")

        # Load documents from website/docs
        import os
        from pathlib import Path

        docs_path = os.path.join(os.path.dirname(__file__), '..', '..', 'website', 'docs')

        if os.path.exists(docs_path):
            logger.info(f"Loading documents from {docs_path}")

            # Load documents
            documents = await doc_loader.load_from_path(docs_path)
            logger.info(f"Loaded {len(documents)} documents")

            if documents:
                # Chunk documents
                chunks = await async_chunk_documents(documents, chunk_size=512, overlap=50)
                logger.info(f"Created {len(chunks)} chunks")

                # Generate embeddings and insert
                points = await embedding_service.embed_chunks(chunks)
                logger.info(f"Generated {len(points)} embeddings")

                # Insert into Qdrant
                qdrant_store.insert_points(points)
                logger.info(f"Inserted {len(points)} vectors into Qdrant")

                # Get collection info
                info = qdrant_store.get_collection_info()
                logger.info(f"Collection ready: {info.get('points_count', 0)} points, status: {info.get('status', 'unknown')}")
        else:
            logger.warning(f"Documents path not found: {docs_path}")

    except Exception as e:
        logger.error(f"Error during startup: {str(e)}")