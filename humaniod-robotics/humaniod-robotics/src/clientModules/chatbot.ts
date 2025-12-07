import ExecutionEnvironment from '@docusaurus/ExecutionEnvironment';

if (ExecutionEnvironment.canUseDOM) {
  // Wait for document to be ready
  const initChatbot = async () => {
    try {
      const React = (await import('react')).default;
      const ReactDOM = (await import('react-dom/client')).default;
      const { default: Chatbot } = await import('../components/Chatbot');

      // Create a container for the chatbot
      const container = document.createElement('div');
      container.id = 'chatbot-root';
      document.body.appendChild(container);

      // Mount the chatbot
      const root = ReactDOM.createRoot(container);
      root.render(React.createElement(Chatbot));

      console.log('✅ Chatbot initialized successfully');
    } catch (error) {
      console.error('❌ Chatbot initialization failed:', error);
    }
  };

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChatbot);
  } else {
    initChatbot();
  }
}

export default {};
