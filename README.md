
# **Projeto Aulas Online**

**Descrição**  
Este projeto é uma aplicação web para gerenciamento de aulas online, composta por um backend em Django e um frontend em React com TypeScript. O backend fornece uma API robusta, enquanto o frontend oferece uma interface moderna e responsiva para interação com os dados. O sistema é ideal para agendamento, controle e gestão de aulas online.

---

## **Funcionalidades**

- **Gerenciamento de Aulas**: Agendamento, edição e remoção de aulas com informações detalhadas.
- **Cadastro de Usuários**: Permite a criação e autenticação de usuários com autenticação JWT.
- **Integração Frontend e Backend**: Comunicação eficiente entre React e Django.
- **Documentação de API**: Documentação gerada com Swagger, acessível para desenvolvedores.

---

## **Demonstração**

Clique na imagem abaixo para assistir à demonstração do projeto:

[![Demonstração do Projeto](https://img.youtube.com/vi/cx-fGsjWJJI/0.jpg)](https://www.youtube.com/watch?v=cx-fGsjWJJI)

---

## **Pré-requisitos**

### **Backend**
- Python 3.11.7 (gerenciado via pyenv ou outra ferramenta)
- Microsoft SQL Server
- Pip para gerenciamento de pacotes

### **Frontend**
- Node.js 20.12.2 (gerenciado via NVM)
- Gerenciador de pacotes npm ou Yarn

---

## **Configuração do Ambiente**

### **Backend**

1. **Navegar para o Diretório do Backend**  
   ```bash
   cd backend
   ```

2. **Configurar o Ambiente Python**  
   ```bash
   pyenv local 3.11.7
   python3.11 -m venv .venv
   ```
   - Ativar o ambiente virtual:  
     - **Linux/Mac**: `source .venv/bin/activate`  
     - **Windows**: `.venv\Scripts\activate`

3. **Instalar Dependências**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar Variáveis de Ambiente**  
   Crie um arquivo `.env` no diretório do backend com o seguinte formato:  
   ```env
   SECRET_KEY='sua_chave_secreta'
   NAME='nome_do_banco'
   USER='usuario_do_banco'
   PASSWORD='senha_do_banco'
   HOST='localhost'
   ```

   - Para gerar uma nova `SECRET_KEY`:  
     ```bash
     python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
     ```

5. **Executar Migrações**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Criar Superusuário**  
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar o Servidor de Desenvolvimento**  
   ```bash
   python manage.py runserver
   ```

---

### **Frontend**

1. **Navegar para o Diretório do Frontend**  
   ```bash
   cd frontend
   ```

2. **Configurar o Ambiente Node.js**  
   ```bash
   nvm use 20.12.2
   ```

3. **Instalar Dependências**  
   ```bash
   npm install
   ```

4. **Iniciar o Servidor de Desenvolvimento**  
   ```bash
   npm start
   ```

---

## **Estrutura do Projeto**

- **backend/**: Código do backend em Django, com API e documentação.
- **frontend/**: Código do frontend em React, integrado à API do backend.

---

## **Documentação**

### **API (Swagger)**

1. Inicie o backend:
   ```bash
   python manage.py runserver
   ```
2. Acesse a documentação Swagger no navegador:
   ```
   http://127.0.0.1:8000/swagger
   ```

### **Autenticação com JWT**
- Faça uma requisição **POST** no endpoint `/token` com o corpo da requisição:  
  ```json
  {
    "username": "seu_usuario",
    "password": "sua_senha"
  }
  ```
- O retorno incluirá os tokens `access` e `refresh`. Utilize o token `access` como Bearer Token para autenticação nos outros endpoints.

---

## **Testes**

- Para rodar os testes do backend:
  ```bash
  pytest backend/tests/
  ```

---

## **Autor**

Lucas Borges

Este projeto foi desenvolvido como parte de um desafio técnico para a vaga de Desenvolvedor Fullstack Junior.
