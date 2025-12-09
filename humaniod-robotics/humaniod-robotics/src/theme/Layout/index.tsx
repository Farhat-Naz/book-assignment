import React from 'react';
import Layout from '@theme-original/Layout';
import Chatbot from '@site/src/components/Chatbot';
import UserDropdown from '@site/src/components/Auth/UserDropdown';

export default function LayoutWrapper(props) {
  return (
    <>
      <Layout {...props} />
      <Chatbot />
      {/* User dropdown positioned in navbar */}
      <div style={{
        position: 'fixed',
        top: '0.5rem',
        right: '1rem',
        zIndex: 1000,
      }}>
        <UserDropdown />
      </div>
    </>
  );
}
