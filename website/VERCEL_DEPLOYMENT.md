# Vercel Deployment Guide

This guide will help you deploy the Physical AI & Humanoid Robotics Course website to Vercel.

## Prerequisites

- GitHub account with repository access
- Vercel account (free tier is sufficient)

## Automatic Deployment (Recommended)

### Step 1: Import Project to Vercel

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **"Add New Project"** or **"Import Project"**
3. Select **"Import Git Repository"**
4. Authorize Vercel to access your GitHub account if not already done
5. Select the repository: `Farhat-Naz/newhumandiod-book`

### Step 2: Configure Project

Vercel will auto-detect Docusaurus. Verify the following settings:

**Framework Preset**: Docusaurus (auto-detected)

**Root Directory**: `website`
- Click **"Edit"** next to Root Directory
- Enter: `website`
- This tells Vercel the Docusaurus project is in the website folder

**Build Command**: `npm run build` (auto-filled)

**Output Directory**: `build` (auto-filled)

**Install Command**: `npm install` (auto-filled)

**Node.js Version**: 18.x or higher (set in Environment Variables if needed)

### Step 3: Environment Variables (Optional)

If you need custom environment variables:

1. Click **"Environment Variables"**
2. Add any required variables (currently none are needed)

### Step 4: Deploy

1. Click **"Deploy"**
2. Vercel will:
   - Clone your repository
   - Install dependencies
   - Build the Docusaurus site
   - Deploy to their CDN

**Deployment time**: ~2-5 minutes

### Step 5: Get Your URL

After successful deployment:

1. You'll see: **"Congratulations! Your project has been deployed."**
2. Your site URL will be: `https://[project-name].vercel.app`
3. Example: `https://newhumandiod-book.vercel.app`

## Automatic Updates

Vercel automatically deploys when you push to GitHub:

- **Production**: Pushes to `master` branch
- **Preview**: Pushes to other branches or pull requests

Every commit triggers a new deployment with a unique preview URL.

## Configuration Files

### vercel.json

Already configured with:
- Build command and output directory
- Static file caching (1 year for immutable assets)
- Security headers (XSS, frame options, content type)
- SPA routing rewrites

### .vercelignore

Excludes unnecessary files:
- `node_modules/`
- `.docusaurus/`
- Build artifacts
- Environment files
- IDE configs

## Custom Domain (Optional)

To use a custom domain:

1. Go to your project in Vercel Dashboard
2. Click **"Settings"** → **"Domains"**
3. Click **"Add Domain"**
4. Enter your domain: `yourdomain.com`
5. Follow DNS configuration instructions
6. Vercel provides automatic HTTPS

## Troubleshooting

### Build Fails

**Check build logs**:
1. Go to Vercel Dashboard → Your Project
2. Click on the failed deployment
3. View **"Building"** logs

**Common issues**:
- **Node version**: Ensure Node.js ≥18 in project settings
- **Dependencies**: Check if all packages install correctly
- **Build command**: Verify `npm run build` works locally

### Deployment Success but Site Broken

1. Check **"Output"** directory is set to `build`
2. Verify **Root Directory** is set to `website`
3. Check browser console for errors
4. Ensure all assets loaded from correct paths

### Chapter 4 Not Showing

1. Verify file exists: `website/docs/module-1/chapter-4-motion-planning.md`
2. Check sidebar configuration in `website/sidebars.ts`
3. Clear Docusaurus cache: `npm run clear`
4. Rebuild: `npm run build`
5. Redeploy from Vercel Dashboard

## Verification

After deployment, verify:

1. ✅ Homepage loads: `https://[your-url].vercel.app/`
2. ✅ Docs accessible: `https://[your-url].vercel.app/docs/intro`
3. ✅ Chapter 4 visible: `https://[your-url].vercel.app/docs/module-1/chapter-4-motion-planning`
4. ✅ All navigation links work
5. ✅ Search functionality works
6. ✅ Mermaid diagrams render

## Manual Deployment (Alternative)

If you prefer manual deployment:

```bash
# Install Vercel CLI
npm install -g vercel

# Navigate to website directory
cd website

# Login to Vercel
vercel login

# Deploy to production
vercel --prod
```

## Deployment Status

Check deployment status:

1. **Vercel Dashboard**: Real-time build logs
2. **GitHub**: Vercel bot comments on commits
3. **CLI**: `vercel inspect [deployment-url]`

## Rollback

To rollback to a previous deployment:

1. Go to Vercel Dashboard → Your Project
2. Click **"Deployments"**
3. Find the working deployment
4. Click **⋯** → **"Promote to Production"**

## Performance

Vercel provides:
- **Global CDN**: Fast loading worldwide
- **Edge caching**: Static assets cached at edge
- **Automatic compression**: Gzip/Brotli
- **HTTP/2**: Faster multiplexed connections
- **Smart builds**: Only rebuilds changed files

## Support

- [Vercel Documentation](https://vercel.com/docs)
- [Docusaurus Deployment Guide](https://docusaurus.io/docs/deployment#deploying-to-vercel)
- [Vercel Support](https://vercel.com/support)

## Next Steps

1. ✅ Deploy to Vercel
2. ✅ Verify Chapter 4 is accessible
3. ✅ Share the Vercel URL
4. Consider adding custom domain
5. Set up analytics (optional)
6. Configure web vitals monitoring

---

**Last Updated**: 2025-12-14
**Deployment Platform**: Vercel
**Framework**: Docusaurus 3.0.1
**Node.js**: ≥18.0
