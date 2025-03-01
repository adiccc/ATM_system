// src/contexts/AuthContext.js
import React, { createContext, useState, useContext } from 'react';

// Create context
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [accountNumber, setAccountNumber] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Login function
  const login = (accountNum) => {
    setAccountNumber(accountNum);
    setIsAuthenticated(true);
  };

  // Logout function
  const logout = () => {
    setAccountNumber(null);
    setIsAuthenticated(false);
  };

  // Context value
  const value = {
    accountNumber,
    isAuthenticated,
    login,
    logout
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

// Custom hook to use auth context
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};