import React, { useState, useEffect } from "react";
import api from "../services/api";
import { User } from "../types/User";
import { useAuth } from "../contexts/AuthContext";
import { Button, Form } from "react-bootstrap";
import "../styles/style.css";

const Perfil: React.FC = () => {
  const { token } = useAuth();
  const [user, setUser] = useState<User | null>(null);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [perfilImage, setPerfilImage] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    if (token) {
      const userId = 1; // Aqui, busque o ID real do usuário com base no token

      api.get<User>(`users/${userId}/`).then((response) => {
        setUser(response.data);
        setPerfilImage(response.data.get_foto_perfil);
        setFirstName(response.data.first_name);
        setLastName(response.data.last_name);
        setEmail(response.data.email);
      });
    }
  }, [token]);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files.length > 0) {
      setSelectedFile(event.target.files[0]);
    }
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    if (user) {
      const formData = new FormData();
      formData.append("get_foto_perfil", perfilImage)
      formData.append("first_name", firstName);
      formData.append("last_name", lastName);
      formData.append("email", email);

      if (selectedFile) {
        const allowedTypes = ["image/jpeg", "image/png", "image/jpg"];
        if (!allowedTypes.includes(selectedFile.type)) {
          console.error("Formato de arquivo não suportado. Por favor, envie uma imagem JPG ou PNG.");
          return;
        }
        formData.append("get_foto_perfil", selectedFile);
      }

      try {
        const response = await api.patch(`users/${user.id}/`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        setUser(response.data);
        console.log("Perfil atualizado:", response.data);
        setIsEditing(false); // Desativa o modo de edição após salvar
      } catch (error) {
        console.error("Erro ao atualizar perfil:", error);
      }
    }
  };

  const handleEditClick = () => {
    setIsEditing(true);
  };

  const handleCancelClick = () => {
    setIsEditing(false);
    // Restaura os valores iniciais
    if (user) {
      setFirstName(user.first_name);
      setLastName(user.last_name);
      setEmail(user.email);
      setSelectedFile(null); // Remove qualquer arquivo selecionado
    }
  };

  return (
    <div className="perfil-container">
      <h2>Perfil</h2>
      {user && (
        <Form onSubmit={handleSubmit}>
          <div className="perfil-details">
            <Form.Group controlId="formFirstName" className="mb-3">
              <Form.Label>Nome</Form.Label>
              <Form.Control
                type="text"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                disabled={!isEditing}
              />
            </Form.Group>

            <Form.Group controlId="formLastName" className="mb-3">
              <Form.Label>Sobrenome</Form.Label>
              <Form.Control
                type="text"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                disabled={!isEditing}
              />
            </Form.Group>

            <Form.Group controlId="formEmail" className="mb-3">
              <Form.Label>Email</Form.Label>
              <Form.Control
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                disabled={!isEditing}
              />
            </Form.Group>
          </div>

          {user.get_foto_perfil && (
            <img
              src={user.get_foto_perfil}
              alt="Foto de Perfil"
              className="perfil-photo-preview"
            />
          )}

          {isEditing && (
            <Form.Group controlId="formFile" className="mb-3">
              <Form.Label>Foto de Perfil</Form.Label>
              <Form.Control type="file" onChange={handleFileChange} />
            </Form.Group>
          )}

          <div className="perfil-buttons">
            {isEditing ? (
              <>
                <Button variant="primary" type="submit" onClick={handleSubmit}>
                  Salvar
                </Button>
                <Button variant="secondary" onClick={handleCancelClick} className="button-cancel">
                  Cancelar
                </Button>
              </>
            ) : (
              <Button variant="primary" onClick={handleEditClick}>
                Editar
              </Button>
            )}
          </div>
        </Form>
      )}
    </div>
  );
};

export default Perfil;