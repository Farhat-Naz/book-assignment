"""Vercel serverless function for chat endpoint."""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uuid
from .rag import rag_chatbot
from .config import settings


# Initialize FastAPI app
app = FastAPI(title="RAG Chatbot API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
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


@app.post("/api/chat", response_model=ChatResponse)
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


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "RAG Chatbot API"}


# Vercel serverless function handler
def handler(request, context):
    """Handler for Vercel serverless function."""
    return app(request, context)
