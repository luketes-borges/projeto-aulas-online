import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import Layout from './components/Layout';
import Login from './components/Login';
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import './App.css';

function App() {
  return (
    <AuthProvider>
      <ToastContainer autoClose={10000} />
      <Router>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/*" element={<Layout />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
