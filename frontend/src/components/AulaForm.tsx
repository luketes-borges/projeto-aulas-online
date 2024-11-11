import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import api from '../services/api';
import { Aula } from '../types/Aula';
import { Form, Button } from 'react-bootstrap';
import "../styles/style.css";

const AulaForm: React.FC = () => {
  const navigate = useNavigate();
  const { id } = useParams();
  const [aula, setAula] = useState<Partial<Aula>>({});

  useEffect(() => {
    if (id) {
      api.get<Aula>(`aulas/${id}/`).then(response => {
        setAula(response.data);
      });
    }
  }, [id]);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      if (id) {
        await api.put(`aulas/${id}/`, aula);
      } else {
        await api.post('aulas/', aula);
      }
      navigate('/');
    } catch (error) {
      console.error("Erro ao salvar aula:", error);
    }
  };

  return (
    <div className="form-container">
      <h2>{id ? 'Editar Aula' : 'Criar Aula'}</h2>
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="titulo" className="form-group">
          <Form.Label className="form-label">Título</Form.Label>
          <Form.Control type="text" name="titulo" value={aula.titulo || ''} onChange={e => setAula({ ...aula, titulo: e.target.value })} required className="form-control" />
        </Form.Group>

        <Form.Group controlId="descricao" className="form-group">
          <Form.Label className="form-label">Descrição</Form.Label>
          <Form.Control as="textarea" rows={3} name="descricao" value={aula.descricao || ''} onChange={e => setAula({ ...aula, descricao: e.target.value })} required className="form-control" />
        </Form.Group>

        <Form.Group controlId="data_hora" className="form-group">
          <Form.Label className="form-label">Data e Hora</Form.Label>
          <Form.Control type="datetime-local" name="data_hora" value={aula.data_hora || ''} onChange={e => setAula({ ...aula, data_hora: e.target.value })} required className="form-control" />
        </Form.Group>

        <Button variant="primary" type="submit">
          Salvar
        </Button>
      </Form>
    </div>
  );
};

export default AulaForm;