# 🚀 Push to GitHub - Simple Instructions

Since the tokens aren't working, here's the **simplest way** to push your code to GitHub:

---

## ✅ **Method 1: PowerShell (Recommended - 1 minute)**

### Step 1: Open PowerShell
- Press `Windows + X`
- Click "Windows PowerShell" or "Terminal"

### Step 2: Run These Commands

Copy and paste **each line** one at a time:

```powershell
cd "D:\quarterr 4\book\humaniod-robotics"
```

```powershell
git push -u origin main
```

### Step 3: Enter Credentials
When prompted:
- **Username**: `Farhat-Naz`
- **Password**: Use your personal access token (create one at https://github.com/settings/tokens)

**That's it!** ✅

---

## ✅ **Method 2: GitHub Desktop (If you have it installed)**

1. Open **GitHub Desktop**
2. Click **File** → **Add Local Repository**
3. Browse to: `D:\quarterr 4\book\humaniod-robotics`
4. Click **Publish repository**
5. Choose **Farhat-Naz** as the owner
6. Name: `book-assignment`
7. Click **Publish**

Done! ✅

---

## ✅ **Method 3: Create New Token with Correct Permissions**

If both methods above fail, create a new token:

1. Go to: https://github.com/settings/tokens/new
2. **Note**: `Book Deploy`
3. **Expiration**: 30 days
4. **Scopes**: Check ✅ **repo** (VERY FIRST checkbox - don't miss this!)
5. Generate token
6. Use this new token as the password

---

## 📊 **After Successful Push**

Once you see "✓ Successfully pushed", go to:
https://github.com/Farhat-Naz/book-assignment

You should see all 143 files!

---

## 🚀 **Next Step: Deploy to Vercel**

After pushing, I'll give you Vercel deployment instructions!
