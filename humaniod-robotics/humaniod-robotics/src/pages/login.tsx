import React from 'react';
import Layout from '@theme/Layout';
import Login from '../components/Auth/Login';

export default function LoginPage() {
  return (
    <Layout title="Sign In" noFooter>
      <Login />
    </Layout>
  );
}
