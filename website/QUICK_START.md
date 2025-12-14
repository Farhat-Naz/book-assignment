# 🚀 Quick Start - Deploy to Railway in 5 Minutes

## ✅ What's Already Done

- ✓ Project built and tested locally
- ✓ Git repository initialized
- ✓ Railway configuration (`railway.toml`) created
- ✓ Docusaurus config updated for Railway

## 📋 What You Need

Just two things:
1. A GitHub account (you have: Farhat-Naz)
2. A Railway account (will create with GitHub)

---

## 🎯 Step 1: Push to GitHub (2 minutes)

### Option A: Using GitHub Desktop (Easiest)

1. Download: https://desktop.github.com/
2. Open GitHub Desktop
3. File → Add Local Repository
4. Choose: `D:\quarterr 4\new-book\book-assignment\website`
5. Click "Publish repository"
   - Name: `physical-ai-robotics-course`
   - ✓ Keep unchecked "Keep this code private"
6. Click "Publish repository"

### Option B: Using Personal Access Token

1. **Create token:** https://github.com/settings/tokens/new
   - Note: `Railway Deploy`
   - Expiration: `90 days`
   - Check: `repo`
   - Click "Generate token"
   - **COPY the token!**

2. **Push to GitHub:**
   ```bash
   cd "D:\quarterr 4\new-book\book-assignment\website"
   git push -u origin main
   ```

   When prompted:
   - Username: `Farhat-Naz`
   - Password: [paste token]

3. **Verify:** Visit https://github.com/Farhat-Naz/physical-ai-robotics-course

---

## 🚂 Step 2: Deploy on Railway (3 minutes)

### 2.1 Create Railway Account

1. Go to: **https://railway.app/**
2. Click: **"Login with GitHub"**
3. Authorize Railway
4. ✓ You're logged in!

### 2.2 Create New Project

1. Click: **"New Project"** (big button in center)
2. Select: **"Deploy from GitHub repo"**

### 2.3 Connect GitHub

First time? You'll see:
1. **"Configure GitHub App"**
2. Click it
3. Select: **"Only select repositories"**
4. Choose: **`physical-ai-robotics-course`**
5. Click: **"Install & Authorize"**

### 2.4 Deploy!

1. Back in Railway, select: **`Farhat-Naz/physical-ai-robotics-course`**
2. Click: **"Add variables"** (optional, skip for now)
3. Click: **"Deploy"**

### 2.5 Watch the Magic ✨

You'll see:
- ⏳ **Initializing...** (10 seconds)
- 📦 **Building...** (1-2 minutes)
  - Running `npm install`
  - Running `npm run build`
- 🚀 **Deploying...** (30 seconds)
- ✅ **Active!** (Your site is live!)

---

## 🌐 Step 3: Get Your Live URL

1. In Railway dashboard, click your deployment
2. Look for **"Deployments"** tab
3. Click the **live deployment** (green checkmark)
4. You'll see: **"your-project.up.railway.app"**
5. Click it or copy the URL

**Your site is now live! 🎉**

---

## 📝 Quick Reference

### Your Repository
```
https://github.com/Farhat-Naz/physical-ai-robotics-course
```

### Railway Dashboard
```
https://railway.app/dashboard
```

### After Changes
```bash
git add .
git commit -m "Your changes"
git push
# Railway auto-deploys! 🚀
```

---

## 🔧 Optional: Add Custom Domain

In Railway Dashboard:
1. Click your project
2. Go to: **Settings → Domains**
3. Click: **"Add Domain"**
4. Enter: `docs.yourdomain.com`
5. Update your DNS:
   ```
   Type: CNAME
   Name: docs
   Value: your-project.up.railway.app
   ```

---

## 🆘 Need Help?

**GitHub push not working?**
- Use GitHub Desktop (easiest)
- Or create Personal Access Token

**Railway not building?**
- Check if `railway.toml` exists
- View build logs in Railway dashboard
- Ensure `package.json` has correct scripts

**Site not loading?**
- Wait 2-3 minutes for first deployment
- Check deployment status (should be green)
- View logs in Railway dashboard

---

## 📊 What's Next?

- ✓ Your site is live!
- [ ] Share your URL
- [ ] Set up custom domain
- [ ] Add automatic deployments (already working!)
- [ ] Monitor site metrics in Railway

---

## 🎉 Done!

Your **Physical AI & Robotics Course** is now live on Railway!

Any push to GitHub `main` branch will automatically deploy. No manual intervention needed!
