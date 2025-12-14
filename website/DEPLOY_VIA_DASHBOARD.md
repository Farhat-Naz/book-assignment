# Deploy via Railway Dashboard (Recommended)

This is the easiest method - no command line authentication needed!

## Step 1: Push Code to GitHub (One-Time Auth)

Open Git Bash or Terminal and run:

```bash
cd "D:\quarterr 4\new-book\book-assignment\website"
git push -u origin main
```

When prompted for credentials:
- **Username:** Farhat-Naz
- **Password:** Use a Personal Access Token (see below)

### Create Personal Access Token (30 seconds):

1. Go to: https://github.com/settings/tokens/new
2. **Note:** `Railway Deployment`
3. **Expiration:** 90 days
4. **Check:** `repo` (Full control)
5. Click **"Generate token"**
6. **Copy the token** (looks like: `ghp_xxxxxxxxxxxx`)

Use this token as your password when pushing.

---

## Step 2: Deploy on Railway Dashboard

### 2a. Go to Railway

Visit: https://railway.app/new

### 2b. Login/Signup

- Click **"Login with GitHub"**
- Authorize Railway to access your GitHub

### 2c. Create New Project

1. Click **"Deploy from GitHub repo"**
2. You'll see: **"Configure GitHub App"**
3. Click **"Configure GitHub App"**
4. Select **"Only select repositories"**
5. Choose: `physical-ai-robotics-course`
6. Click **"Install & Authorize"**

### 2d. Select Repository

1. Back in Railway, click **"Deploy from GitHub repo"** again
2. Select: **`Farhat-Naz/physical-ai-robotics-course`**
3. Click **"Deploy Now"**

### 2e. Automatic Configuration

Railway will automatically:
- ✓ Detect `railway.toml`
- ✓ Set Node.js environment
- ✓ Run `npm run build`
- ✓ Start with `npm run serve`
- ✓ Assign a public URL

---

## Step 3: Wait for Deployment (2-3 minutes)

You'll see:
1. **Building...** (npm install, npm run build)
2. **Deploying...** (starting server)
3. **Active** (live and running!)

---

## Step 4: Get Your URL

Once deployed:
1. Click on your deployment
2. Go to **"Settings"** → **"Domains"**
3. You'll see: `your-project.up.railway.app`
4. Click to open your live site! 🎉

---

## Step 5: Set Up Automatic Deployments

Now, every time you push to GitHub, Railway auto-deploys!

```bash
# Make changes
git add .
git commit -m "Update content"
git push

# Railway automatically deploys! 🚀
```

---

## Troubleshooting

### Can't push to GitHub?

**Quick fix - Try SSH:**

```bash
# Change to SSH
cd "D:\quarterr 4\new-book\book-assignment\website"
git remote set-url origin git@github.com:Farhat-Naz/physical-ai-robotics-course.git
git push -u origin main
```

### Railway can't find repository?

1. Make sure repository exists: https://github.com/Farhat-Naz/physical-ai-robotics-course
2. Repository must be public OR Railway must have access
3. Reinstall GitHub App in Railway settings

### Build fails?

Check Railway logs:
1. Click on your project
2. View **"Deployments"**
3. Click on failed deployment
4. Check **"Build Logs"**

---

## All Done! 🎉

Your site should now be live at:
```
https://your-project-name.up.railway.app
```

**Next steps:**
- Add custom domain (Settings → Domains)
- Configure environment variables (Settings → Variables)
- Monitor deployment (View logs and metrics)
