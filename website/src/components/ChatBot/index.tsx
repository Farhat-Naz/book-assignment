import React, { useState, useRef, useEffect } from 'react';
import styles from './styles.module.css';

interface Message {
  id: string;
  type: 'user' | 'assistant' | 'error';
  content: string;
  sources?: Array<{
    source: string;
    score: number;
    content: string;
  }>;
  timestamp: Date;
}

const ChatBot: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isMinimized, setIsMinimized] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!isMinimized && messages.length === 0) {
      // Show welcome message
      setMessages([
        {
          id: Date.now().toString(),
          type: 'assistant',
          content: 'Hello! I\'m your Physical AI & Robotics course assistant. Ask me anything about the course content, robotics concepts, or specific topics!',
          timestamp: new Date(),
        },
      ]);
    }
  }, [isMinimized]);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const sendMessage = async () => {
    if (!input.trim() || isLoading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      type: 'user',
      content: input,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);
    setInput('');

    try {
      // Call Vercel serverless API
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: input }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Failed to get response');
      }

      // Add assistant response
      setMessages((prev) => [
        ...prev,
        {
          id: Date.now().toString(),
          type: 'assistant',
          content: data.content,
          sources: data.sources,
          timestamp: new Date(),
        },
      ]);
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages((prev) => [
        ...prev,
        {
          id: Date.now().toString(),
          type: 'error',
          content: `Error: ${error.message}. Please make sure the OpenAI API key is configured in Vercel environment variables.`,
          timestamp: new Date(),
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const toggleMinimize = () => {
    setIsMinimized(!isMinimized);
  };

  if (isMinimized) {
    return (
      <div className={styles.chatbotMinimized} onClick={toggleMinimize}>
        <span className={styles.chatIcon}>💬</span>
        <span className={styles.chatLabel}>Ask AI Assistant</span>
      </div>
    );
  }

  return (
    <div className={styles.chatbotContainer}>
      <div className={styles.chatbotHeader}>
        <div className={styles.headerLeft}>
          <span className={styles.botIcon}>🤖</span>
          <span className={styles.botName}>Course AI Assistant</span>
          <span className={styles.statusOnline}>●</span>
        </div>
        <button className={styles.minimizeBtn} onClick={toggleMinimize}>
          ✕
        </button>
      </div>

      <div className={styles.chatbotMessages}>
        {messages.map((message) => (
          <div key={message.id} className={`${styles.message} ${styles[message.type]}`}>
            <div className={styles.messageContent}>
              {message.content}
            </div>
            {message.sources && message.sources.length > 0 && (
              <div className={styles.sources}>
                <strong>Sources:</strong>
                <ul>
                  {message.sources.slice(0, 3).map((source, idx) => (
                    <li key={idx}>
                      <span className={styles.sourceName}>{source.source}</span>
                      <span className={styles.sourceScore}>(score: {source.score.toFixed(3)})</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
            <div className={styles.timestamp}>
              {message.timestamp.toLocaleTimeString()}
            </div>
          </div>
        ))}
        {isLoading && (
          <div className={`${styles.message} ${styles.assistant}`}>
            <div className={styles.messageContent}>
              <div className={styles.typingIndicator}>
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className={styles.chatbotInput}>
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Ask about the course..."
          disabled={isLoading}
          rows={1}
        />
        <button
          onClick={sendMessage}
          disabled={!input.trim() || isLoading}
          className={styles.sendBtn}
        >
          ➤
        </button>
      </div>
    </div>
  );
};

export default ChatBot;
