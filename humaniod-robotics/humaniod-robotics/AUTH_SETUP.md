# Authentication Setup Guide

This guide will help you set up Firebase Authentication for the Humanoid Robotics Course platform.

## Prerequisites

- Node.js 20.0 or higher
- A Google/Gmail account for Firebase
- Basic understanding of Firebase

## Step 1: Create a Firebase Project

1. Go to the [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project" or "Create a project"
3. Enter a project name (e.g., "humanoid-robotics-course")
4. Choose whether to enable Google Analytics (optional)
5. Click "Create project"

## Step 2: Register Your Web App

1. In your Firebase project, click the web icon (`</>`) to add a web app
2. Enter an app nickname (e.g., "Robotics Course Web")
3. Check "Also set up Firebase Hosting" if you want to use Firebase Hosting
4. Click "Register app"
5. Copy the Firebase configuration object (you'll need this later)

## Step 3: Enable Authentication Methods

1. In the Firebase Console, go to **Build** > **Authentication**
2. Click "Get started" if this is your first time
3. Go to the **Sign-in method** tab
4. Enable the following providers:
   - **Email/Password**: Click on it, toggle "Enable", and save
   - **Google**: Click on it, toggle "Enable", select a support email, and save

## Step 4: Configure Firestore (Optional but Recommended)

If you want to store user data or course progress:

1. Go to **Build** > **Firestore Database**
2. Click "Create database"
3. Choose a location (closest to your users)
4. Start in **test mode** for development (you can secure it later)

### Firestore Security Rules (Production)

Once you're ready for production, update your Firestore rules:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Allow users to read/write their own data
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    // Allow authenticated users to read course content
    match /courses/{courseId} {
      allow read: if request.auth != null;
      allow write: if false; // Only allow writes through admin SDK
    }
  }
}
```

## Step 5: Configure Environment Variables

1. Copy `.env.example` to `.env.local` in the `humaniod-robotics` directory:

```bash
cp .env.example .env.local
```

2. Open `.env.local` and fill in your Firebase configuration values from Step 2:

```env
FIREBASE_API_KEY=AIzaSyC...
FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
FIREBASE_PROJECT_ID=your-project
FIREBASE_STORAGE_BUCKET=your-project.appspot.com
FIREBASE_MESSAGING_SENDER_ID=123456789
FIREBASE_APP_ID=1:123456789:web:abc123
```

3. Make sure `.env.local` is in your `.gitignore` (it should be by default)

## Step 6: Configure Docusaurus

The authentication system is already integrated into the Docusaurus theme. You need to ensure environment variables are accessible in the browser.

Create or update `docusaurus.config.ts`:

```typescript
const config: Config = {
  // ... other config
  customFields: {
    firebaseApiKey: process.env.FIREBASE_API_KEY,
    firebaseAuthDomain: process.env.FIREBASE_AUTH_DOMAIN,
    firebaseProjectId: process.env.FIREBASE_PROJECT_ID,
    firebaseStorageBucket: process.env.FIREBASE_STORAGE_BUCKET,
    firebaseMessagingSenderId: process.env.FIREBASE_MESSAGING_SENDER_ID,
    firebaseAppId: process.env.FIREBASE_APP_ID,
  },
};
```

Then update `src/firebase/config.ts` to use these:

```typescript
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export function useFirebaseConfig() {
  const { siteConfig } = useDocusaurusContext();
  return siteConfig.customFields;
}
```

## Step 7: Test the Authentication

1. Start the development server:

```bash
npm start
```

2. Navigate to `http://localhost:3000/signup`
3. Create a test account with email and password
4. Verify that you're redirected to the docs after signup
5. Test the Google Sign-In button
6. Test logout functionality

## Step 8: Protect Your Routes (Optional)

To make the docs accessible only to authenticated users, wrap the doc pages with `ProtectedRoute`:

```typescript
// src/theme/DocPage/index.tsx
import React from 'react';
import DocPage from '@theme-original/DocPage';
import ProtectedRoute from '../../components/Auth/ProtectedRoute';

export default function DocPageWrapper(props) {
  return (
    <ProtectedRoute>
      <DocPage {...props} />
    </ProtectedRoute>
  );
}
```

## Features Included

### Authentication Methods

- ✅ Email/Password authentication
- ✅ Google OAuth
- ✅ Password reset functionality

### User Interface

- ✅ Login page (`/login`)
- ✅ Signup page (`/signup`)
- ✅ Password reset page (`/forgot-password`)
- ✅ User profile page (`/profile`)
- ✅ User dropdown in navbar
- ✅ Protected routes

### User Experience

- ✅ Responsive design
- ✅ Loading states
- ✅ Error handling
- ✅ Auto-redirect after authentication
- ✅ Persistent authentication state

## Deployment Considerations

### Vercel

If deploying to Vercel, add your environment variables in the Vercel dashboard:

1. Go to your project settings
2. Navigate to "Environment Variables"
3. Add each `FIREBASE_*` variable
4. Make sure to add them for all environments (Production, Preview, Development)

### Firebase Security

1. **Add authorized domains** in Firebase Console:
   - Go to Authentication > Settings > Authorized domains
   - Add your production domain (e.g., `your-site.vercel.app`)

2. **Update Firebase Security Rules** for production

3. **Enable App Check** (optional but recommended):
   - Prevents abuse and ensures requests come from your app
   - Go to Build > App Check in Firebase Console

## Customization

### Styling

All authentication components use CSS modules. You can customize the styles:

- `src/components/Auth/Auth.module.css` - Login/Signup styles
- `src/components/Auth/UserProfile.module.css` - Profile page styles
- `src/components/Auth/UserDropdown.module.css` - Navbar dropdown styles

### Branding

Update the gradient colors in the CSS files to match your brand:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

## Troubleshooting

### "Firebase: Error (auth/configuration-not-found)"

- Make sure your `.env.local` file exists and has the correct values
- Restart the development server after adding environment variables

### "Firebase: Error (auth/unauthorized-domain)"

- Add your domain to the authorized domains in Firebase Console
- For localhost, it should be authorized by default

### Google Sign-In not working

- Ensure Google provider is enabled in Firebase Console
- Check that you've selected a support email in the Google sign-in settings
- Verify your authorized domains include your development and production URLs

## Next Steps

- Set up Firestore to store user progress
- Add email verification
- Implement role-based access control (admin, student, instructor)
- Add course progress tracking
- Implement quiz results storage
- Add user analytics

## Support

For issues or questions:
- Check the [Firebase Documentation](https://firebase.google.com/docs)
- Review the [Docusaurus Documentation](https://docusaurus.io/docs)
- Open an issue in the repository

---

**Made with ❤️ for robotics education**
