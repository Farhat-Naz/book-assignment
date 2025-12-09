import React from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { Redirect } from '@docusaurus/router';

interface ProtectedRouteProps {
  children: React.ReactNode;
}

export default function ProtectedRoute({ children }: ProtectedRouteProps) {
  const { currentUser, loading } = useAuth();

  if (loading) {
    return (
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          minHeight: '100vh',
          fontSize: '1.2rem',
          color: '#718096'
        }}
      >
        Loading...
      </div>
    );
  }

  if (!currentUser) {
    return <Redirect to="/login" />;
  }

  return <>{children}</>;
}
