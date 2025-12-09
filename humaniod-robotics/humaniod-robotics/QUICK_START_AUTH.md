# Quick Start: Authentication Setup

This is a quick guide to get authentication up and running in 5 minutes.

## Step 1: Create Firebase Project (2 minutes)

1. Go to https://console.firebase.google.com/
2. Click "Add project" → Name it → Click "Create project"
3. In your project, click the web icon (`</>`)
4. Register your app and copy the config object

## Step 2: Enable Authentication (1 minute)

1. In Firebase Console: **Build** → **Authentication** → **Get started**
2. **Sign-in method** tab → Enable:
   - Email/Password (toggle + save)
   - Google (toggle + select support email + save)

## Step 3: Configure Environment Variables (1 minute)

Create `.env.local` in the `humaniod-robotics/humaniod-robotics` directory:

```env
FIREBASE_API_KEY=AIzaSy...
FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_STORAGE_BUCKET=your-project.appspot.com
FIREBASE_MESSAGING_SENDER_ID=123456789
FIREBASE_APP_ID=1:123456789:web:abc...
```

## Step 4: Start the App (1 minute)

```bash
cd humaniod-robotics/humaniod-robotics
npm start
```

## Test It Out

1. Go to http://localhost:3000/signup
2. Create an account
3. You should be redirected to the course content
4. Check the navbar - you'll see your profile dropdown

## Available Routes

- `/login` - Sign in page
- `/signup` - Sign up page
- `/forgot-password` - Password reset
- `/profile` - User profile (protected)

## Making Pages Protected

Wrap any page content with `ProtectedRoute`:

```tsx
import ProtectedRoute from '../components/Auth/ProtectedRoute';

export default function MyProtectedPage() {
  return (
    <ProtectedRoute>
      <div>This content requires authentication</div>
    </ProtectedRoute>
  );
}
```

## Features

✅ Email/Password authentication
✅ Google OAuth
✅ Password reset
✅ User profile page
✅ Protected routes
✅ Persistent login
✅ User dropdown in navbar

## Need More Help?

See `AUTH_SETUP.md` for detailed setup instructions, deployment guides, and troubleshooting.

## Production Deployment

When deploying to Vercel:

1. Go to your Vercel project settings
2. Add environment variables (same as `.env.local`)
3. In Firebase Console:
   - **Authentication** → **Settings** → **Authorized domains**
   - Add your Vercel domain (e.g., `your-site.vercel.app`)

Done! 🎉
