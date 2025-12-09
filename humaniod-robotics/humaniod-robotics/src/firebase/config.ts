import { initializeApp, FirebaseApp } from 'firebase/app';
import { getAuth, Auth } from 'firebase/auth';
import { getFirestore, Firestore } from 'firebase/firestore';

// Get Firebase configuration from Docusaurus customFields
function getFirebaseConfig() {
  if (typeof window !== 'undefined') {
    // Client-side: Access via window.docusaurus
    const customFields = (window as any).docusaurus?.siteConfig?.customFields || {};
    return {
      apiKey: customFields.firebaseApiKey || '',
      authDomain: customFields.firebaseAuthDomain || '',
      projectId: customFields.firebaseProjectId || '',
      storageBucket: customFields.firebaseStorageBucket || '',
      messagingSenderId: customFields.firebaseMessagingSenderId || '',
      appId: customFields.firebaseAppId || ''
    };
  }
  // Server-side: Return empty config (Firebase will only be used on client)
  return {
    apiKey: '',
    authDomain: '',
    projectId: '',
    storageBucket: '',
    messagingSenderId: '',
    appId: ''
  };
}

const firebaseConfig = getFirebaseConfig();

// Initialize Firebase only on client-side and when config is available
let app: FirebaseApp | undefined;
let auth: Auth | undefined;
let db: Firestore | undefined;

// Check if we have a valid Firebase config
const hasValidConfig = firebaseConfig.apiKey &&
                       firebaseConfig.authDomain &&
                       firebaseConfig.projectId;

if (typeof window !== 'undefined' && hasValidConfig) {
  try {
    app = initializeApp(firebaseConfig);
    auth = getAuth(app);
    db = getFirestore(app);
    console.log('Firebase initialized successfully');
  } catch (error) {
    console.warn('Firebase initialization failed:', error);
  }
} else if (typeof window !== 'undefined') {
  console.warn('Firebase not initialized: Missing configuration. Add Firebase environment variables to enable authentication.');
}

export { auth, db };
export default app;
