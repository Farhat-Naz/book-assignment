import React, { useState } from 'react';
import { useAuth } from './AuthContext';
import styles from './Auth.module.css';

export default function Login({ onClose, onSwitchToSignup }: { onClose: () => void; onSwitchToSignup: () => void }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { login, loginWithGoogle } = useAuth();

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    try {
      setError('');
      setLoading(true);
      await login(email, password);
      onClose();
    } catch (err: any) {
      setError('Failed to log in: ' + err.message);
    }

    setLoading(false);
  }

  async function handleGoogleLogin() {
    try {
      setError('');
      setLoading(true);
      await loginWithGoogle();
      onClose();
    } catch (err: any) {
      setError('Failed to log in with Google: ' + err.message);
    }
    setLoading(false);
  }

  return (
    <div className={styles.authModal}>
      <div className={styles.authContainer}>
        <button className={styles.closeBtn} onClick={onClose}>✕</button>
        <h2>Login</h2>
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
          <button type="submit" disabled={loading} className={styles.submitBtn}>
            {loading ? 'Loading...' : 'Login'}
          </button>
        </form>
        <div className={styles.divider}>OR</div>
        <button onClick={handleGoogleLogin} disabled={loading} className={styles.googleBtn}>
          🔍 Continue with Google
        </button>
        <p className={styles.switchText}>
          Don't have an account?{' '}
          <button onClick={onSwitchToSignup} className={styles.linkBtn}>
            Sign up
          </button>
        </p>
      </div>
    </div>
  );
}
