# RAG Chatbot Integration Guide

This document explains how to set up and use the integrated RAG (Retrieval-Augmented Generation) chatbot for the Physical AI & Humanoid Robotics book.

## Features

- **Intelligent Q&A**: Ask questions about any topic in the book
- **Text Selection**: Select text on the page and ask questions specifically about that content
- **Contextual Responses**: Powered by OpenAI with retrieval from your book content
- **Source Citations**: See which parts of the book were used to answer your question
- **Chat History**: Maintains conversation context using Neon Postgres
- **Floating Widget**: Non-intrusive chat interface that's always available

## Architecture

- **Frontend**: React component integrated into Docusaurus
- **Backend**: FastAPI deployed as Vercel serverless functions (Python)
- **Vector Database**: Qdrant Cloud for semantic search
- **SQL Database**: Neon Serverless Postgres for chat history
- **AI Model**: OpenAI GPT-4 Turbo with embeddings

## Setup Instructions

### 1. Prerequisites

- OpenAI API key
- Qdrant Cloud account (free tier)
- Neon Serverless Postgres database
- Vercel account

### 2. Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
# OpenAI Configuration
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4-turbo-preview
EMBEDDING_MODEL=text-embedding-3-small

# Qdrant Cloud Configuration
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your-api-key
QDRANT_COLLECTION=humanoid_robotics_docs

# Neon Postgres Configuration
DATABASE_URL=postgresql://user:password@host.neon.tech/database

# RAG Settings (optional)
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
TOP_K_RESULTS=5
```

### 3. Install Dependencies

Install Python dependencies for the API:

```bash
pip install -r api/requirements.txt
```

The frontend dependencies are already included in the main package.json.

### 4. Initialize Databases

#### Create Postgres Tables

Run this Python script to create the necessary tables:

```python
from api.database import postgres_db

postgres_db.create_tables()
print("✅ Postgres tables created!")
```

#### Create Qdrant Collection

The collection will be automatically created when you run the ingestion script.

### 5. Ingest Book Content

Process and embed all markdown files from your docs:

```bash
python -m api.ingest docs
```

This will:
1. Extract all markdown files from the `docs/` directory
2. Chunk the content into manageable pieces
3. Create embeddings using OpenAI
4. Upload to Qdrant Cloud

**Note**: This may take several minutes depending on the size of your documentation.

### 6. Configure Vercel Environment Variables

Add your environment variables to Vercel:

```bash
vercel env add OPENAI_API_KEY
vercel env add QDRANT_URL
vercel env add QDRANT_API_KEY
vercel env add DATABASE_URL
```

Or add them through the Vercel dashboard:
1. Go to your project settings
2. Navigate to "Environment Variables"
3. Add each variable for Production, Preview, and Development

### 7. Deploy

Deploy to Vercel:

```bash
vercel --prod
```

The chatbot will now be available on your live site!

## Usage

### For End Users

1. **Open the Chat**: Click the chat bubble icon (💬) in the bottom-right corner
2. **Ask a Question**: Type your question and press Enter
3. **Select Text** (optional): Highlight any text on the page before asking a question
4. **View Sources**: Expand the sources section to see where the answer came from

### For Developers

#### Customizing the Chatbot

The chatbot component is located at `src/components/Chatbot/index.tsx`. You can customize:

- **Styling**: Edit `src/components/Chatbot/styles.module.css`
- **API Endpoint**: Pass a custom `apiEndpoint` prop
- **Behavior**: Modify the component logic

#### Customizing the RAG Pipeline

Edit `api/rag.py` to customize:

- **Prompt engineering**: Modify the system message
- **Context retrieval**: Adjust `TOP_K_RESULTS` or add filters
- **Response generation**: Change model parameters

#### Re-ingesting Content

If you update your documentation, re-run the ingestion:

```bash
python -m api.ingest docs
```

This will update the vector database with new content.

## API Endpoints

### POST /api/chat

Chat with the RAG chatbot.

**Request Body**:
```json
{
  "session_id": "optional-session-id",
  "query": "What is forward kinematics?",
  "selected_text": "optional selected text from the page"
}
```

**Response**:
```json
{
  "session_id": "session_xxx",
  "answer": "Forward kinematics is...",
  "sources": [
    {
      "source": "module-02-kinematics/chapter-3.md",
      "score": 0.89,
      "text_preview": "Forward kinematics refers to..."
    }
  ],
  "has_selected_text": false
}
```

### GET /api/health

Health check endpoint.

**Response**:
```json
{
  "status": "healthy",
  "service": "RAG Chatbot API"
}
```

## Troubleshooting

### Chatbot Not Appearing

1. Check browser console for errors
2. Verify the Root.tsx component is loaded
3. Clear browser cache and reload

### API Errors

1. Check Vercel function logs
2. Verify all environment variables are set
3. Test the `/api/health` endpoint

### No Responses from Chatbot

1. Ensure book content has been ingested
2. Check Qdrant Cloud connection
3. Verify OpenAI API key is valid and has credits

### Slow Responses

1. Consider upgrading Vercel plan for better performance
2. Adjust `TOP_K_RESULTS` to retrieve fewer documents
3. Reduce `CHUNK_SIZE` for faster embedding

## Cost Considerations

- **OpenAI**: Charges per token (embedding + generation)
- **Qdrant Cloud**: Free tier includes 1GB storage
- **Neon**: Free tier includes 0.5GB storage
- **Vercel**: Serverless function execution time

**Estimate**: For a moderately active book with 100-200 queries/day:
- OpenAI: ~$5-10/month
- Qdrant: Free
- Neon: Free
- Vercel: Free (within limits)

## Future Enhancements

- [ ] Add conversation export
- [ ] Implement feedback mechanism
- [ ] Add suggested questions
- [ ] Support for images and diagrams
- [ ] Multi-language support
- [ ] Voice input/output

## Support

For issues or questions:
1. Check the [GitHub Issues](https://github.com/Farhat-Naz/book-assignment/issues)
2. Review Vercel deployment logs
3. Test API endpoints directly

## License

This chatbot integration follows the same license as the main book project.
