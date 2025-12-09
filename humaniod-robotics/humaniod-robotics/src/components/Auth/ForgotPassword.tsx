import React, { useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import styles from './Auth.module.css';

export default function ForgotPassword() {
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const { resetPassword } = useAuth();

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    if (!email) {
      return setError('Please enter your email');
    }

    try {
      setMessage('');
      setError('');
      setLoading(true);
      await resetPassword(email);
      setMessage('Password reset email sent. Check your inbox!');
    } catch (err) {
      setError('Failed to reset password. Please check your email address.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className={styles.authContainer}>
      <div className={styles.authCard}>
        <h1>Reset Password</h1>
        <p className={styles.subtitle}>
          Enter your email and we'll send you a link to reset your password
        </p>

        {error && <div className={styles.error}>{error}</div>}
        {message && (
          <div
            style={{
              background: '#c6f6d5',
              color: '#22543d',
              padding: '1rem',
              borderRadius: '6px',
              marginBottom: '1.5rem',
              fontSize: '0.9rem',
              borderLeft: '4px solid #22543d'
            }}
          >
            {message}
          </div>
        )}

        <form onSubmit={handleSubmit} className={styles.form}>
          <div className={styles.formGroup}>
            <label htmlFor="email">Email</label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              placeholder="your.email@example.com"
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className={styles.submitButton}
          >
            {loading ? 'Sending...' : 'Send Reset Link'}
          </button>
        </form>

        <div className={styles.footer}>
          <p>
            <a href="/login">Back to Sign In</a>
          </p>
          <p>
            Don't have an account? <a href="/signup">Sign up</a>
          </p>
        </div>
      </div>
    </div>
  );
}
