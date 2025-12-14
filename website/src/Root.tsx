import React from 'react';
import CatBot from './components/CatBot/CatBot';

// This is the root wrapper for the entire app
// It will render the CatBot on all pages
export default function Root({children}) {
  return (
    <>
      {children}
      <CatBot />
    </>
  );
}