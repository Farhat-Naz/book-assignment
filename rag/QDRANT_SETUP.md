# Qdrant Cloud Setup Guide

Complete step-by-step guide to set up Qdrant Cloud for your RAG chatbot.

## Step 1: Create Qdrant Cloud Account

1. **Go to Qdrant Cloud**:
   - Open: https://cloud.qdrant.io/

2. **Sign Up** (Free):
   - Click "Sign Up" or "Get Started"
   - Use Google, GitHub, or Email
   - No credit card required for free tier!

## Step 2: Create a Free Cluster

1. **After login, click "Create Cluster"**

2. **Choose Free Tier**:
   - Cluster Name: `rag-chatbot` (or your choice)
   - Cloud Provider: Any (AWS/GCP/Azure)
   - Region: Choose closest to you
   - Plan: **Free 1GB** (select this!)

3. **Click "Create"**
   - Wait 1-2 minutes for provisioning
   - Status will change to "Running"

## Step 3: Get Your Credentials

1. **Open your cluster** (click on cluster name)

2. **Copy these values**:

   **Cluster URL** (looks like):
   ```
   https://abc123-example-xyz.aws.cloud.qdrant.io:6333
   ```

   **API Key**:
   - Click "API Keys" tab
   - Click "Generate API Key"
   - Copy the key (starts with `pk-` or similar)
   - **SAVE IT!** You can't see it again

## Step 4: Update Your .env File

Open `D:\quarterr 4\new-book\book-assignment\rag\.env` and update:

```bash
# Qdrant Configuration - UPDATE THESE!
QDRANT_HOST=https://your-cluster-xyz.aws.cloud.qdrant.io:6333
QDRANT_API_KEY=pk-your-actual-api-key-here
QDRANT_COLLECTION_NAME=course_chapters
QDRANT_VECTOR_SIZE=384
```

**Important**:
- Replace `your-cluster-xyz` with your actual cluster URL
- Replace `pk-your-actual-api-key-here` with your actual API key
- Keep the port number (usually :6333)

## Step 5: Restart the Server

1. **Stop the current server**:
   - Press CTRL+C in the terminal where uvicorn is running
   - Or close the terminal

2. **Start fresh**:
   ```bash
   cd "D:\quarterr 4\new-book\book-assignment\rag"
   uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
   ```

3. **Watch the logs**:
   - Should see: "Qdrant Cloud client initialized"
   - Should see: "Loaded 12 documents"
   - Should see: "Inserted 148 vectors into Qdrant"

## Step 6: Verify in Qdrant Dashboard

1. **Go back to Qdrant Cloud dashboard**:
   - https://cloud.qdrant.io/

2. **Click on your cluster**

3. **Navigate to "Collections"**:
   - You should see `course_chapters`
   - Click on it

4. **Verify data**:
   - Points: 148
   - Vector size: 384
   - Status: Green

5. **Browse vectors** (optional):
   - Click "Console" tab
   - Run queries to see your data

## Troubleshooting

### Connection Errors

If you see connection errors:

1. **Check URL format**:
   ```bash
   # Correct formats:
   https://xyz.aws.cloud.qdrant.io:6333
   https://xyz.gcp.cloud.qdrant.io:6333

   # Include the port number!
   ```

2. **Check API key**:
   - No spaces before/after
   - Full key copied
   - Not expired

3. **Check firewall**:
   - Qdrant uses port 6333
   - Make sure it's not blocked

### "Collection already exists" Error

This is normal! The code handles this automatically.

### Still using mock?

Check the logs for:
```
"Using in-memory mock Qdrant (placeholder credentials detected)"
```

If you see this, your credentials aren't being read correctly:
- Check .env file location
- Restart the server
- Verify no typos in QDRANT_HOST and QDRANT_API_KEY

## Free Tier Limits

Qdrant Free Tier includes:
- **1 GB storage**
- **1 cluster**
- **Unlimited API calls**
- **Public internet access**

This is plenty for:
- 148 current documents
- Thousands more documents
- Development and testing

## Security Best Practices

1. **Never commit `.env` to Git**:
   - Already in `.gitignore`
   - Keep API keys secret!

2. **Rotate keys periodically**:
   - Generate new key in dashboard
   - Update .env
   - Delete old key

3. **Use different keys for dev/prod**:
   - Create separate clusters
   - Different API keys

## Testing After Setup

Run the test suite:

```bash
# Check documents loaded
curl http://localhost:8000/api/v1/documents/info

# Test chat
python test_chat.py

# Interactive mode
python test_chat.py interactive
```

Expected output:
```json
{
  "name": "course_chapters",
  "vectors_count": 148,
  "points_count": 148,
  "status": "green"
}
```

## Next Steps

Once Qdrant is working:

1. **Add Claude API key** for full chatbot functionality
2. **Test vector search** in Qdrant dashboard
3. **Add more documents** if needed
4. **Monitor usage** in dashboard

## Need Help?

- **Qdrant Docs**: https://qdrant.tech/documentation/
- **Qdrant Discord**: https://qdrant.to/discord
- **API Reference**: https://qdrant.tech/documentation/api-reference/

---

**Current Status**: Using in-memory mock (placeholder credentials)
**Target**: Connect to Qdrant Cloud cluster
**Impact**: Documents will persist across server restarts and be visible in dashboard
