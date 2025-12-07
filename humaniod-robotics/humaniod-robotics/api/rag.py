"""RAG (Retrieval-Augmented Generation) logic."""
from typing import List, Dict, Optional
from openai import OpenAI
from .config import settings
from .database import vector_db, postgres_db


class RAGChatbot:
    """RAG-powered chatbot for answering questions about the book."""

    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.vector_db = vector_db
        self.postgres_db = postgres_db

    def create_embedding(self, text: str) -> List[float]:
        """Create embedding for a text using OpenAI."""
        response = self.client.embeddings.create(
            model=settings.EMBEDDING_MODEL,
            input=text
        )
        return response.data[0].embedding

    def retrieve_context(
        self,
        query: str,
        selected_text: Optional[str] = None,
        top_k: int = None
    ) -> List[Dict]:
        """
        Retrieve relevant context from the vector database.

        Args:
            query: User's question
            selected_text: Text selected by user (if any)
            top_k: Number of results to retrieve

        Returns:
            List of relevant context chunks with metadata
        """
        if top_k is None:
            top_k = settings.TOP_K_RESULTS

        # If user selected text, prioritize it
        if selected_text:
            # Create embedding for selected text and search for similar content
            query_embedding = self.create_embedding(f"{query} {selected_text}")
        else:
            # Just use the query
            query_embedding = self.create_embedding(query)

        # Search vector database
        results = self.vector_db.search(
            query_vector=query_embedding,
            limit=top_k,
            score_threshold=0.7
        )

        return results

    def generate_response(
        self,
        query: str,
        context_chunks: List[Dict],
        selected_text: Optional[str] = None,
        chat_history: List[Dict] = None
    ) -> Dict[str, str]:
        """
        Generate a response using OpenAI with retrieved context.

        Args:
            query: User's question
            context_chunks: Retrieved context from vector database
            selected_text: Text selected by user (if any)
            chat_history: Previous messages in the conversation

        Returns:
            Dict with answer and sources
        """
        # Build context from retrieved chunks
        context_parts = []

        if selected_text:
            context_parts.append(f"SELECTED TEXT:\n{selected_text}\n")

        if context_chunks:
            context_parts.append("RELEVANT BOOK CONTENT:")
            for i, chunk in enumerate(context_chunks, 1):
                payload = chunk.get("payload", {})
                text = payload.get("text", "")
                source = payload.get("source", "Unknown")
                context_parts.append(
                    f"\n[Source {i}: {source}]\n{text}"
                )

        full_context = "\n".join(context_parts)

        # Build system message
        system_message = {
            "role": "system",
            "content": """You are an AI assistant helping users understand the "Physical AI & Humanoid Robotics" book.

Your responsibilities:
1. Answer questions accurately based on the provided book content
2. If the user has selected text, prioritize that text in your answer
3. Cite sources from the book when possible
4. If the answer is not in the provided context, say so politely
5. Be concise but comprehensive

When answering:
- Use technical terminology from the book
- Provide examples when helpful
- Reference specific chapters or sections when relevant
"""
        }

        # Build messages for the chat
        messages = [system_message]

        # Add chat history if available
        if chat_history:
            for msg in chat_history[-5:]:  # Last 5 messages
                messages.append({
                    "role": msg.get("role", "user"),
                    "content": msg.get("content", "")
                })

        # Add current query with context
        user_message = f"""Context from the book:
{full_context}

Question: {query}
"""

        messages.append({"role": "user", "content": user_message})

        # Generate response
        response = self.client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )

        answer = response.choices[0].message.content

        # Extract sources
        sources = [
            {
                "source": chunk.get("payload", {}).get("source", "Unknown"),
                "score": chunk.get("score", 0),
                "text_preview": chunk.get("payload", {}).get("text", "")[:200]
            }
            for chunk in context_chunks
        ]

        return {
            "answer": answer,
            "sources": sources,
            "context_used": full_context
        }

    def chat(
        self,
        session_id: str,
        query: str,
        selected_text: Optional[str] = None
    ) -> Dict[str, any]:
        """
        Main chat method that orchestrates the RAG pipeline.

        Args:
            session_id: Unique session ID for the conversation
            query: User's question
            selected_text: Text selected by user (if any)

        Returns:
            Response dict with answer, sources, and metadata
        """
        # Get chat history
        chat_history = self.postgres_db.get_chat_history(session_id)

        # Retrieve relevant context
        context_chunks = self.retrieve_context(query, selected_text)

        # Generate response
        result = self.generate_response(
            query=query,
            context_chunks=context_chunks,
            selected_text=selected_text,
            chat_history=chat_history
        )

        # Save the conversation
        self.postgres_db.save_message(
            session_id=session_id,
            role="user",
            content=query
        )

        self.postgres_db.save_message(
            session_id=session_id,
            role="assistant",
            content=result["answer"],
            context_used=result.get("context_used", "")
        )

        return {
            "answer": result["answer"],
            "sources": result["sources"],
            "has_selected_text": selected_text is not None
        }


# Global chatbot instance
rag_chatbot = RAGChatbot()
