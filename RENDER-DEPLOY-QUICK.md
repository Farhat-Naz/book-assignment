# 🚀 Quick Render Deployment Guide

This guide will help you deploy all backend services (Backend API, RAG Service, Agent Service) to Render in one go.

## Prerequisites
- Render account (sign up at https://render.com)
- GitHub repository connected

---

## Step 1: Go to Render Dashboard

1. Open: **https://dashboard.render.com/**
2. Click **"New"** → **"Blueprint"**

---

## Step 2: Connect Your Repository

1. Select **"Connect a repository"**
2. Choose: **`Farhat-Naz/newhumandiod-book`**
3. Render will detect the `render.yaml` file automatically
4. Click **"Apply"**

---

## Step 3: Configure Environment Variables

Render will prompt you to fill in environment variables marked with `sync: false`.

### 📋 Copy and paste these values:

#### **For Service: `physicalai-rag`**

**Copy these values from `.env.production` file:**

```bash
QDRANT_URL=<your-qdrant-url-from-env-production>

QDRANT_API_KEY=<your-qdrant-api-key-from-env-production>

CLAUDE_API_KEY=<your-claude-api-key-from-env-production>
```

**Find these values in your local `.env.production` file (lines 24-26 and line 10)**

#### **For Service: `physicalai-backend`**

```bash
CORS_ORIGINS=https://book-assignment-bqy4ulakm-farhats-projects-27800a4d.vercel.app
```

#### **For Service: `physicalai-agent`**

```bash
TRANSLATION_API_KEY=
```
*(Leave empty for now - translation will be added later)*

---

## Step 4: Deploy

1. Click **"Apply"** or **"Create Blueprint"**
2. Render will start deploying all 3 services:
   - ✅ `physicalai-backend` (Authentication & API)
   - ✅ `physicalai-rag` (RAG Chatbot)
   - ✅ `physicalai-agent` (Translation Agent)

3. **Wait 5-10 minutes** for the first deployment to complete

---

## Step 5: Get Your Service URLs

Once deployed, Render will give you URLs like:
- Backend: `https://physicalai-backend.onrender.com`
- RAG: `https://physicalai-rag.onrender.com`
- Agent: `https://physicalai-agent.onrender.com`

**Note these URLs down!** You'll need them for the next step.

---

## Step 6: Update Vercel Environment Variables

After Render deployment completes, run this command to update your Vercel website:

```bash
# Set backend URL in Vercel
vercel env add BACKEND_API_URL production
# Paste: https://physicalai-backend.onrender.com

# Set RAG WebSocket URL
vercel env add RAG_WS_URL production
# Paste: wss://physicalai-rag.onrender.com
```

Or update via Vercel Dashboard:
1. Go to: https://vercel.com/farhats-projects-27800a4d/book-assignment/settings/environment-variables
2. Add these variables for **Production**:
   - `BACKEND_API_URL` = `https://physicalai-backend.onrender.com`
   - `RAG_WS_URL` = `wss://physicalai-rag.onrender.com`
3. **Redeploy** the Vercel site

---

## Step 7: Run Database Migrations

After the backend is deployed, you need to initialize the database:

1. Go to Render Dashboard → `physicalai-backend` service
2. Click **"Shell"** tab
3. Run these commands:

```bash
# Run migrations
alembic upgrade head

# Seed roles
python scripts/seed_roles.py
```

---

## Step 8: Index Content for RAG

For the RAG chatbot to work, index the course content:

1. Go to Render Dashboard → `physicalai-rag` service
2. Click **"Shell"** tab
3. Run:

```bash
# Index all chapters (if script exists)
python scripts/index_chapters.py
```

---

## ✅ Verification Checklist

- [ ] All 3 Render services show "Live" status (green)
- [ ] Backend API responds at: `https://physicalai-backend.onrender.com/docs`
- [ ] RAG service responds at: `https://physicalai-rag.onrender.com/docs`
- [ ] Database migrations completed
- [ ] Roles seeded in database
- [ ] Vercel environment variables updated
- [ ] Vercel site redeployed

---

## 🎯 Test Your Deployment

1. **Visit your site**: https://book-assignment-bqy4ulakm-farhats-projects-27800a4d.vercel.app
2. **Test Authentication**: Try to sign up/login
3. **Test RAG Chatbot**: Ask a question about the course
4. **Test Translation**: Switch languages

---

## 🐛 Troubleshooting

### Backend won't start
- Check DATABASE_URL is set correctly
- Check logs in Render dashboard

### RAG returns errors
- Verify CLAUDE_API_KEY is valid
- Check QDRANT_URL is accessible
- Ensure content is indexed

### CORS errors
- Make sure CORS_ORIGINS in backend matches your Vercel URL exactly

---

## 📞 Need Help?

- Check Render logs for each service
- Verify all environment variables are set
- Ensure services are on the free tier (may have cold starts)

---

Built with Claude Code 🤖
