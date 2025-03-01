// src/App.js
import React from 'react';
import { ThemeProvider } from '@mui/material/styles';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import theme from './theme';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Layout from './components/Layout';

// Component that conditionally renders based on auth state
const AppContent = () => {
  const { isAuthenticated } = useAuth();
  
  return (
    <Layout>
      {isAuthenticated ? <Dashboard /> : <Login />}
    </Layout>
  );
};

function App() {
  return (
    <ThemeProvider theme={theme}>
      <AuthProvider>
        <AppContent />
      </AuthProvider>
    </ThemeProvider>
  );
}

export default App;