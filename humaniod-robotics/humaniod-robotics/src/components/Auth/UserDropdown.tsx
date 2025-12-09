import React, { useState, useRef, useEffect } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { useHistory } from '@docusaurus/router';
import styles from './UserDropdown.module.css';

export default function UserDropdown() {
  const { currentUser, logout } = useAuth();
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const history = useHistory();

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleLogout = async () => {
    try {
      await logout();
      setIsOpen(false);
      history.push('/');
    } catch (error) {
      console.error('Failed to logout:', error);
    }
  };

  if (!currentUser) {
    return (
      <div className={styles.authLinks}>
        <a href="/login" className={styles.loginLink}>
          Sign In
        </a>
        <a href="/signup" className={styles.signupLink}>
          Sign Up
        </a>
      </div>
    );
  }

  return (
    <div className={styles.userDropdown} ref={dropdownRef}>
      <button
        className={styles.userButton}
        onClick={() => setIsOpen(!isOpen)}
        aria-expanded={isOpen}
      >
        {currentUser.photoURL ? (
          <img
            src={currentUser.photoURL}
            alt={currentUser.displayName || 'User'}
            className={styles.userAvatar}
          />
        ) : (
          <div className={styles.avatarPlaceholder}>
            {(currentUser.displayName || currentUser.email || 'U').charAt(0).toUpperCase()}
          </div>
        )}
        <span className={styles.userName}>
          {currentUser.displayName || currentUser.email?.split('@')[0] || 'User'}
        </span>
        <svg
          className={`${styles.chevron} ${isOpen ? styles.chevronUp : ''}`}
          width="12"
          height="8"
          viewBox="0 0 12 8"
          fill="none"
        >
          <path
            d="M1 1.5L6 6.5L11 1.5"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
      </button>

      {isOpen && (
        <div className={styles.dropdownMenu}>
          <div className={styles.userInfo}>
            <div className={styles.userEmail}>{currentUser.email}</div>
          </div>
          <div className={styles.divider} />
          <a
            href="/profile"
            className={styles.menuItem}
            onClick={() => setIsOpen(false)}
          >
            <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
              <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2 2.5v-.5a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v.5a.5.5 0 0 0 .5.5h7a.5.5 0 0 0 .5-.5z" />
            </svg>
            Profile
          </a>
          <div className={styles.divider} />
          <button className={styles.menuItem} onClick={handleLogout}>
            <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
              <path d="M6 3.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-7a.5.5 0 0 1-.5-.5V11h1v1h6V4H7v1H6V3.5z" />
              <path d="M9.854 8.854a.5.5 0 0 0 0-.708L7.207 5.5l.647-.646a.5.5 0 1 0-.708-.708l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L7.207 9.5H13a.5.5 0 0 0 0-1H7.207l.647-.646z" />
            </svg>
            Sign Out
          </button>
        </div>
      )}
    </div>
  );
}
