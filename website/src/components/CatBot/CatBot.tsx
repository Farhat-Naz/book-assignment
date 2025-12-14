import React, { useState, useEffect } from 'react';
import clsx from 'clsx';
import styles from './CatBot.module.css';

const CatBot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { id: 1, text: 'Meow! 👋 Welcome to our Physical AI & Humanoid Robotics course! I\'m your catbot assistant. Ask me anything about the course content!', sender: 'bot' }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [ws, setWs] = useState<WebSocket | null>(null);

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  // Initialize WebSocket connection when component mounts
  useEffect(() => {
    // Function to initialize WebSocket
    const initWebSocket = () => {
      // Use the appropriate URL based on environment
      let wsUrl;
      if (typeof window !== 'undefined') {
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        wsUrl = `${protocol}//${window.location.host}/ws/chat`;
      } else {
        // Default for server-side rendering
        wsUrl = 'ws://localhost:8000/ws/chat';  // Default RAG service URL
      }

      const websocket = new WebSocket(wsUrl);

      websocket.onopen = () => {
        console.log('Connected to CatBot RAG service');
      };

      websocket.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);

          if (data.type === 'complete') {
            const botResponse = {
              id: Date.now(),
              text: data.content,
              sender: 'bot',
              sources: data.sources || []
            };

            setMessages(prev => {
              // Remove the typing indicator message if it exists
              const updatedMessages = prev.filter(msg => msg.sender !== 'bot' || !msg.isTyping);
              return [...updatedMessages, botResponse];
            });
            setIsTyping(false);
          } else if (data.type === 'error') {
            const errorMessage = {
              id: Date.now(),
              text: `Error: ${data.error}`,
              sender: 'bot'
            };

            setMessages(prev => {
              const updatedMessages = prev.filter(msg => msg.sender !== 'bot' || !msg.isTyping);
              return [...updatedMessages, errorMessage];
            });
            setIsTyping(false);
          }
        } catch (error) {
          console.error('Error parsing WebSocket message:', error);
        }
      };

      websocket.onerror = (error) => {
        console.error('WebSocket error:', error);
      };

      websocket.onclose = () => {
        console.log('Disconnected from CatBot RAG service');
        // Attempt to reconnect after 3 seconds
        setTimeout(initWebSocket, 3000);
      };

      setWs(websocket);
    };

    initWebSocket();

    // Cleanup function
    return () => {
      if (ws) {
        ws.close();
      }
    };
  }, []);

  const handleSend = (e: React.FormEvent) => {
    e.preventDefault();
    if (inputValue.trim() === '' || !ws) return;

    // Add user message
    const newUserMessage = {
      id: Date.now(),
      text: inputValue,
      sender: 'user'
    };

    setMessages(prev => [...prev, newUserMessage]);
    setInputValue('');
    setIsTyping(true);

    // Send message via WebSocket
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({
        query: inputValue,
        chapter_filter: null  // Can be used to filter by specific chapters later
      }));
    } else {
      // Fallback if WebSocket is not connected
      setMessages(prev => {
        const updatedMessages = prev.filter(msg => msg.sender !== 'bot' || !msg.isTyping);
        return [...updatedMessages, {
          id: Date.now(),
          text: "Sorry, I'm having trouble connecting to the knowledge base. Please try again later.",
          sender: 'bot'
        }];
      });
      setIsTyping(false);
    }
  };

  return (
    <div className={styles.catBotContainer}>
      {/* Cat Bot Icon/Face */}
      <button
        className={clsx(styles.catIcon, isOpen ? styles.hidden : styles.visible)}
        onClick={toggleChat}
        aria-label="Open CatBot"
      >
        <div className={styles.catFace}>
          <div className={styles.catEars}>
            <div className={clsx(styles.catEar, styles.left)}></div>
            <div className={clsx(styles.catEar, styles.right)}></div>
          </div>
          <div className={styles.catHead}>
            <div className={styles.catEyes}>
              <div className={clsx(styles.catEye, styles.left)}></div>
              <div className={clsx(styles.catEye, styles.right)}></div>
            </div>
            <div className={styles.catNose}></div>
            <div className={styles.catMouth}>
              <div className={styles.whiskers}>
                <span className={styles.whiskerLeft}></span>
                <span className={styles.whiskerRight}></span>
              </div>
            </div>
          </div>
        </div>
      </button>

      {/* Chat Window */}
      <div className={clsx(styles.chatWindow, isOpen ? styles.open : styles.closed)}>
        <div className={styles.chatHeader}>
          <div className={styles.headerInfo}>
            <div className={styles.botAvatar}>
              <div className={styles.catIconSmall}>
                <div className={styles.catEars}>
                  <div className={clsx(styles.catEar, styles.left)}></div>
                  <div className={clsx(styles.catEar, styles.right)}></div>
                </div>
                <div className={styles.catHead}>
                  <div className={styles.catEyes}>
                    <div className={clsx(styles.catEye, styles.left)}></div>
                    <div className={clsx(styles.catEye, styles.right)}></div>
                  </div>
                </div>
              </div>
            </div>
            <div className={styles.botName}>CatBot (RAG)</div>
          </div>
          <button
            className={styles.closeButton}
            onClick={toggleChat}
            aria-label="Close Chat"
          >
            ✕
          </button>
        </div>

        <div className={styles.chatMessages}>
          {messages.map((message) => (
            <div
              key={message.id}
              className={clsx(
                styles.message,
                message.sender === 'user' ? styles.userMessage : styles.botMessage
              )}
            >
              {message.sender === 'bot' && (
                <div className={styles.botAvatarSmall}>
                  <div className={styles.catIconTiny}>
                    <div className={styles.catHead}>
                      <div className={styles.catEyes}>
                        <div className={clsx(styles.catEye, styles.left, styles.tiny)}></div>
                        <div className={clsx(styles.catEye, styles.right, styles.tiny)}></div>
                      </div>
                    </div>
                  </div>
                </div>
              )}
              <div className={styles.messageText}>
                {message.text}
                {message.sources && message.sources.length > 0 && (
                  <div className={styles.sources}>
                    <details>
                      <summary>Sources</summary>
                      <ul>
                        {message.sources.map((source: any, idx: number) => (
                          <li key={idx}>
                            {source.source ? source.source.split('/').pop() : 'Unknown source'}
                            (Score: {source.score.toFixed(3)})
                          </li>
                        ))}
                      </ul>
                    </details>
                  </div>
                )}
              </div>
              {message.sender === 'user' && (
                <div className={styles.userAvatar}></div>
              )}
            </div>
          ))}

          {isTyping && (
            <div className={clsx(styles.message, styles.botMessage)}>
              <div className={styles.botAvatarSmall}>
                <div className={styles.catIconTiny}>
                  <div className={styles.catHead}>
                    <div className={styles.catEyes}>
                      <div className={clsx(styles.catEye, styles.left, styles.tiny)}></div>
                      <div className={clsx(styles.catEye, styles.right, styles.tiny)}></div>
                    </div>
                  </div>
                </div>
              </div>
              <div className={styles.typingIndicator}>
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          )}
        </div>

        <form onSubmit={handleSend} className={styles.chatInputForm}>
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Ask about Physical AI, Robotics, ROS2, etc..."
            className={styles.chatInput}
            aria-label="Type your message to CatBot"
          />
          <button type="submit" className={styles.sendButton} aria-label="Send message">
            🕊️
          </button>
        </form>
      </div>
    </div>
  );
};

export default CatBot;