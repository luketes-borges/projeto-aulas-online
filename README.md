# Projeto Aulas Online

Este projeto é uma aplicação web para gerenciamento de aulas online, com um backend em Django e um frontend em React com TypeScript.

## Vídeo de Demonstração

Veja o vídeo abaixo para mais detalhes sobre o projeto:

[![Demonstração do Projeto](https://img.youtube.com/vi/cx-fGsjWJJI/0.jpg)](https://www.youtube.com/watch?v=cx-fGsjWJJI)

Clique no vídeo para assistir à demonstração.

## Como Executar o Projeto

### Pré-requisitos
Backend: Python 3.11.7 (configurado via pyenv), SQL Server, e pip
Frontend: Node.js 20.12.2 e NVM para gerenciamento de versões de Node.js

### Configuração do Backend

1. Navegar para o Diretório do Backend
   - `cd backend`

2. Configurar o Ambiente Python
   - `pyenv local 3.11.7`
   - `python3.11 -m venv .venv`
   - MAC/linux `source .venv/bin/activate`
   - Windows `.venv/Scripts/activate`

3. Instalar Dependências
   - `pip install -r requirements.txt`

4. Executar Migrações
   - `python manage.py makemigrations`
   - `python manage.py migrate`

5. Criar Superusuário
   - `python manage.py createsuperuser`

6. Executar o Servidor de Desenvolvimento
   - `python manage.py runserver`

### Configuração do Frontend

1. Navegar para o Diretório do Frontend
   - `cd frontend`

2. Configurar o Ambiente Node.js
   - `nvm use 20.12.2`

3. Instalar Dependências
   - `npm install`

4. Executar o Servidor de Desenvolvimento
   - `npm start`

### Estrutura do Projeto

- backend/: Contém o código do backend em Django
- frontend/: Contém o código do frontend em React

### Documentação

No backend esta disponível uma documentação de API utilizando Swagger.

### Autor

Desenvolvido como parte de um desafio técnico para a vaga de Desenvolvedor Fullstack Junior.
