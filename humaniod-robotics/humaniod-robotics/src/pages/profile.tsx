import React from 'react';
import Layout from '@theme/Layout';
import UserProfile from '../components/Auth/UserProfile';
import ProtectedRoute from '../components/Auth/ProtectedRoute';

export default function ProfilePage() {
  return (
    <Layout title="Profile" noFooter>
      <ProtectedRoute>
        <UserProfile />
      </ProtectedRoute>
    </Layout>
  );
}
