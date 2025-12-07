import React from 'react';
import Chatbot from '@site/src/components/Chatbot';

// This component wraps the entire app and is a good place to add global components
export default function Root({children}: {children: React.ReactNode}): JSX.Element {
  return (
    <>
      {children}
      <Chatbot />
    </>
  );
}
