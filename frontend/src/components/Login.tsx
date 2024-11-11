import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";
import { useAuth } from "../contexts/AuthContext";
import { Alert, Button, Form } from "react-bootstrap";
import { toast } from "react-toastify";
import "../styles/style.css";

const Login: React.FC = () => {
  const navigate = useNavigate();
  const { setToken } = useAuth();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setError(""); // Limpa a mensagem de erro anterior

    try {
      const response = await api.post("token/", { username, password });

      const token = response.data.access;
      localStorage.setItem("token", token);
      setToken(token);

      navigate("/");
    } catch (error: any) {
      if (error.response) {
        if (error.response.status === 401) {
          setError("Credenciais inválidas. Verifique seu usuário e senha.");
          toast.error("Credenciais inválidas. Verifique seu usuário e senha.");
        } else {
          setError("Erro ao fazer login. Por favor, tente novamente mais tarde.");
          toast.error("Erro ao fazer login. Por favor, tente novamente mais tarde.");
        }
      } else if (error.request) {
        setError("Erro de conexão. Verifique sua internet.");
        toast.error("Erro de conexão. Verifique sua internet.");
      } else {
        setError("Erro inesperado. Por favor, tente novamente mais tarde.");
        toast.error("Erro inesperado. Por favor, tente novamente mais tarde.");
      }

      console.error("Erro ao fazer login:", error);
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="username">
          <Form.Label>Usuário</Form.Label>
          <Form.Control
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </Form.Group>
        <Form.Group controlId="password">
          <Form.Label>Senha</Form.Label>
          <Form.Control
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <br />
        </Form.Group>
        <Button variant="primary" type="submit" className="button-submit">
          Entrar
        </Button>
        {error && (
          <Alert variant="danger" className="mt-3">
            {error}
          </Alert>
        )}
      </Form>
    </div>
  );
};

export default Login;