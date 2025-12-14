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
  const [isConnected, setIsConnected] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [isMinimized, setIsMinimized] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const wsRef = useRef<WebSocket | null>(null);

  // RAG backend WebSocket URL - adjust if needed
  const WS_URL = process.env.NODE_ENV === 'production'
    ? 'wss://your-rag-backend.com/ws/chat'
    : 'ws://localhost:8000/ws/chat';

  useEffect(() => {
    if (!isMinimized) {
      connectWebSocket();
    }
    return () => {
      if (wsRef.current) {
        wsRef.current.close();
      }
    };
  }, [isMinimized]);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const connectWebSocket = () => {
    try {
      const ws = new WebSocket(WS_URL);

      ws.onopen = () => {
        console.log('Connected to RAG chatbot');
        setIsConnected(true);
        setMessages([
          {
            id: Date.now().toString(),
            type: 'assistant',
            content: 'Hello! I\'m your Physical AI & Robotics course assistant. Ask me anything about the course content, robotics concepts, or specific chapters!',
            timestamp: new Date(),
          },
        ]);
      };

      ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        setIsLoading(false);

        if (data.type === 'complete') {
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
        } else if (data.type === 'error') {
          setMessages((prev) => [
            ...prev,
            {
              id: Date.now().toString(),
              type: 'error',
              content: data.error || 'An error occurred',
              timestamp: new Date(),
            },
          ]);
        }
      };

      ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        setIsConnected(false);
        setIsLoading(false);
        setMessages((prev) => [
          ...prev,
          {
            id: Date.now().toString(),
            type: 'error',
            content: 'Failed to connect to the chatbot. Please ensure the RAG server is running on localhost:8000.',
            timestamp: new Date(),
          },
        ]);
      };

      ws.onclose = () => {
        console.log('Disconnected from RAG chatbot');
        setIsConnected(false);
      };

      wsRef.current = ws;
    } catch (error) {
      console.error('Failed to connect:', error);
      setIsConnected(false);
    }
  };

  const sendMessage = () => {
    if (!input.trim() || !isConnected || isLoading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      type: 'user',
      content: input,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);

    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({ query: input }));
    }

    setInput('');
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
          {isConnected && <span className={styles.statusOnline}>●</span>}
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
          placeholder={isConnected ? "Ask about the course..." : "Connecting..."}
          disabled={!isConnected || isLoading}
          rows={1}
        />
        <button
          onClick={sendMessage}
          disabled={!input.trim() || !isConnected || isLoading}
          className={styles.sendBtn}
        >
          ➤
        </button>
      </div>

      {!isConnected && (
        <div className={styles.connectionWarning}>
          ⚠️ Not connected. Start the RAG server: <code>cd rag && uvicorn src.main:app --reload</code>
        </div>
      )}
    </div>
  );
};

export default ChatBot;
