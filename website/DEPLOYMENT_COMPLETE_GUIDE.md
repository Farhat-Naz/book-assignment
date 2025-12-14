# Complete Deployment Guide

This guide provides a complete, step-by-step process to deploy your Physical AI & Robotics course to Railway.

## Prerequisites Installed ✓

- [x] Node.js 18+
- [x] Git
- [x] Railway CLI
- [x] Git repository initialized

## Quick Start (Automated)

### Option 1: One-Command Deployment (Windows)

```bash
cd book-assignment/website
bash deploy.sh
```

### Option 2: Manual Step-by-Step

Follow the steps below for complete control over the deployment process.

---

## Step-by-Step Manual Deployment

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in the details:
   - **Repository name:** `physical-ai-robotics-course`
   - **Description:** `Physical AI & Humanoid Robotics Learning Platform - Documentation and Course Materials`
   - **Visibility:** Public
   - **DO NOT** check "Initialize with README"
3. Click "Create repository"

### Step 2: Push Code to GitHub

Open your terminal and run:

```bash
cd "D:\quarterr 4\new-book\book-assignment\website"

# Add GitHub remote
git remote add origin https://github.com/Farhat-Naz/physical-ai-robotics-course.git

# Rename branch to main
git branch -M main

# Push code
git push -u origin main
```

**Expected output:**
```
Enumerating objects: 50, done.
Counting objects: 100% (50/50), done.
...
To https://github.com/Farhat-Naz/physical-ai-robotics-course.git
 * [new branch]      main -> main
```

### Step 3: Login to Railway

```bash
railway login
```

This will:
- Open your browser
- Ask you to authorize Railway CLI
- Automatically log you in

**Expected output:**
```
🎉 Logged in as Farhat-Naz (you@email.com)
```

### Step 4: Initialize Railway Project

```bash
cd "D:\quarterr 4\new-book\book-assignment\website"
railway init
```

When prompted:
- **Project name:** `physical-ai-robotics-course` (or press Enter for default)
- **Start with:** Empty project

**Expected output:**
```
✓ Created project physical-ai-robotics-course
✓ Linked to project physical-ai-robotics-course
```

### Step 5: Deploy to Railway

```bash
railway up
```

This will:
- Upload your code
- Detect the `railway.toml` configuration
- Build your Docusaurus site
- Deploy it

**Expected output:**
```
=== Uploading 50 files
=== Building...
=== Build completed
=== Deploying...
✓ Deployment live at https://physical-ai-robotics-course-production.up.railway.app
```

### Step 6: Get Your Deployment URL

```bash
railway status
```

Or open the Railway dashboard:

```bash
railway open
```

---

## Alternative: Deploy via Railway Dashboard

If you prefer using the web interface:

### Step 1: Push to GitHub

```bash
cd "D:\quarterr 4\new-book\book-assignment\website"
git remote add origin https://github.com/Farhat-Naz/physical-ai-robotics-course.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Railway

1. Go to https://railway.app/new
2. Click "Deploy from GitHub repo"
3. Select `Farhat-Naz/physical-ai-robotics-course`
4. Railway will automatically:
   - Detect `railway.toml`
   - Configure build settings
   - Deploy your site

### Step 3: Configure Settings (if needed)

Railway should auto-configure everything, but verify:

- **Build Command:** `npm run build`
- **Start Command:** `npm run serve -- --host 0.0.0.0 --port $PORT`
- **Environment Variables:** All set automatically

---

## Environment Variables

Railway automatically provides:

| Variable | Description | Auto-Set |
|----------|-------------|----------|
| `PORT` | Application port | ✓ |
| `RAILWAY_PUBLIC_DOMAIN` | Your Railway domain | ✓ |
| `NODE_ENV` | Environment (production) | ✓ |

Your `docusaurus.config.ts` is already configured to use these.

---

## Custom Domain Setup

### Step 1: Add Domain in Railway

1. Open Railway dashboard: `railway open`
2. Go to **Settings** → **Domains**
3. Click **Add Domain**
4. Enter your domain (e.g., `docs.yourdomain.com`)

### Step 2: Configure DNS

Add these records to your DNS provider:

**For subdomain (docs.yourdomain.com):**
```
Type: CNAME
Name: docs
Value: <your-railway-domain>.up.railway.app
```

**For root domain (yourdomain.com):**
```
Type: A
Name: @
Value: <Railway IP - shown in dashboard>
```

### Step 3: Verify

- SSL certificate is automatically provisioned
- Domain will be active within 5-10 minutes

---

## Useful Railway Commands

```bash
# View deployment logs
railway logs

# Check deployment status
railway status

# Redeploy
railway up

# Open Railway dashboard
railway open

# View environment variables
railway variables

# Add environment variable
railway variables set KEY=value

# Link to different project
railway link

# View project info
railway whoami
```

---

## Continuous Deployment

### Enable Automatic Deployments

Railway can automatically deploy when you push to GitHub:

1. In Railway dashboard, go to **Settings**
2. Under **Deployment**, enable **Auto Deploy**
3. Select branch: `main`

Now, every push to `main` triggers a deployment:

```bash
# Make changes
git add .
git commit -m "Update documentation"
git push

# Railway automatically deploys! 🚀
```

---

## Monitoring & Logs

### View Live Logs

```bash
railway logs --follow
```

### Check Build Logs

1. Run `railway open`
2. Click on your deployment
3. View **Build Logs** and **Deploy Logs**

### Monitor Metrics

Railway dashboard shows:
- CPU usage
- Memory usage
- Network traffic
- Request count

---

## Troubleshooting

### Build Fails

**Error:** `npm install failed`
```bash
# Clear Railway cache
railway down
railway up
```

**Error:** `Port binding failed`
- Verify `railway.toml` has correct start command
- Ensure using `$PORT` environment variable

### Site Not Loading

1. Check deployment status:
   ```bash
   railway status
   ```

2. View logs:
   ```bash
   railway logs
   ```

3. Verify build completed:
   ```bash
   railway open
   # Check deployment status in dashboard
   ```

### Custom Domain Not Working

1. Verify DNS records:
   ```bash
   nslookup yourdomain.com
   ```

2. Wait 5-10 minutes for DNS propagation

3. Check Railway dashboard for SSL status

---

## Cost Estimation

Railway Pricing:
- **Hobby Plan:** $5/month + usage
- **Pay-as-you-go** for resources

Estimated cost for this static site:
- **~$1-3/month** (very light usage)
- **Free trial:** $5 credit to start

---

## Next Steps After Deployment

1. ✓ Push code to GitHub
2. ✓ Deploy to Railway
3. [ ] Add custom domain
4. [ ] Set up automatic deployments
5. [ ] Monitor site performance
6. [ ] Share your deployed URL!

---

## Support & Resources

- **Railway Docs:** https://docs.railway.app/
- **Docusaurus Docs:** https://docusaurus.io/
- **GitHub Repository:** https://github.com/Farhat-Naz/physical-ai-robotics-course
- **Issues:** https://github.com/Farhat-Naz/physical-ai-robotics-course/issues

---

## Quick Reference

| Task | Command |
|------|---------|
| Deploy | `railway up` |
| View logs | `railway logs` |
| Open dashboard | `railway open` |
| Check status | `railway status` |
| Redeploy | `railway up` |
| View variables | `railway variables` |

---

**Ready to deploy?** Run `bash deploy.sh` or follow the manual steps above! 🚀
