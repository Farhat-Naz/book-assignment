import React, { useState } from 'react';
import { useAuth } from './AuthContext';
import styles from './Auth.module.css';

export default function Signup({ onClose, onSwitchToLogin }: { onClose: () => void; onSwitchToLogin: () => void }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { signup, loginWithGoogle } = useAuth();

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    if (password !== confirmPassword) {
      return setError('Passwords do not match');
    }

    if (password.length < 6) {
      return setError('Password must be at least 6 characters');
    }

    try {
      setError('');
      setLoading(true);
      await signup(email, password);
      onClose();
    } catch (err: any) {
      setError('Failed to create an account: ' + err.message);
    }

    setLoading(false);
  }

  async function handleGoogleSignup() {
    try {
      setError('');
      setLoading(true);
      await loginWithGoogle();
      onClose();
    } catch (err: any) {
      setError('Failed to sign up with Google: ' + err.message);
    }
    setLoading(false);
  }

  return (
    <div className={styles.authModal}>
      <div className={styles.authContainer}>
        <button className={styles.closeBtn} onClick={onClose}>✕</button>
        <h2>Sign Up</h2>
        {error && <div className={styles.error}>{error}</div>}
        <form onSubmit={handleSubmit}>
          <div className={styles.formGroup}>
            <label>Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className={styles.formGroup}>
            <label>Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <div className={styles.formGroup}>
            <label>Confirm Password</label>
            <input
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" disabled={loading} className={styles.submitBtn}>
            {loading ? 'Loading...' : 'Sign Up'}
          </button>
        </form>
        <div className={styles.divider}>OR</div>
        <button onClick={handleGoogleSignup} disabled={loading} className={styles.googleBtn}>
          🔍 Continue with Google
        </button>
        <p className={styles.switchText}>
          Already have an account?{' '}
          <button onClick={onSwitchToLogin} className={styles.linkBtn}>
            Login
          </button>
        </p>
      </div>
    </div>
  );
}
