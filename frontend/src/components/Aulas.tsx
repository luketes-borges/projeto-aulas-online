import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import api from "../services/api";
import { useAuth } from "../contexts/AuthContext";
import { Aula } from "../types/Aula";
import { Button, Table } from "react-bootstrap";
import "../styles/style.css";

const Aulas: React.FC = () => {
  const { token } = useAuth();
  const [aulas, setAulas] = useState<Aula[]>([]);

  useEffect(() => {
    api.get("aulas/").then((response) => {
      setAulas(response.data);
    });
  }, []);

  const handleDelete = async (id: number) => {
    try {
      await api.delete(`aulas/${id}/`);
      setAulas(aulas.filter((aula) => aula.id !== id));
    } catch (error) {
      console.error("Erro ao deletar aula:", error);
    }
  };

  return (
    <div className="table-container">
      <h2>Aulas</h2>

      {token && (
        <Link to="/aulas/criar">
          <Button variant="primary" className="btn-primary">Criar Aula</Button>
        </Link>
      )}

      <Table striped bordered hover responsive="sm" className="table">
        <thead>
          <tr>
            <th>Título</th>
            <th>Instrutor</th>
            <th>Data e Hora</th>
            <th>Total de Participantes</th>
            {token && <th>Ações</th>}
          </tr>
        </thead>
        <tbody>
          {aulas.map((aula) => (
            <tr key={aula.id}>
              <td data-label="Título">{aula.titulo}</td>
              <td data-label="Instrutor">{aula.instrutor.username}</td>
              <td data-label="Data e Hora">{new Date(aula.data_hora).toLocaleString()}</td>
              <td data-label="Total de Participantes">{aula.total_participantes}</td>
              {token && (
                <td data-label="Ações" className="action-buttons">
                  <Button href={`/aulas/${aula.id}/editar`} className="btn-primary">Editar</Button>
                  <Button className="btn-danger" onClick={() => handleDelete(aula.id)}>
                    Excluir
                  </Button>
                </td>
              )}
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default Aulas;