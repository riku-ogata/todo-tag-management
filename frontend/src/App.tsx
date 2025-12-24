// @ts-nocheck
import React from 'react';
import ReactDOM from 'react-dom/client';
import './App.css';
import './index.css';
import { BrowserRouter } from 'react-router-dom';
import AppRoutes from '@/routers/Index';

function App() {
  return (
    <BrowserRouter>
      <AppRoutes />
    </BrowserRouter>
  );
}

// Reactアプリケーションのエントリーポイント
const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);