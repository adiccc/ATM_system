// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
// Roboto font is now loaded from Google Fonts CDN in index.html

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);