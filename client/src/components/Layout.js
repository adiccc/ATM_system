// src/components/Layout.js
import React from 'react';
import { CssBaseline, Box, Container, AppBar, Toolbar, Typography } from '@mui/material';
import { AccountBalance as AccountBalanceIcon } from '@mui/icons-material';
import { useAuth } from '../contexts/AuthContext';

const Layout = ({ children }) => {
  const { isAuthenticated } = useAuth();

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      <CssBaseline />

      {isAuthenticated && (
        <AppBar position="static" color="primary" elevation={3}>
          <Container maxWidth="lg">
            <Toolbar disableGutters>
              <AccountBalanceIcon sx={{ mr: 1 }} />
              <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                ATM System
              </Typography>
            </Toolbar>
          </Container>
        </AppBar>
      )}

      <Box
        component="main"
        sx={{
          flexGrow: 1,
          bgcolor: (theme) => theme.palette.grey[50],
          pt: isAuthenticated ? 3 : 0
        }}
      >
        {children}
      </Box>

      <Box
        component="footer"
        sx={{
          py: 3,
          px: 2,
          mt: 'auto',
          backgroundColor: (theme) => theme.palette.grey[100],
          textAlign: 'center'
        }}
      >
        <Container maxWidth="sm">
          <Typography variant="body2" color="text.secondary">
            &copy; {new Date().getFullYear()} ATM System - All rights reserved
          </Typography>
        </Container>
      </Box>
    </Box>
  );
};

export default Layout;