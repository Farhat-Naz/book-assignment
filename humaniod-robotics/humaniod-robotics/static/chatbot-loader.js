// Simple chatbot loader - No dependencies required
(function() {
  'use strict';

  // Wait for page to fully load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChatbot);
  } else {
    initChatbot();
  }

  function initChatbot() {
    console.log('🤖 Initializing chatbot...');

    // Create chatbot button
    const button = document.createElement('button');
    button.id = 'chatbot-button';
    button.innerHTML = '💬';
    button.setAttribute('aria-label', 'Open chatbot');
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
      font-size: 28px;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.3s ease;
    `;

    // Add hover effect
    button.onmouseenter = function() {
      button.style.transform = 'scale(1.1)';
      button.style.boxShadow = '0 6px 16px rgba(0, 0, 0, 0.2)';
    };

    button.onmouseleave = function() {
      button.style.transform = 'scale(1)';
      button.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
    };

    // Create chat window
    const chatWindow = document.createElement('div');
    chatWindow.id = 'chatbot-window';
    chatWindow.style.cssText = `
      position: fixed;
      bottom: 100px;
      right: 24px;
      width: 400px;
      max-width: calc(100vw - 48px);
      height: 600px;
      max-height: calc(100vh - 150px);
      background: white;
      border-radius: 16px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
      display: none;
      flex-direction: column;
      z-index: 9998;
      overflow: hidden;
      border: 1px solid #e0e0e0;
    `;

    chatWindow.innerHTML = `
      <div style="padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 16px 16px 0 0;">
        <h3 style="margin: 0 0 8px 0; font-size: 18px; font-weight: 600;">📚 Book Assistant</h3>
        <p style="margin: 0; font-size: 13px; opacity: 0.9;">Ask me about Physical AI & Humanoid Robotics</p>
      </div>
      <div id="chat-messages" style="flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 12px;">
        <div style="text-align: center; padding: 20px; color: #666;">
          <p style="margin: 8px 0;">👋 Hi! I'm your AI assistant for this book.</p>
          <p style="margin: 8px 0; font-size: 14px;">This chatbot needs a backend API to function.</p>
          <p style="margin: 8px 0; font-size: 14px;">Coming soon with full RAG integration! 🚀</p>
        </div>
      </div>
      <div style="padding: 16px; border-top: 1px solid #e0e0e0; background: white; display: flex; gap: 8px;">
        <input
          type="text"
          id="chat-input"
          placeholder="Ask a question..."
          disabled
          style="flex: 1; padding: 10px 14px; border: 1px solid #ddd; border-radius: 20px; font-size: 14px; outline: none; background: #f5f5f5;"
        />
        <button
          id="chat-send"
          disabled
          style="width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border: none; color: white; font-size: 20px; cursor: not-allowed; opacity: 0.5;"
        >→</button>
      </div>
    `;

    // Toggle chat window
    let isOpen = false;
    button.onclick = function() {
      isOpen = !isOpen;
      if (isOpen) {
        chatWindow.style.display = 'flex';
        button.innerHTML = '✕';
      } else {
        chatWindow.style.display = 'none';
        button.innerHTML = '💬';
      }
    };

    // Close chat when clicking outside
    document.addEventListener('click', function(e) {
      if (isOpen && !chatWindow.contains(e.target) && e.target !== button) {
        isOpen = false;
        chatWindow.style.display = 'none';
        button.innerHTML = '💬';
      }
    });

    // Add to page
    document.body.appendChild(button);
    document.body.appendChild(chatWindow);

    console.log('✅ Chatbot button added successfully!');
  }
})();
