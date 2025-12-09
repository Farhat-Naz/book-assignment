import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

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

// Initialize Firebase only on client-side
let app;
let auth;
let db;

if (typeof window !== 'undefined' && firebaseConfig.apiKey) {
  app = initializeApp(firebaseConfig);
  auth = getAuth(app);
  db = getFirestore(app);
}

export { auth, db };
export default app;
