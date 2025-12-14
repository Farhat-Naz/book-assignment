# Physical AI & Humanoid Robotics Course

> Comprehensive learning platform for Physical AI, Humanoid Robotics, ROS 2, and Autonomous Systems

[![Deploy to Railway](https://railway.app/button.svg)](https://railway.app/new/template)

## 🚀 Quick Deploy

Your project is **ready to deploy**! Choose your method:

### Option 1: Railway Dashboard (Recommended)
**Easiest method - 5 minutes**

📖 **[Follow QUICK_START.md](./QUICK_START.md)**

1. Push code to GitHub
2. Connect Railway to GitHub
3. Click Deploy
4. Done! ✅

### Option 2: Automated Script
**For command-line users**

```bash
bash deploy.sh
```

### Option 3: Manual CLI
**Full control over each step**

📖 **[Follow DEPLOYMENT_COMPLETE_GUIDE.md](./DEPLOYMENT_COMPLETE_GUIDE.md)**

---

## 📚 Documentation Files

All deployment guides are included:

| File | Purpose |
|------|---------|
| [QUICK_START.md](./QUICK_START.md) | ⚡ 5-minute deployment guide |
| [DEPLOYMENT_COMPLETE_GUIDE.md](./DEPLOYMENT_COMPLETE_GUIDE.md) | 📖 Complete manual with all options |
| [DEPLOY_VIA_DASHBOARD.md](./DEPLOY_VIA_DASHBOARD.md) | 🖥️ Railway dashboard method |
| [CREATE_GITHUB_REPO.md](./CREATE_GITHUB_REPO.md) | 📦 GitHub setup instructions |
| [GITHUB_AUTH_SETUP.md](./GITHUB_AUTH_SETUP.md) | 🔐 Authentication setup |
| [RAILWAY_DEPLOYMENT.md](./RAILWAY_DEPLOYMENT.md) | 🚂 Railway-specific guide |
| [deploy.sh](./deploy.sh) | 🤖 Automated deployment script |

---

## ✅ What's Already Configured

- ✓ Railway configuration (`railway.toml`)
- ✓ Docusaurus optimized for production
- ✓ Environment detection (Railway/Vercel/GitHub Pages)
- ✓ Automatic builds and deployments
- ✓ Git repository initialized
- ✓ All dependencies installed

---

## 🏗️ Project Structure

```
website/
├── docs/                    # Course content (Markdown)
│   ├── intro.md
│   ├── module-1/           # Module 1 chapters
│   └── module-2/           # Module 2 chapters
├── blog/                   # Blog posts
├── src/                    # Custom React components
│   ├── components/
│   ├── css/
│   └── pages/
├── static/                 # Static assets (images, etc.)
├── docusaurus.config.ts   # Docusaurus configuration
├── sidebars.ts            # Sidebar navigation
├── railway.toml           # Railway deployment config
└── package.json           # Dependencies and scripts
```

---

## 💻 Local Development

```bash
# Install dependencies
npm install

# Start development server
npm start

# Build for production
npm run build

# Test production build locally
npm run serve
```

---

## 🌐 Deployment URLs

After deployment, your site will be available at:

### Railway
```
https://physical-ai-robotics-course.up.railway.app
```
(or your custom domain)

### GitHub Repository
```
https://github.com/Farhat-Naz/physical-ai-robotics-course
```

---

## 🔄 Continuous Deployment

Every push to the `main` branch automatically triggers a deployment on Railway.

```bash
# Make changes
git add .
git commit -m "Update content"
git push

# Railway automatically deploys! 🚀
```

---

## 🛠️ Technologies Used

- **[Docusaurus](https://docusaurus.io/)** - Static site generator
- **[React](https://reactjs.org/)** - UI framework
- **[Mermaid](https://mermaid-js.github.io/)** - Diagrams and flowcharts
- **[Prism](https://prismjs.com/)** - Syntax highlighting
- **[Railway](https://railway.app/)** - Hosting platform
- **Node.js 18+** - Runtime environment

---

## 📝 Course Content

### Module 1: Foundations of Physical AI & Robotics
- Chapter 1: Introduction to Physical AI
- Chapter 2: Hardware Fundamentals
- Chapter 3: Sensors & Actuators

### Module 2: ROS 2 & Autonomous Systems
- Chapter 5: ROS 2 Introduction
- More chapters coming soon...

---

## 🔧 Configuration

### Environment Variables

Railway automatically sets:
- `PORT` - Application port
- `RAILWAY_PUBLIC_DOMAIN` - Your Railway domain
- `NODE_ENV` - Production environment

### Custom Domain

To add a custom domain:
1. Go to Railway Dashboard
2. Settings → Domains
3. Add your domain
4. Configure DNS (CNAME record)

---

## 🐛 Troubleshooting

### Build Fails
```bash
# Clear cache and rebuild
npm run clear
npm run build
```

### Port Issues
Railway automatically assigns the `PORT` environment variable. The start command uses it:
```bash
npm run serve -- --host 0.0.0.0 --port $PORT
```

### Broken Links
Check `docusaurus.config.ts` for correct `baseUrl` configuration.

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/Farhat-Naz/physical-ai-robotics-course/issues)
- **Discussions:** [GitHub Discussions](https://github.com/Farhat-Naz/physical-ai-robotics-course/discussions)
- **Railway Docs:** [docs.railway.app](https://docs.railway.app/)
- **Docusaurus Docs:** [docusaurus.io](https://docusaurus.io/)

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🎉 Ready to Deploy?

**Start here:** [QUICK_START.md](./QUICK_START.md)

Your Physical AI & Robotics course is ready to go live! 🚀
