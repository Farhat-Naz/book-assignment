# Deployment Instructions

## Quick Deploy to Vercel

1. **Push to GitHub** (completed)
   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/Book-Assignment.git
   git branch -M main
   git push -u origin main
   ```

2. **Deploy to Vercel**
   - Go to: https://vercel.com/new
   - Sign in with GitHub
   - Import your `Book-Assignment` repository
   - **Framework Preset**: Docusaurus
   - **Root Directory**: `humaniod-robotics`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`
   - Click "Deploy"

3. **Vercel will automatically**:
   - Install dependencies
   - Build the site
   - Deploy to a production URL
   - Set up automatic deployments on git push

## Manual GitHub Pages Deploy (Alternative)

If you prefer GitHub Pages instead of Vercel:

1. Update `docusaurus.config.ts`:
   ```typescript
   url: 'https://YOUR-USERNAME.github.io',
   baseUrl: '/Book-Assignment/',
   organizationName: 'YOUR-USERNAME',
   projectName: 'Book-Assignment',
   ```

2. Deploy:
   ```bash
   cd humaniod-robotics
   GIT_USER=YOUR-USERNAME npm run deploy
   ```

## Environment Variables (if needed later)

For future features that need environment variables:

- Create `.env.local` (already gitignored)
- Add to Vercel dashboard under Settings → Environment Variables

## Custom Domain (Optional)

1. In Vercel dashboard: Settings → Domains
2. Add your custom domain
3. Update DNS records as instructed
4. Vercel will automatically provision SSL certificate

## Automatic Deployments

Vercel will automatically deploy:
- **Production**: Every push to `main` branch
- **Preview**: Every pull request

## Build Performance

Current build time: ~25 seconds
Site size: ~2MB (before content)

## Monitoring

- Vercel provides analytics automatically
- View deployment logs in Vercel dashboard
- Set up alerts for build failures
