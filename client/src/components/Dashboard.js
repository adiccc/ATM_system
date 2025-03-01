// src/components/Dashboard.js
import React, { useState, useEffect } from 'react';
import {
  Box,
  Card,
  CardContent,
  Typography,
  Button,
  Container,
  Grid,
  Divider,
  Alert,
  Snackbar,
  CircularProgress,
  Paper
} from '@mui/material';
import {
  AccountBalance as AccountIcon,
  ArrowUpward as DepositIcon,
  ArrowDownward as WithdrawIcon,
  Refresh as RefreshIcon,
  Logout as LogoutIcon
} from '@mui/icons-material';
import { useAuth } from '../contexts/AuthContext';
import apiService from '../services/api';
import TransactionDialog from './TransactionDialog';

const Dashboard = () => {
  const { accountNumber, logout } = useAuth();
  const [accountData, setAccountData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [transactionType, setTransactionType] = useState(null);
  const [processing, setProcessing] = useState(false);
  const [notification, setNotification] = useState({ show: false, message: '', type: 'success' });

  // Fetch account data
  const fetchAccountData = async () => {
    try {
      const data = await apiService.getBalance(accountNumber);
      setAccountData(data);
    } catch (error) {
      console.error('Error fetching account data:', error);
      setNotification({
        show: true,
        message: 'Failed to load account data. Please try again.',
        type: 'error'
      });
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  // Initial data fetch
  useEffect(() => {
    if (accountNumber) {
      fetchAccountData();
    }
  }, [accountNumber]);

  // Handle refresh
  const handleRefresh = () => {
    setRefreshing(true);
    fetchAccountData();
  };

  // Handle transaction submit
  const handleTransactionSubmit = async (amount) => {
    setProcessing(true);

    try {
      let result;

      if (transactionType === 'deposit') {
        result = await apiService.deposit(accountNumber, amount);
      } else {
        result = await apiService.withdraw(accountNumber, amount);
      }

      // Update account data with response
      setAccountData(result);

      // Show success notification
      setNotification({
        show: true,
        message: result.message || `${transactionType === 'deposit' ? 'Deposit' : 'Withdrawal'} successful`,
        type: 'success'
      });

      // Close dialog
      setTransactionType(null);
    } catch (error) {
      console.error('Transaction error:', error);

      let errorMessage = 'Transaction failed. Please try again.';

      // Get specific error message from API if available
      if (error.response?.data?.detail) {
        errorMessage = error.response.data.detail;
      } else if (transactionType === 'withdraw') {
        errorMessage = 'Withdrawal failed. Insufficient funds or account error.';
      }

      setNotification({
        show: true,
        message: errorMessage,
        type: 'error'
      });
    } finally {
      setProcessing(false);
    }
  };

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
        <CircularProgress size={60} />
      </Box>
    );
  }

  return (
    <Container maxWidth="md">
      <Box sx={{ my: 4 }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 4 }}>
          <Box sx={{ display: 'flex', alignItems: 'center' }}>
            <AccountIcon color="primary" sx={{ fontSize: 32, mr: 1 }} />
            <Typography variant="h4">Account Dashboard</Typography>
          </Box>

          <Button
            variant="outlined"
            color="error"
            startIcon={<LogoutIcon />}
            onClick={logout}
          >
            Logout
          </Button>
        </Box>

        <Card sx={{ mb: 4 }}>
          <CardContent>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <Typography variant="subtitle1" color="text.secondary">
                  Account Number
                </Typography>
                <Typography variant="h5">
                  {accountData?.account_number}
                </Typography>
              </Grid>

              <Grid item xs={12} sm={6}>
                <Typography variant="subtitle1" color="text.secondary">
                  Current Balance
                </Typography>
                <Typography variant="h4" color="primary.main" sx={{ fontWeight: 'bold' }}>
                  ${accountData?.balance.toFixed(2)}
                </Typography>
              </Grid>
            </Grid>

            <Box sx={{ display: 'flex', justifyContent: 'flex-end', mt: 2 }}>
              <Button
                startIcon={<RefreshIcon />}
                onClick={handleRefresh}
                disabled={refreshing}
                size="small"
              >
                {refreshing ? 'Updating...' : 'Refresh'}
              </Button>
            </Box>
          </CardContent>
        </Card>

        <Typography variant="h6" sx={{ mb: 2 }}>
          Actions
        </Typography>

        <Grid container spacing={3}>
          <Grid item xs={12} sm={6}>
            <Paper
              elevation={3}
              sx={{
                p: 3,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                cursor: 'pointer',
                '&:hover': { backgroundColor: 'action.hover' },
                height: '100%'
              }}
              onClick={() => setTransactionType('deposit')}
            >
              <DepositIcon sx={{ fontSize: 48, color: 'success.main', mb: 2 }} />
              <Typography variant="h6" color="success.main">Deposit Funds</Typography>
              <Typography variant="body2" color="text.secondary" align="center" sx={{ mt: 1 }}>
                Add money to your account
              </Typography>
            </Paper>
          </Grid>

          <Grid item xs={12} sm={6}>
            <Paper
              elevation={3}
              sx={{
                p: 3,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                cursor: 'pointer',
                '&:hover': { backgroundColor: 'action.hover' },
                height: '100%'
              }}
              onClick={() => setTransactionType('withdraw')}
            >
              <WithdrawIcon sx={{ fontSize: 48, color: 'primary.main', mb: 2 }} />
              <Typography variant="h6" color="primary.main">Withdraw Funds</Typography>
              <Typography variant="body2" color="text.secondary" align="center" sx={{ mt: 1 }}>
                Take money from your account
              </Typography>
            </Paper>
          </Grid>
        </Grid>

        {/* Transaction Dialog */}
        <TransactionDialog
          open={!!transactionType}
          onClose={() => setTransactionType(null)}
          type={transactionType}
          onSubmit={handleTransactionSubmit}
          processing={processing}
        />

        {/* Notification */}
        <Snackbar
          open={notification.show}
          autoHideDuration={6000}
          onClose={() => setNotification({ ...notification, show: false })}
          anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
        >
          <Alert
            onClose={() => setNotification({ ...notification, show: false })}
            severity={notification.type}
            sx={{ width: '100%' }}
          >
            {notification.message}
          </Alert>
        </Snackbar>
      </Box>
    </Container>
  );
};

export default Dashboard;