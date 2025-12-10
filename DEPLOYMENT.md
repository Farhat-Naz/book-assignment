# Deployment Guide

This guide covers deploying the Physical AI & Humanoid Robotics Learning Platform to production.

## Architecture

The platform consists of 4 services:
- **Website** (Docusaurus) → Vercel
- **Backend** (FastAPI) → Render/Railway
- **RAG Service** → Render/Railway
- **Agent Service** → Render/Railway
- **Databases** → Managed services (PostgreSQL on Render, Qdrant Cloud)

## Prerequisites

- GitHub account with repository access
- Vercel account (for website)
- Render or Railway account (for backend services)
- Anthropic API key (for Claude)
- Qdrant Cloud account (or self-hosted Qdrant)

---

## 1. Deploy Website to Vercel

### Option A: Via Vercel Dashboard (Recommended)

1. **Connect GitHub Repository**
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "Add New Project"
   - Import `Farhat-Naz/newhumandiod-book`

2. **Configure Project**
   - Framework Preset: `Docusaurus`
   - Root Directory: `website`
   - Build Command: `npm run build`
   - Output Directory: `build`
   - Install Command: `npm install`

3. **Environment Variables**
   ```
   NODE_ENV=production
   BACKEND_API_URL=https://your-backend.onrender.com
   RAG_WS_URL=wss://your-rag.onrender.com
   ```

4. **Deploy**
   - Click "Deploy"
   - Vercel will automatically deploy on every push to `master`

### Option B: Via GitHub Actions

1. **Get Vercel Token**
   - Go to Vercel → Settings → Tokens
   - Create a new token

2. **Add GitHub Secrets**
   - Go to GitHub repo → Settings → Secrets and variables → Actions
   - Add: `VERCEL_TOKEN`

3. **Configure Vercel Project**
   ```bash
   cd website
   npm i -g vercel
   vercel login
   vercel link
   ```

4. **Push to trigger deployment**
   - The `.github/workflows/deploy-vercel.yml` workflow will run automatically

---

## 2. Deploy Backend to Render

### Create PostgreSQL Database

1. **Go to Render Dashboard**
   - Create New → PostgreSQL
   - Name: `physicalai-db`
   - Region: Choose closest to your users
   - Plan: Free or Starter

2. **Note Connection Details**
   - Save the `Internal Database URL` for backend connection

### Deploy Backend Service

1. **Create New Web Service**
   - Create New → Web Service
   - Connect GitHub repository
   - Name: `physicalai-backend`
   - Root Directory: `backend`
   - Runtime: `Python 3.11`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`

2. **Environment Variables**
   ```bash
   DATABASE_URL=<from Render PostgreSQL>
   JWT_SECRET=<generate-secure-random-string>
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=15
   REFRESH_TOKEN_EXPIRE_DAYS=7
   CORS_ORIGINS=https://your-vercel-app.vercel.app
   ```

3. **Deploy**
   - Click "Create Web Service"
   - Render will auto-deploy on git push

4. **Run Migrations**
   ```bash
   # In Render Shell (or locally with production DB URL)
   alembic upgrade head
   python scripts/seed_roles.py
   ```

---

## 3. Deploy RAG Service to Render

### Create Qdrant Instance

**Option A: Qdrant Cloud (Recommended)**
1. Go to [Qdrant Cloud](https://cloud.qdrant.io/)
2. Create cluster
3. Note the API URL and API key

**Option B: Self-hosted on Render**
1. Create New → Private Service
2. Image: `qdrant/qdrant:latest`
3. Add persistent disk at `/qdrant/storage`

### Deploy RAG Service

1. **Create New Web Service**
   - Name: `physicalai-rag`
   - Root Directory: `rag`
   - Runtime: `Python 3.11`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`

2. **Environment Variables**
   ```bash
   QDRANT_URL=<your-qdrant-url>
   QDRANT_API_KEY=<if-using-cloud>
   CLAUDE_API_KEY=<your-anthropic-api-key>
   OLLAMA_URL=<optional-for-embeddings>
   ```

3. **Index Course Content**
   ```bash
   # Run once after deployment
   python scripts/index_chapters.py
   ```

---

## 4. Deploy Agent Service to Render

1. **Create New Web Service**
   - Name: `physicalai-agent`
   - Root Directory: `agent`
   - Runtime: `Python 3.11`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python src/main.py`

2. **Environment Variables**
   ```bash
   TRANSLATION_API_KEY=<optional-gpt4-or-seamless>
   SOURCE_CONTENT_PATH=/app/content
   ```

3. **Configure Content Access**
   - Mount persistent disk for translated content
   - Or use GitHub API to fetch/commit translations

---

## 5. Update Environment Variables

After all services are deployed, update cross-references:

### Vercel (Website)
```bash
BACKEND_API_URL=https://physicalai-backend.onrender.com
RAG_WS_URL=wss://physicalai-rag.onrender.com
```

### Render (Backend)
```bash
CORS_ORIGINS=https://your-vercel-app.vercel.app
FRONTEND_URL=https://your-vercel-app.vercel.app
```

---

## 6. Set Up Custom Domain (Optional)

### Vercel
1. Go to Project Settings → Domains
2. Add custom domain: `www.physicalai-robotics.com`
3. Configure DNS records as instructed

### Render
1. Go to Service → Settings → Custom Domain
2. Add: `api.physicalai-robotics.com`
3. Update DNS records

---

## 7. Monitoring & Logs

### Vercel
- Real-time logs in dashboard
- Analytics automatically enabled

### Render
- Logs tab shows live output
- Set up Alerts for service health

### Sentry (Recommended)
```bash
# Add to all services
pip install sentry-sdk
# Configure in src/main.py
```

---

## 8. CI/CD Pipeline

GitHub Actions automatically:
- ✅ Run tests on PRs
- ✅ Build and test website
- ✅ Deploy to Vercel on merge to master
- ✅ Trigger Render deployments

**Required GitHub Secrets:**
- `VERCEL_TOKEN` (for website deployment)
- Render auto-deploys via GitHub integration

---

## 9. Environment Variables Summary

Create a `.env.production` file locally (DON'T commit):

```bash
# Backend
DATABASE_URL=postgresql://user:pass@host:5432/db
JWT_SECRET=<64-char-random-string>

# RAG
QDRANT_URL=https://xxx.qdrant.io
QDRANT_API_KEY=xxx
CLAUDE_API_KEY=sk-ant-xxx

# Website
BACKEND_API_URL=https://physicalai-backend.onrender.com
RAG_WS_URL=wss://physicalai-rag.onrender.com
```

---

## 10. Post-Deployment Checklist

- [ ] All services are running (green status)
- [ ] Database migrations completed
- [ ] Roles seeded in database
- [ ] Course chapters indexed in Qdrant
- [ ] Website loads at Vercel URL
- [ ] Authentication works (signup/login)
- [ ] RAG chatbot responds to queries
- [ ] API endpoints return 200 (check /docs)
- [ ] CORS configured correctly
- [ ] Custom domains configured (if using)
- [ ] Monitoring/alerts set up

---

## Troubleshooting

### Backend won't start
- Check DATABASE_URL is correct
- Verify Python version is 3.11+
- Run migrations manually

### RAG returns errors
- Verify CLAUDE_API_KEY is valid
- Check Qdrant connection
- Re-run indexing script

### Website build fails
- Check Node.js version (18+)
- Clear Vercel cache and redeploy
- Verify package.json dependencies

---

## Cost Estimates (Monthly)

- **Vercel**: Free tier (Hobby)
- **Render Backend**: $7/service (3 services = $21)
- **PostgreSQL**: Free tier or $7/month
- **Qdrant Cloud**: Free 1GB or $25/month
- **Claude API**: Pay-per-use (~$0.01-0.10 per query)

**Total: ~$28-60/month** for low-to-medium traffic.

---

## Support

- **Render Docs**: https://render.com/docs
- **Vercel Docs**: https://vercel.com/docs
- **Qdrant Docs**: https://qdrant.tech/documentation/
- **Issues**: https://github.com/Farhat-Naz/newhumandiod-book/issues

---

Built with Claude Code.
