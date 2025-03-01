// src/services/api.js
import axios from 'axios';

const API_URL = 'http://localhost:8000';  // Make sure this matches your server address

// Set up axios with more detailed error handling
axios.interceptors.response.use(
  response => response,
  error => {
    console.error('API error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// Create axios instance with base URL
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// API service methods
const apiService = {
  // Get account balance
  getBalance: async (accountNumber) => {
    try {
      const response = await api.get(`/accounts/${accountNumber}/balance`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Deposit money to account
  deposit: async (accountNumber, amount) => {
    try {
      const response = await api.post(`/accounts/${accountNumber}/deposit`, { amount });
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Withdraw money from account
  withdraw: async (accountNumber, amount) => {
    try {
      const response = await api.post(`/accounts/${accountNumber}/withdraw`, { amount });
      return response.data;
    } catch (error) {
      throw error;
    }
  }
};

export default apiService;