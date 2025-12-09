import React from 'react';
import { AuthProvider } from '../contexts/AuthContext';

// This component wraps the entire app and provides global context
// Note: Chatbot is integrated via Layout component
export default function Root({children}: {children: React.ReactNode}): JSX.Element {
  return (
    <AuthProvider>
      {children}
    </AuthProvider>
  );
}
