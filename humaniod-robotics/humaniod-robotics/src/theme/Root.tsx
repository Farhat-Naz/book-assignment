import React from 'react';
import Chatbot from '@site/src/components/Chatbot';
import { AuthProvider } from '../contexts/AuthContext';

// This component wraps the entire app and is a good place to add global components
export default function Root({children}: {children: React.ReactNode}): JSX.Element {
  return (
    <AuthProvider>
      {children}
      <Chatbot />
    </AuthProvider>
  );
}
