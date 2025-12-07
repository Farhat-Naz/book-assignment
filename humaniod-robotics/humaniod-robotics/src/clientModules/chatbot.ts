import ExecutionEnvironment from '@docusaurus/ExecutionEnvironment';

if (ExecutionEnvironment.canUseDOM) {
  // Dynamically import and mount the chatbot
  import('../components/Chatbot').then((module) => {
    const Chatbot = module.default;
    const React = require('react');
    const ReactDOM = require('react-dom/client');

    // Create a container for the chatbot
    const container = document.createElement('div');
    container.id = 'chatbot-root';
    document.body.appendChild(container);

    // Mount the chatbot
    const root = ReactDOM.createRoot(container);
    root.render(React.createElement(Chatbot));
  });
}

export default {};
