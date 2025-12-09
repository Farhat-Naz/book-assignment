import React, { createContext, useContext, useEffect, useState } from 'react';
import {
  User,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  GoogleAuthProvider,
  signInWithPopup,
  sendPasswordResetEmail,
  updateProfile
} from 'firebase/auth';
import { auth } from '../firebase/config';

interface AuthContextType {
  currentUser: User | null;
  loading: boolean;
  signup: (email: string, password: string, displayName?: string) => Promise<void>;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  loginWithGoogle: () => Promise<void>;
  resetPassword: (email: string) => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [currentUser, setCurrentUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  async function signup(email: string, password: string, displayName?: string) {
    if (!auth) {
      throw new Error('Firebase is not configured. Please add Firebase environment variables.');
    }
    const userCredential = await createUserWithEmailAndPassword(auth, email, password);
    if (displayName && userCredential.user) {
      await updateProfile(userCredential.user, { displayName });
    }
  }

  function login(email: string, password: string) {
    if (!auth) {
      throw new Error('Firebase is not configured. Please add Firebase environment variables.');
    }
    return signInWithEmailAndPassword(auth, email, password).then(() => {});
  }

  function logout() {
    if (!auth) {
      throw new Error('Firebase is not configured. Please add Firebase environment variables.');
    }
    return signOut(auth);
  }

  async function loginWithGoogle() {
    if (!auth) {
      throw new Error('Firebase is not configured. Please add Firebase environment variables.');
    }
    const provider = new GoogleAuthProvider();
    await signInWithPopup(auth, provider);
  }

  function resetPassword(email: string) {
    if (!auth) {
      throw new Error('Firebase is not configured. Please add Firebase environment variables.');
    }
    return sendPasswordResetEmail(auth, email);
  }

  useEffect(() => {
    // If Firebase auth is not configured, just set loading to false
    if (!auth) {
      console.warn('Firebase Auth not configured. Authentication features will be disabled.');
      setLoading(false);
      return;
    }

    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setCurrentUser(user);
      setLoading(false);
    });

    return unsubscribe;
  }, []);

  const value: AuthContextType = {
    currentUser,
    loading,
    signup,
    login,
    logout,
    loginWithGoogle,
    resetPassword
  };

  return (
    <AuthContext.Provider value={value}>
      {!loading && children}
    </AuthContext.Provider>
  );
}
