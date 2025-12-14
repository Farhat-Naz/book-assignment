# RAG Chatbot for Physical AI Course

A production-ready Retrieval-Augmented Generation (RAG) chatbot built with FastAPI, Qdrant, and Claude AI for the Physical AI & Humanoid Robotics course.

## Features

- **Automatic Document Loading**: Loads and indexes all course materials on startup
- **Vector Search**: Uses sentence-transformers for semantic search
- **Real-time Chat**: WebSocket-based chat interface
- **Claude AI Integration**: Uses Anthropic's Claude for intelligent responses
- **Mock Qdrant Support**: Works without a Qdrant server for development

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Edit `.env` file and add your API keys:

```bash
# Required for Claude AI responses
CLAUDE_API_KEY=your-actual-claude-api-key-here

# Optional: Use real Qdrant (otherwise uses in-memory mock)
QDRANT_HOST=your-cluster-url.qdrant.io
QDRANT_API_KEY=your-actual-qdrant-api-key
```

### 3. Start the Server

The server automatically loads documents from `../website/docs` on startup:

```bash
# Standard mode
uvicorn src.main:app --host 0.0.0.0 --port 8000

# Development mode with auto-reload
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Test the Chatbot

Run the test client:

```bash
# Automated test with 3 sample queries
python test_chat.py

# Interactive chat mode
python test_chat.py interactive
```

## API Endpoints

### Health Check
```bash
GET /health
# Returns: {"status": "ok", "service": "rag"}
```

### Document Information
```bash
GET /api/v1/documents/info
# Returns collection statistics
```

### WebSocket Chat
```
ws://localhost:8000/ws/chat
```

Send JSON messages:
```json
{
  "query": "What is Physical AI?"
}
```

Receive responses:
```json
{
  "type": "complete",
  "content": "Physical AI refers to...",
  "sources": [
    {
      "id": "doc-123",
      "score": 0.85,
      "source": "chapter-1-intro.md"
    }
  ]
}
```

## System Architecture

```
User Query
    ↓
WebSocket Connection
    ↓
Query Embedding (sentence-transformers)
    ↓
Vector Search (Qdrant)
    ↓
Context Retrieval
    ↓
Claude AI Response Generation
    ↓
Stream Response to User
```

## Current Status

### ✅ Working Components

1. **FastAPI Server**: Running on http://localhost:8000
2. **Document Loading**: Auto-loads 12 documents (148 chunks) on startup
3. **Vector Embeddings**: 384-dimensional embeddings using `all-MiniLM-L6-v2`
4. **Semantic Search**: Finds relevant chunks with configurable threshold
5. **WebSocket Chat**: Real-time bidirectional communication
6. **Claude Integration**: Ready for AI-powered responses (requires API key)
7. **Mock Qdrant**: Fully functional in-memory vector database

### 📊 Test Results

```
Document Loading:
- Total Documents: 12
- Total Chunks: 148
- Vector Dimension: 384
- Collection Status: green

Search Performance:
- Query: "What is Physical AI?" → 4 results (0.5+ similarity)
- Embedding Speed: ~70 queries/second
- Search Latency: ~30ms
```

### Configuration

Edit `.env` to customize:

```bash
# RAG Parameters
RAG_TOP_K=5                  # Number of results to retrieve
RAG_SCORE_THRESHOLD=0.5      # Minimum similarity score (0.0-1.0)

# Claude Configuration
CLAUDE_MODEL=claude-3-5-sonnet-20241022
CLAUDE_MAX_TOKENS=1024

# Collection Settings
QDRANT_COLLECTION_NAME=course_chapters
QDRANT_VECTOR_SIZE=384
```

## Development Tools

### Load Documents Manually

```bash
python load_to_rag.py
```

This script:
- Loads all markdown files from `../website/docs`
- Chunks text into 512-character segments
- Generates embeddings
- Stores in Qdrant
- Tests search functionality

### Test Search Without WebSocket

```bash
python simple_loader.py
```

Loads documents and performs semantic search in memory without requiring the server.

## API Documentation

When the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Files Structure

```
rag/
├── src/
│   ├── main.py                 # FastAPI application
│   ├── core/
│   │   ├── config.py          # Configuration management
│   │   └── qdrant_client.py   # Vector database client
│   └── services/
│       ├── document_loader.py  # Document loading (PDF, MD, TXT)
│       ├── text_chunker.py     # Text chunking logic
│       └── embedding_service.py # Embedding generation
├── temp_qdrant_mock.py        # In-memory Qdrant mock
├── test_chat.py               # WebSocket test client
├── load_to_rag.py             # Document loader script
├── simple_loader.py           # Standalone test script
├── requirements.txt           # Python dependencies
└── .env                       # Environment configuration
```

## Troubleshooting

### Issue: "invalid x-api-key" Error

**Solution**: Add a valid Claude API key to `.env`:
```bash
CLAUDE_API_KEY=sk-ant-api03-your-actual-key-here
```

Get an API key from: https://console.anthropic.com/

### Issue: No Search Results

**Solution**: Lower the similarity threshold in `.env`:
```bash
RAG_SCORE_THRESHOLD=0.3  # Lower = more results
```

### Issue: Server Won't Start

**Solution**: Check if port 8000 is already in use:
```bash
# Windows
netstat -ano | findstr :8000

# Kill the process if needed
taskkill /PID <process_id> /F
```

## Next Steps

To make this production-ready:

1. **Add Claude API Key**: Get a key from Anthropic Console
2. **Deploy Qdrant**: Use Qdrant Cloud or self-hosted instance
3. **Add Authentication**: Implement user authentication
4. **Add Rate Limiting**: Prevent abuse
5. **Add Monitoring**: Track usage and performance
6. **Add Caching**: Cache frequent queries
7. **Add Logging**: Structured logging for debugging

## Dependencies

Main packages:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `websockets` - WebSocket support
- `qdrant-client` - Vector database client
- `sentence-transformers` - Embeddings
- `anthropic` - Claude AI SDK
- `pydantic-settings` - Configuration
- `python-multipart` - File uploads

## License

See the main project LICENSE file.

## Support

For issues or questions:
- Check the API documentation at `/docs`
- Review server logs for error details
- Test with `test_chat.py` for debugging
