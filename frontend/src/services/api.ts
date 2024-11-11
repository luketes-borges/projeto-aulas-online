import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

// Adicione um interceptor para incluir o token JWT nas requisições
api.interceptors.request.use(config => {
  const token = localStorage.getItem('token'); // Recupere o token do localStorage
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
