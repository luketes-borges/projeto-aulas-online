import React, { useState, useEffect } from "react";
import { Outlet, useNavigate, Navigate, Routes, Route } from "react-router-dom";
import { Container, Navbar, Nav, NavDropdown, Image } from "react-bootstrap";
import { useAuth } from "../contexts/AuthContext";
import api from "../services/api";
import PrivateRoute from "../routes/PrivateRoute";
import Aulas from "../components/Aulas";
import AulaForm from "../components/AulaForm";
import Perfil from "../components/Perfil";
import DashboardInstrutor from "../components/DashboardInstrutor";
import "../styles/style.css";

const Layout: React.FC = () => {
  const { token, setToken } = useAuth();
  const [user, setUser] = useState<any | null>(null);
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    setToken(null);
    navigate("/login");
  };

  useEffect(() => {
    const fetchUserData = async () => {
      if (token) {
        try {
          const response = await api.get("/users/me/");
          setUser(response.data);
        } catch (error) {
          console.error("Erro ao buscar dados do usuário:", error);
        }
      }
    };

    fetchUserData();
  }, [token]);

  return (
    <div>
      {token && user && (
        <Navbar>
          <Container>
            <Navbar.Brand href="/">Aulas Online</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="me-auto">
                <Nav.Link href="/">Aulas</Nav.Link>
              </Nav>
              <Nav>
                <NavDropdown
                  title={
                    <>
                      {user.perfil && user.perfil.foto_perfil && (
                        <Image
                          src={user.perfil.foto_perfil}
                          roundedCircle
                          width={30}
                          height={30}
                          className="user-avatar"
                        />
                      )}
                      {user.username}
                    </>
                  }
                  id="basic-nav-dropdown"
                  drop="end"
                >
                  <NavDropdown.Item href="/perfil">Perfil</NavDropdown.Item>
                  <NavDropdown.Item onClick={handleLogout}>
                    Sair
                  </NavDropdown.Item>
                </NavDropdown>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
      )}
      <Container className="mt-5">
        <Routes>
          <Route element={<PrivateRoute />}>
            <Route path="/" element={<Aulas />} />
            <Route path="/aulas/criar" element={<AulaForm />} />
            <Route path="/aulas/:id/editar" element={<AulaForm />} />
            <Route path="/perfil" element={<Perfil />} />
            <Route path="/dashboard-instrutor" element={<DashboardInstrutor />} />
          </Route>
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </Container>
    </div>
  );
};

export default Layout;