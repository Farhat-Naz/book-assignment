import React, { useState } from 'react';
import { useAuth } from './AuthContext';
import Login from './Login';
import Signup from './Signup';
import styles from './UserMenu.module.css';

export default function UserMenu() {
  const { currentUser, logout } = useAuth();
  const [showLogin, setShowLogin] = useState(false);
  const [showSignup, setShowSignup] = useState(false);
  const [showMenu, setShowMenu] = useState(false);

  async function handleLogout() {
    try {
      await logout();
      setShowMenu(false);
    } catch (error) {
      console.error('Failed to log out', error);
    }
  }

  if (!currentUser) {
    return (
      <>
        <div className={styles.authButtons}>
          <button
            onClick={() => setShowLogin(true)}
            className={styles.loginBtn}
          >
            Login
          </button>
          <button
            onClick={() => setShowSignup(true)}
            className={styles.signupBtn}
          >
            Sign Up
          </button>
        </div>

        {showLogin && (
          <Login
            onClose={() => setShowLogin(false)}
            onSwitchToSignup={() => {
              setShowLogin(false);
              setShowSignup(true);
            }}
          />
        )}

        {showSignup && (
          <Signup
            onClose={() => setShowSignup(false)}
            onSwitchToLogin={() => {
              setShowSignup(false);
              setShowLogin(true);
            }}
          />
        )}
      </>
    );
  }

  return (
    <div className={styles.userMenuContainer}>
      <button
        className={styles.userButton}
        onClick={() => setShowMenu(!showMenu)}
      >
        <span className={styles.userIcon}>👤</span>
        <span className={styles.userEmail}>{currentUser.email}</span>
      </button>

      {showMenu && (
        <div className={styles.dropdown}>
          <div className={styles.dropdownItem}>
            <strong>{currentUser.email}</strong>
          </div>
          <div className={styles.divider} />
          <button
            className={styles.dropdownItem}
            onClick={handleLogout}
          >
            Logout
          </button>
        </div>
      )}
    </div>
  );
}
