# GitHub Authentication Setup

Git needs authentication to push to your repository. Choose one of these methods:

## Method 1: GitHub Personal Access Token (Recommended for Windows)

### Step 1: Create a Personal Access Token

1. Go to: https://github.com/settings/tokens/new
2. **Note:** `Railway Deployment Token`
3. **Expiration:** 90 days (or custom)
4. **Select scopes:**
   - ✓ `repo` (Full control of private repositories)
   - ✓ `workflow` (if using GitHub Actions)

5. Click **"Generate token"**
6. **COPY THE TOKEN** - you won't see it again!

### Step 2: Use Token When Pushing

When Git asks for credentials:
- **Username:** `Farhat-Naz`
- **Password:** paste your token

## Method 2: Use SSH (Alternative)

### Step 1: Generate SSH Key (if you don't have one)

```bash
ssh-keygen -t ed25519 -C "asfiqbl177@gmail.com"
```

Press Enter for all prompts to use defaults.

### Step 2: Add SSH Key to GitHub

```bash
# Copy your public key
cat ~/.ssh/id_ed25519.pub
```

1. Go to: https://github.com/settings/ssh/new
2. **Title:** `Windows PC`
3. **Key:** Paste the key from above
4. Click **"Add SSH key"**

### Step 3: Change Remote to SSH

```bash
cd "book-assignment/website"
git remote set-url origin git@github.com:Farhat-Naz/physical-ai-robotics-course.git
```

---

## Quick Fix: Let's Try Again

After setting up authentication above, run:

```bash
cd "D:\quarterr 4\new-book\book-assignment\website"
git push -u origin main
```

---

## Still Having Issues?

Make sure:
1. Repository exists at: https://github.com/Farhat-Naz/physical-ai-robotics-course
2. You're logged into GitHub with username: `Farhat-Naz`
3. Repository is not private (or you have access)
