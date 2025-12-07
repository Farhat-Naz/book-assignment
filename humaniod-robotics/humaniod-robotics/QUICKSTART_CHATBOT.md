# Quick Start Guide: RAG Chatbot Setup

This guide will help you get the RAG chatbot up and running quickly.

## Prerequisites Checklist

Before starting, make sure you have:

- [ ] OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- [ ] Qdrant Cloud account ([Sign up free](https://qdrant.tech/))
- [ ] Neon Serverless Postgres database ([Sign up free](https://neon.tech/))
- [ ] Vercel account ([Sign up free](https://vercel.com/))
- [ ] Python 3.9+ installed locally
- [ ] Node.js 20+ installed locally

## Step 1: Get Your Credentials

### OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy and save it securely

### Qdrant Cloud
1. Sign up at https://qdrant.tech/
2. Create a new cluster (free tier)
3. Get your:
   - Cluster URL (e.g., `https://xyz.qdrant.io`)
   - API Key

### Neon Postgres
1. Sign up at https://neon.tech/
2. Create a new project
3. Copy the connection string (looks like: `postgresql://user:pass@host.neon.tech/db`)

## Step 2: Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and fill in your credentials:
   ```bash
   # OpenAI
   OPENAI_API_KEY=sk-your-key-here
   OPENAI_MODEL=gpt-4-turbo-preview
   EMBEDDING_MODEL=text-embedding-3-small

   # Qdrant
   QDRANT_URL=https://your-cluster.qdrant.io
   QDRANT_API_KEY=your-qdrant-key
   QDRANT_COLLECTION=humanoid_robotics_docs

   # Neon Postgres
   DATABASE_URL=postgresql://user:pass@host.neon.tech/dbname

   # Settings (optional - defaults are fine)
   CHUNK_SIZE=1000
   CHUNK_OVERLAP=200
   TOP_K_RESULTS=5
   ```

## Step 3: Install Dependencies

```bash
# Install Python dependencies
pip install -r api/requirements.txt

# Install Node dependencies (if not already done)
npm install
```

## Step 4: Initialize Databases

Run the setup script to create tables and collections:

```bash
python -m api.setup_db
```

You should see:
```
✅ Postgres tables created successfully!
✅ Qdrant collection 'humanoid_robotics_docs' created successfully!
✅ Setup Complete!
```

## Step 5: Ingest Book Content

Process and embed all your documentation:

```bash
python -m api.ingest docs
```

This will:
- Extract all markdown files
- Create text chunks
- Generate embeddings
- Upload to Qdrant

**Time estimate**: 5-15 minutes depending on content size.

## Step 6: Test Locally (Optional)

Before deploying, test the API locally:

```bash
# Start the API server
uvicorn api.chat:app --reload --port 8000
```

Then in another terminal:

```bash
# Start Docusaurus dev server
npm start
```

Visit http://localhost:3000 and test the chatbot!

## Step 7: Configure Vercel

Add environment variables to Vercel:

### Option A: Using Vercel CLI

```bash
vercel env add OPENAI_API_KEY
# Enter your key when prompted

vercel env add QDRANT_URL
# Enter your URL when prompted

vercel env add QDRANT_API_KEY
# Enter your key when prompted

vercel env add DATABASE_URL
# Enter your connection string when prompted
```

### Option B: Using Vercel Dashboard

1. Go to https://vercel.com/dashboard
2. Select your project
3. Go to Settings → Environment Variables
4. Add each variable:
   - OPENAI_API_KEY
   - QDRANT_URL
   - QDRANT_API_KEY
   - DATABASE_URL
   - (Optional) OPENAI_MODEL, EMBEDDING_MODEL, etc.

**Important**: Make sure to add them for **Production**, **Preview**, and **Development** environments.

## Step 8: Deploy to Vercel

```bash
# Commit your changes (but not .env!)
git add .
git commit -m "Add RAG chatbot integration"

# Deploy to production
git push

# Or deploy directly
vercel --prod
```

## Step 9: Verify Deployment

1. Visit your live site: `https://humaniod-robotics.vercel.app`
2. Look for the chat bubble (💬) in the bottom-right corner
3. Click it and ask a test question
4. Verify you get a response with sources

## Troubleshooting

### "Module not found" errors
```bash
pip install -r api/requirements.txt --force-reinstall
```

### Chatbot not appearing
1. Check browser console for errors
2. Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
3. Verify `src/theme/Root.tsx` exists

### API errors in production
1. Check Vercel function logs
2. Verify all environment variables are set
3. Test `/api/health` endpoint

### No responses from chatbot
1. Ensure ingestion completed successfully
2. Check Qdrant dashboard for documents
3. Verify OpenAI API key is valid

## Next Steps

- Read the full [RAG_CHATBOT_README.md](./RAG_CHATBOT_README.md)
- Customize the chatbot UI in `src/components/Chatbot/`
- Adjust RAG parameters in `api/config.py`
- Monitor usage and costs

## Cost Monitoring

Keep an eye on:
- **OpenAI**: https://platform.openai.com/usage
- **Qdrant**: Check your cluster dashboard
- **Neon**: https://console.neon.tech/
- **Vercel**: https://vercel.com/dashboard/usage

## Support

If you encounter issues:
1. Check the detailed [RAG_CHATBOT_README.md](./RAG_CHATBOT_README.md)
2. Review Vercel deployment logs
3. Check browser console for frontend errors
4. Test API endpoints directly

## Success Checklist

- [ ] All environment variables configured
- [ ] Databases initialized successfully
- [ ] Book content ingested into Qdrant
- [ ] Local testing passed
- [ ] Deployed to Vercel
- [ ] Chatbot appears on live site
- [ ] Test questions get answered with sources

Congratulations! Your RAG chatbot is live! 🎉
