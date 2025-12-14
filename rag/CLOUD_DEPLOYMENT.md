# RAG Backend Cloud Deployment Guide

This guide shows you how to deploy the RAG backend to the cloud so your Vercel website can connect to it.

## Quick Deploy Options

Choose one of these platforms for deploying your RAG backend:

### Option 1: Railway (Recommended - Easiest)

**Why Railway?**
- Free tier with $5/month credit
- Automatic HTTPS and WebSocket support
- One-click deploy from GitHub
- Built-in environment variables

**Steps:**

1. **Sign up**: Go to [Railway.app](https://railway.app/) and sign in with GitHub

2. **Create New Project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository: `Farhat-Naz/newhumandiod-book`
   - Select root directory: `rag`

3. **Configure Environment Variables**:
   Click "Variables" and add:
   ```
   QDRANT_HOST=your-cluster-url.qdrant.io
   QDRANT_API_KEY=your-qdrant-api-key
   CLAUDE_API_KEY=your-claude-api-key
   ALLOWED_ORIGINS=["https://your-vercel-app.vercel.app"]
   ```

4. **Deploy**:
   - Railway will auto-detect Python and install dependencies
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`

5. **Get Your URL**:
   - After deployment, Railway gives you a URL like: `https://your-app.railway.app`
   - Your WebSocket URL will be: `wss://your-app.railway.app/ws/chat`

6. **Update Vercel**:
   In Vercel, add environment variable:
   ```
   REACT_APP_RAG_BACKEND_URL=wss://your-app.railway.app/ws/chat
   ```

### Option 2: Render

**Why Render?**
- Free tier available
- Good for Python apps
- Automatic deploys from GitHub

**Steps:**

1. **Sign up**: Go to [Render.com](https://render.com/) and sign in with GitHub

2. **Create Web Service**:
   - Click "New +" → "Web Service"
   - Connect your repository
   - Select branch: `master`
   - Root directory: `rag`

3. **Configure Service**:
   ```
   Name: rag-backend
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn src.main:app --host 0.0.0.0 --port $PORT
   ```

4. **Add Environment Variables**:
   ```
   QDRANT_HOST=your-cluster-url.qdrant.io
   QDRANT_API_KEY=your-qdrant-api-key
   CLAUDE_API_KEY=your-claude-api-key
   ALLOWED_ORIGINS=["https://your-vercel-app.vercel.app"]
   ```

5. **Deploy**:
   - Render will deploy automatically
   - You'll get a URL like: `https://rag-backend.onrender.com`

### Option 3: Fly.io

**Why Fly.io?**
- Good global performance
- WebSocket support
- Free tier with resource limits

**Steps:**

1. **Install Fly CLI**:
   ```bash
   # Windows
   powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
   ```

2. **Login and Initialize**:
   ```bash
   cd rag
   fly auth login
   fly launch
   ```

3. **Configure** (when prompted):
   - App name: `rag-backend-[your-name]`
   - Region: Choose closest to you
   - Database: No

4. **Set Environment Variables**:
   ```bash
   fly secrets set QDRANT_HOST=your-cluster-url.qdrant.io
   fly secrets set QDRANT_API_KEY=your-qdrant-api-key
   fly secrets set CLAUDE_API_KEY=your-claude-api-key
   fly secrets set ALLOWED_ORIGINS='["https://your-vercel-app.vercel.app"]'
   ```

5. **Deploy**:
   ```bash
   fly deploy
   ```

## Required Files for Deployment

### 1. Create `rag/runtime.txt` (for Python version)

```
python-3.11
```

### 2. Update `rag/requirements.txt`

Make sure it includes all dependencies:
```
fastapi>=0.104.1
uvicorn[standard]>=0.24.0
websockets>=12.0
python-multipart==0.0.20
sentence-transformers>=2.5.0
qdrant-client>=1.7.0
anthropic>=0.40.0
pydantic-settings==2.1.0
PyPDF2>=3.0.0
python-docx>=1.1.0
python-dotenv>=1.0.0
```

### 3. Create `rag/Procfile` (for some platforms)

```
web: uvicorn src.main:app --host 0.0.0.0 --port $PORT
```

## Connecting Website to Cloud Backend

### Update Vercel Environment Variables

1. Go to your Vercel project → Settings → Environment Variables

2. Add:
   ```
   Variable: REACT_APP_RAG_BACKEND_URL
   Value: wss://your-backend.railway.app/ws/chat
   ```

3. Redeploy your Vercel site for changes to take effect

### Alternative: Update in Code

Edit `website/docusaurus.config.ts`:

```typescript
customFields: {
  RAG_BACKEND_URL: process.env.RAG_BACKEND_URL || 'wss://your-backend.railway.app/ws/chat',
},
```

Then in `ChatBot/index.tsx`, access it:
```typescript
const WS_URL = (useDocusaurusContext().siteConfig.customFields.RAG_BACKEND_URL as string) || null;
```

## Testing Your Deployment

### 1. Test Backend Health

```bash
curl https://your-backend.railway.app/health
```

Should return:
```json
{"status":"ok","service":"rag"}
```

### 2. Test WebSocket Connection

Use the test HTML file:
1. Edit `test_websocket.html`
2. Change the WebSocket URL to your cloud URL
3. Open in browser and test

### 3. Test from Vercel Site

1. Open your Vercel site
2. Click the chatbot button
3. Should see "✅ Connected"
4. Ask a question to verify

## Cost Estimates

### Railway
- **Free**: $5/month credit (enough for small apps)
- **Hobby**: $5/month for more resources
- **Pro**: $20/month for production

### Render
- **Free**: Limited resources, sleeps after 15 min inactivity
- **Starter**: $7/month for always-on service

### Fly.io
- **Free**: 3 shared-cpu-1x VMs, 3GB persistent storage
- **Paid**: Starts at $1.94/month

## Environment Variables Reference

Required for all platforms:

```bash
# Qdrant Cloud (for vector storage)
QDRANT_HOST=your-cluster.qdrant.io
QDRANT_PORT=443
QDRANT_API_KEY=your-qdrant-api-key
QDRANT_COLLECTION_NAME=course_chapters

# Claude API (for chat responses)
CLAUDE_API_KEY=sk-ant-...
CLAUDE_MODEL=claude-3-5-sonnet-20241022

# CORS (allow your Vercel domain)
ALLOWED_ORIGINS=["https://your-app.vercel.app","http://localhost:3000"]

# RAG Parameters
RAG_TOP_K=5
RAG_SCORE_THRESHOLD=0.3
```

## Troubleshooting

### WebSocket Connection Fails

1. **Check CORS**: Ensure your Vercel URL is in `ALLOWED_ORIGINS`
2. **Use WSS**: Production must use `wss://` not `ws://`
3. **Check Firewall**: Some platforms block WebSocket by default

### Backend Crashes on Startup

1. **Check Logs**: View deployment logs in your platform dashboard
2. **Verify ENV Variables**: All required variables must be set
3. **Check Dependencies**: Ensure all packages in requirements.txt install

### Slow Performance

1. **Upgrade Plan**: Free tiers have limited resources
2. **Add Redis**: Cache embeddings for faster responses
3. **Use Smaller Model**: Switch to a lighter embedding model

## Production Checklist

Before going live:

- [ ] Set up Qdrant Cloud (not using mock)
- [ ] Add real Claude API key
- [ ] Configure CORS with your Vercel domain
- [ ] Test all endpoints
- [ ] Set up monitoring/logging
- [ ] Configure rate limiting
- [ ] Add error tracking (e.g., Sentry)
- [ ] Set up health checks
- [ ] Configure auto-scaling (if needed)

## Next Steps

1. Deploy backend to Railway/Render
2. Get your backend URL
3. Add to Vercel environment variables
4. Redeploy Vercel site
5. Test chatbot on live site

## Support

- Railway: https://docs.railway.app/
- Render: https://render.com/docs
- Fly.io: https://fly.io/docs/

---

**Last Updated**: 2025-12-14
**Platforms Tested**: Railway, Render, Fly.io
