import React from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { useHistory } from '@docusaurus/router';
import styles from './UserProfile.module.css';

export default function UserProfile() {
  const { currentUser, logout } = useAuth();
  const history = useHistory();

  if (!currentUser) {
    return null;
  }

  const handleLogout = async () => {
    try {
      await logout();
      history.push('/');
    } catch (error) {
      console.error('Failed to logout:', error);
    }
  };

  return (
    <div className={styles.profileContainer}>
      <div className={styles.profileCard}>
        <div className={styles.profileHeader}>
          <div className={styles.avatar}>
            {currentUser.photoURL ? (
              <img src={currentUser.photoURL} alt={currentUser.displayName || 'User'} />
            ) : (
              <div className={styles.avatarPlaceholder}>
                {(currentUser.displayName || currentUser.email || 'U').charAt(0).toUpperCase()}
              </div>
            )}
          </div>
          <div className={styles.userInfo}>
            <h2>{currentUser.displayName || 'User'}</h2>
            <p>{currentUser.email}</p>
          </div>
        </div>

        <div className={styles.profileSection}>
          <h3>Account Information</h3>
          <div className={styles.infoItem}>
            <span className={styles.label}>Email:</span>
            <span className={styles.value}>{currentUser.email}</span>
          </div>
          <div className={styles.infoItem}>
            <span className={styles.label}>Display Name:</span>
            <span className={styles.value}>{currentUser.displayName || 'Not set'}</span>
          </div>
          <div className={styles.infoItem}>
            <span className={styles.label}>Account Created:</span>
            <span className={styles.value}>
              {currentUser.metadata.creationTime
                ? new Date(currentUser.metadata.creationTime).toLocaleDateString()
                : 'Unknown'}
            </span>
          </div>
          <div className={styles.infoItem}>
            <span className={styles.label}>Last Sign In:</span>
            <span className={styles.value}>
              {currentUser.metadata.lastSignInTime
                ? new Date(currentUser.metadata.lastSignInTime).toLocaleDateString()
                : 'Unknown'}
            </span>
          </div>
        </div>

        <div className={styles.actions}>
          <button onClick={handleLogout} className={styles.logoutButton}>
            Sign Out
          </button>
        </div>
      </div>
    </div>
  );
}
