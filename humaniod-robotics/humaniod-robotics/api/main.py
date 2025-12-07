"""Main FastAPI application for RAG Chatbot."""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uuid
import os

# Import our RAG components
from .rag import rag_chatbot
from .config import settings

# Initialize FastAPI app
app = FastAPI(
    title="Humanoid Robotics RAG Chatbot API",
    description="AI-powered chatbot for Physical AI & Humanoid Robotics book",
    version="1.0.0"
)

# Add CORS middleware - allow all origins for now
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    """Chat request model."""
    session_id: Optional[str] = None
    query: str
    selected_text: Optional[str] = None


class ChatResponse(BaseModel):
    """Chat response model."""
    session_id: str
    answer: str
    sources: list
    has_selected_text: bool


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Humanoid Robotics RAG Chatbot API",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "RAG Chatbot API",
        "qdrant_collection": settings.QDRANT_COLLECTION
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint for the RAG chatbot.

    Args:
        request: ChatRequest with query and optional selected text

    Returns:
        ChatResponse with answer and sources
    """
    try:
        # Generate session ID if not provided
        session_id = request.session_id or str(uuid.uuid4())

        # Process the chat request
        result = rag_chatbot.chat(
            session_id=session_id,
            query=request.query,
            selected_text=request.selected_text
        )

        return ChatResponse(
            session_id=session_id,
            answer=result["answer"],
            sources=result["sources"],
            has_selected_text=result["has_selected_text"]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# For local development
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
