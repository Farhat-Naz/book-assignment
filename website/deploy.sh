#!/bin/bash

# Physical AI & Robotics Course - Complete Deployment Script
# This script handles GitHub and Railway deployment

set -e  # Exit on error

echo "🚀 Starting deployment process..."

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
GITHUB_USERNAME="Farhat-Naz"
REPO_NAME="physical-ai-robotics-course"
GITHUB_REPO_URL="https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"

echo -e "${BLUE}📦 Repository: ${GITHUB_REPO_URL}${NC}"

# Step 1: Check if repository exists on GitHub
echo -e "\n${YELLOW}Step 1: Checking GitHub repository...${NC}"
if git ls-remote "$GITHUB_REPO_URL" &>/dev/null; then
    echo -e "${GREEN}✓ Repository exists on GitHub${NC}"
else
    echo -e "${RED}✗ Repository does not exist yet${NC}"
    echo -e "${YELLOW}Please create the repository on GitHub:${NC}"
    echo -e "  1. Go to: https://github.com/new"
    echo -e "  2. Repository name: ${REPO_NAME}"
    echo -e "  3. Description: Physical AI & Humanoid Robotics Learning Platform"
    echo -e "  4. Set to Public"
    echo -e "  5. Do NOT initialize with README"
    echo -e "  6. Click 'Create repository'"
    echo ""
    read -p "Press Enter after creating the repository..."
fi

# Step 2: Add remote if not exists
echo -e "\n${YELLOW}Step 2: Configuring git remote...${NC}"
if git remote get-url origin &>/dev/null; then
    echo -e "${GREEN}✓ Remote 'origin' already exists${NC}"
    git remote set-url origin "$GITHUB_REPO_URL"
    echo -e "${GREEN}✓ Updated remote URL${NC}"
else
    git remote add origin "$GITHUB_REPO_URL"
    echo -e "${GREEN}✓ Added remote 'origin'${NC}"
fi

# Step 3: Push to GitHub
echo -e "\n${YELLOW}Step 3: Pushing to GitHub...${NC}"
git branch -M main
echo -e "${BLUE}Pushing to main branch...${NC}"
git push -u origin main
echo -e "${GREEN}✓ Code pushed to GitHub successfully${NC}"

# Step 4: Railway Login
echo -e "\n${YELLOW}Step 4: Railway Authentication...${NC}"
echo -e "${BLUE}Checking Railway login status...${NC}"

if railway whoami &>/dev/null; then
    echo -e "${GREEN}✓ Already logged in to Railway${NC}"
    railway whoami
else
    echo -e "${YELLOW}Please log in to Railway...${NC}"
    railway login
    echo -e "${GREEN}✓ Successfully logged in to Railway${NC}"
fi

# Step 5: Initialize Railway Project
echo -e "\n${YELLOW}Step 5: Initializing Railway project...${NC}"
if [ -f ".railway.json" ]; then
    echo -e "${GREEN}✓ Railway project already initialized${NC}"
else
    echo -e "${BLUE}Creating new Railway project...${NC}"
    railway init --name "$REPO_NAME"
    echo -e "${GREEN}✓ Railway project created${NC}"
fi

# Step 6: Link to GitHub
echo -e "\n${YELLOW}Step 6: Linking Railway to GitHub...${NC}"
echo -e "${BLUE}Note: Railway will automatically detect your GitHub repository${NC}"

# Step 7: Deploy to Railway
echo -e "\n${YELLOW}Step 7: Deploying to Railway...${NC}"
echo -e "${BLUE}Starting deployment...${NC}"
railway up
echo -e "${GREEN}✓ Deployment initiated${NC}"

# Step 8: Get deployment URL
echo -e "\n${YELLOW}Step 8: Getting deployment URL...${NC}"
sleep 5  # Wait for deployment to register
RAILWAY_URL=$(railway status --json 2>/dev/null | grep -o '"url":"[^"]*"' | cut -d'"' -f4 || echo "")

if [ -z "$RAILWAY_URL" ]; then
    echo -e "${YELLOW}⚠ URL not available yet. Check Railway dashboard:${NC}"
    railway open
else
    echo -e "${GREEN}✓ Your site is deployed at: ${RAILWAY_URL}${NC}"
fi

# Step 9: Configure domain (optional)
echo -e "\n${YELLOW}Step 9: Domain configuration...${NC}"
echo -e "${BLUE}Your Railway domain will be automatically assigned.${NC}"
echo -e "${BLUE}To add a custom domain:${NC}"
echo -e "  1. Run: railway open"
echo -e "  2. Go to Settings → Domains"
echo -e "  3. Add your custom domain"

# Summary
echo -e "\n${GREEN}═══════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ Deployment Complete!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════${NC}"
echo -e "\n${BLUE}Repository:${NC} ${GITHUB_REPO_URL}"
if [ ! -z "$RAILWAY_URL" ]; then
    echo -e "${BLUE}Live URL:${NC} ${RAILWAY_URL}"
fi
echo -e "\n${YELLOW}Useful commands:${NC}"
echo -e "  ${BLUE}railway open${NC}        - Open Railway dashboard"
echo -e "  ${BLUE}railway logs${NC}        - View deployment logs"
echo -e "  ${BLUE}railway status${NC}      - Check deployment status"
echo -e "  ${BLUE}railway up${NC}          - Redeploy"
echo -e "\n${GREEN}Done! 🎉${NC}\n"
