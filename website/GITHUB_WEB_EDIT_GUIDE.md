# GitHub Web Edit Guide - Fix Deployment Step by Step

Follow these exact steps to fix your deployment issues directly on GitHub.

---

## 📝 Part 1: Edit docusaurus.config.ts (3 changes needed)

### Step 1.1: Open the file

1. Open your browser
2. Go to: **https://github.com/Farhat-Naz/physical-ai-robotics-course**
3. You should see a list of files
4. **Click on:** `docusaurus.config.ts` (in the file list)
5. The file will open and show code

### Step 1.2: Start editing

1. Look at the top right of the file
2. **Click the pencil icon** ✏️ (says "Edit this file" when you hover)
3. Now you can edit the text!

---

### CHANGE #1: Fix the image

**Find this line** (around line 95):
```typescript
image: 'img/docusaurus-social-card.jpg',
```

**HOW TO FIND IT:**
- Press `Ctrl+F` (Windows) or `Cmd+F` (Mac)
- Type: `docusaurus-social-card`
- Press Enter
- It will highlight the line

**CHANGE IT TO:**
```typescript
image: 'img/logo.svg',
```

**What you're changing:**
- Delete: `docusaurus-social-card.jpg`
- Type: `logo.svg`

---

### CHANGE #2: Fix the baseUrl

**Find this line** (around line 26):
```typescript
baseUrl: (process.env.RAILWAY_PUBLIC_DOMAIN || process.env.VERCEL_URL) ? '/' : '/newhumandiod-book/',
```

**HOW TO FIND IT:**
- Press `Ctrl+F`
- Type: `baseUrl:`
- Press Enter (might need to press Enter multiple times to find the right one)

**CHANGE THE ENTIRE LINE TO:**
```typescript
baseUrl: '/',
```

**What you're doing:**
- Select the ENTIRE line after `baseUrl: `
- Delete it all
- Type: `'/',`

---

### CHANGE #3: Fix footer links

**Find these lines** (around line 133-136):
```typescript
{
  label: 'Modules',
  to: '/docs/category/modules',
},
```

**HOW TO FIND IT:**
- Press `Ctrl+F`
- Type: `category/modules`
- Press Enter

**REPLACE THOSE 4 LINES WITH THESE 8 LINES:**
```typescript
{
  label: 'Module 1',
  to: '/docs/category/module-1',
},
{
  label: 'Module 2',
  to: '/docs/category/module-2',
},
```

**What you're doing:**
- Select all 4 lines (from `{` to `},`)
- Delete them
- Paste the new 8 lines

---

### Step 1.3: Save your changes

1. **Scroll to the bottom** of the page
2. You'll see "Commit changes"
3. In the first box, type: `Fix deployment issues`
4. **Click the green button:** "Commit changes"
5. ✅ Done! First file updated!

---

## 📝 Part 2: Add nixpacks.toml (NEW FILE)

### Step 2.1: Create new file

1. **Go back** to your repository homepage
   - URL: https://github.com/Farhat-Naz/physical-ai-robotics-course
2. **Click:** "Add file" button (near the green "Code" button)
3. **Select:** "Create new file"

### Step 2.2: Name the file

1. At the top, you'll see a text box that says "Name your file..."
2. **Type exactly:** `nixpacks.toml`
3. Make sure it's spelled correctly!

### Step 2.3: Add the content

**Copy and paste this ENTIRE block into the big text area:**

```toml
[phases.setup]
nixPkgs = ["nodejs_18"]

[phases.install]
cmds = ["npm ci"]

[phases.build]
cmds = ["npm run build"]

[start]
cmd = "npm run serve -- --host 0.0.0.0 --port $PORT"
```

### Step 2.4: Save the new file

1. **Scroll down**
2. You'll see "Commit new file"
3. In the first box, type: `Add nixpacks configuration`
4. **Click green button:** "Commit new file"
5. ✅ Done! New file created!

---

## 🚂 Part 3: Check Railway Dashboard

### Step 3.1: Wait a moment

After committing both changes:
- Wait 10-20 seconds
- Railway detects the changes automatically

### Step 3.2: Open Railway

1. Go to: **https://railway.app/dashboard**
2. **Click** on your project: `physical-ai-robotics-course`

### Step 3.3: Watch the deployment

You should see:
- **"Deploying..."** or **"Building..."**
- Status changes to show progress
- Logs scrolling (showing the build)

**Wait 2-3 minutes** for the build to complete.

### Step 3.4: Success!

When it's done, you'll see:
- ✅ Green checkmark
- Status: **"Active"** or **"Success"**
- Your URL will be visible (click to open your site!)

---

## ✅ Summary of Changes

We fixed 3 things:

1. **Image error** - Changed to existing logo.svg
2. **Wrong baseUrl** - Set to / for Railway
3. **Broken footer links** - Fixed module links

Plus added:
4. **nixpacks.toml** - Tells Railway exactly how to build

---

## 🆘 Having Trouble?

### Can't find docusaurus.config.ts?
- Make sure you're at: https://github.com/Farhat-Naz/physical-ai-robotics-course
- It should be in the main file list
- Scroll down if you don't see it

### Can't edit the file?
- Make sure you're logged into GitHub
- Make sure it's your repository
- Look for the pencil icon ✏️ at the top right

### Changes didn't save?
- Make sure you clicked "Commit changes"
- Check that both files were updated (go back and look)

### Railway still failing?
- Wait the full 2-3 minutes
- Check the Railway logs for specific errors
- Let me know what error you see

---

## 📞 Next Steps

After completing these edits:
1. ✅ Both files updated on GitHub
2. ⏳ Railway auto-deploys (2-3 min)
3. ✅ Site should be live!
4. 🔗 Get your URL from Railway dashboard

---

**Take your time with each step. Let me know when you've completed the edits!**
