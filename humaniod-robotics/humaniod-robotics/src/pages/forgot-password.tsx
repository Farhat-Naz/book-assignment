import React from 'react';
import Layout from '@theme/Layout';
import ForgotPassword from '../components/Auth/ForgotPassword';

export default function ForgotPasswordPage() {
  return (
    <Layout title="Reset Password" noFooter>
      <ForgotPassword />
    </Layout>
  );
}
