// Simple chatbot loader
(function() {
  // Wait for page to load
  window.addEventListener('load', function() {
    console.log('Chatbot loader: Page loaded, initializing...');

    // Create chatbot button
    const button = document.createElement('button');
    button.id = 'chatbot-button';
    button.innerHTML = '💬';
    button.style.cssText = `
      position: fixed;
      bottom: 24px;
      right: 24px;
      width: 60px;
      height: 60px;
      border-radius: 50%;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      border: none;
      color: white;
      font-size: 24px;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      z-index: 9999;
    `;

    button.onclick = function() {
      alert('Chatbot UI loaded! Backend integration pending.');
    };

    document.body.appendChild(button);
    console.log('Chatbot button added successfully!');
  });
})();
