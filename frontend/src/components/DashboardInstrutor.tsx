import React, { useState, useEffect } from "react";
import api from "../services/api";
import { Aula } from "../types/Aula";
import { Table, Button } from "react-bootstrap";
import { Link } from "react-router-dom";
import "../styles/style.css";

const DashboardInstrutor: React.FC = () => {
  const [aulas, setAulas] = useState<Aula[]>([]);

  useEffect(() => {
    api.get("instrutor_dashboard/").then((response) => {
      setAulas(response.data);
    });
  }, []);

  return (
    <div>
      <h2>Dashboard do Instrutor</h2>

      <Table striped bordered hover responsive="sm">
        <thead>
          <tr>
            <th>Título</th>
            <th>Data e Hora</th>
            <th>Total de Participantes</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {aulas.map((aula) => (
            <tr key={aula.id}>
              <td data-label="Título">{aula.titulo}</td>
              <td data-label="Data e Hora">{new Date(aula.data_hora).toLocaleString()}</td>
              <td data-label="Total de Participantes">{aula.total_participantes}</td>
              <td data-label="Ações">
                <Link to={`/aulas/${aula.id}/editar`}>
                  <Button variant="primary">Editar</Button>
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default DashboardInstrutor;