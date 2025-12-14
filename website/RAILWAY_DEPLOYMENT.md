# Railway Deployment Guide

This guide will help you deploy the Physical AI & Humanoid Robotics documentation site to Railway.

## Prerequisites

1. A [Railway account](https://railway.app/) (sign up with GitHub)
2. [Railway CLI](https://docs.railway.app/develop/cli) (optional, but recommended)
3. Git installed on your machine
4. Node.js 18+ installed

## Deployment Steps

### Option 1: Deploy via Railway Dashboard (Easiest)

1. **Push your code to GitHub:**
   ```bash
   cd book-assignment/website
   git add .
   git commit -m "Initial commit - ready for Railway deployment"
   ```

   Then create a new repository on GitHub and push:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git branch -M main
   git push -u origin main
   ```

2. **Deploy on Railway:**
   - Go to [railway.app](https://railway.app/)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect the configuration from `railway.toml`

3. **Configure Environment Variables:**
   - Once deployed, go to your project settings
   - The `RAILWAY_PUBLIC_DOMAIN` will be automatically set
   - Your site will be available at `https://your-project.up.railway.app`

4. **Custom Domain (Optional):**
   - Go to Settings → Domains
   - Add your custom domain
   - Follow the DNS configuration instructions

### Option 2: Deploy via Railway CLI

1. **Install Railway CLI:**
   ```bash
   npm i -g @railway/cli
   ```

2. **Login to Railway:**
   ```bash
   railway login
   ```

3. **Initialize and Deploy:**
   ```bash
   cd book-assignment/website
   git add .
   git commit -m "Initial commit"
   railway init
   railway up
   ```

4. **Open your deployment:**
   ```bash
   railway open
   ```

## Configuration Files

The following files have been created/modified for Railway deployment:

1. **railway.toml** - Railway configuration
   - Specifies build and start commands
   - Configures the PORT variable

2. **docusaurus.config.ts** - Updated to support Railway
   - Automatically detects `RAILWAY_PUBLIC_DOMAIN`
   - Sets correct base URL for deployment

3. **.gitignore** - Prevents committing build artifacts and dependencies

## Local Testing

Test the production build locally before deploying:

```bash
npm run build
npm run serve
```

Visit http://localhost:3000 to verify everything works.

## Troubleshooting

### Build fails on Railway
- Check the build logs in Railway dashboard
- Ensure all dependencies are in `package.json`
- Verify Node.js version matches `engines` field in package.json

### Site doesn't load
- Check if the PORT environment variable is set correctly
- Verify the start command in railway.toml
- Check Railway logs for errors

### Broken links warnings
- These are warnings about some internal links in the documentation
- They won't prevent deployment but should be fixed for better UX
- Check the footer links in `docusaurus.config.ts`

## Environment Variables

Railway automatically provides:
- `PORT` - The port your app should listen on
- `RAILWAY_PUBLIC_DOMAIN` - Your Railway domain (used in docusaurus.config.ts)
- `NODE_ENV` - Set to "production" automatically

## Costs

Railway offers:
- Free trial with $5 credit
- Hobby plan: $5/month + usage
- Pay-as-you-go for resources used

A static Docusaurus site typically costs $1-3/month.

## Next Steps

After deployment:
1. Set up automatic deployments from GitHub
2. Configure a custom domain
3. Enable Railway's built-in SSL (automatic)
4. Monitor your deployment in the Railway dashboard

## Support

- [Railway Documentation](https://docs.railway.app/)
- [Docusaurus Documentation](https://docusaurus.io/)
- [GitHub Issues](https://github.com/physicalai/book-assignment/issues)
