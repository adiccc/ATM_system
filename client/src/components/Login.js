// src/components/Login.js
import React, { useState } from 'react';
import {
  Box,
  Card,
  CardContent,
  Typography,
  TextField,
  Button,
  Container,
  Alert,
  Snackbar,
  CircularProgress
} from '@mui/material';
import { AccountBalance as AccountBalanceIcon } from '@mui/icons-material';
import { useAuth } from '../contexts/AuthContext';
import apiService from '../services/api';

const Login = () => {
  const { login } = useAuth();
  const [accountNumber, setAccountNumber] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [showError, setShowError] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();

    if (!accountNumber.trim()) {
      setError('Please enter an account number');
      setShowError(true);
      return;
    }

    setLoading(true);

    try {
      // Check if account exists by getting balance
      await apiService.getBalance(accountNumber);

      // If we get here, the account exists or was created
      login(accountNumber);
    } catch (err) {
      console.error('Login error:', err);
      setError('Failed to access account. Please try again.');
      setShowError(true);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="sm">
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          minHeight: '100vh'
        }}
      >
        <AccountBalanceIcon
          sx={{
            fontSize: 60,
            color: 'primary.main',
            mb: 2
          }}
        />

        <Typography variant="h4" component="h1" gutterBottom>
          ATM System
        </Typography>

        <Card sx={{ width: '100%', mt: 3 }}>
          <CardContent>
            <Box component="form" onSubmit={handleLogin} noValidate>
              <Typography variant="h6" gutterBottom>
                Account Login
              </Typography>

              <TextField
                margin="normal"
                required
                fullWidth
                id="accountNumber"
                label="Account Number"
                name="accountNumber"
                autoFocus
                value={accountNumber}
                onChange={(e) => setAccountNumber(e.target.value)}
                inputProps={{ inputMode: 'numeric', pattern: '[0-9]*' }}
              />

              <Button
                type="submit"
                fullWidth
                variant="contained"
                size="large"
                sx={{ mt: 3, mb: 2 }}
                disabled={loading}
              >
                {loading ? (
                  <CircularProgress size={24} color="inherit" />
                ) : (
                  'Login'
                )}
              </Button>
            </Box>
          </CardContent>
        </Card>

        <Snackbar
          open={showError}
          autoHideDuration={6000}
          onClose={() => setShowError(false)}
          anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
        >
          <Alert
            onClose={() => setShowError(false)}
            severity="error"
            sx={{ width: '100%' }}
          >
            {error}
          </Alert>
        </Snackbar>
      </Box>
    </Container>
  );
};

export default Login;