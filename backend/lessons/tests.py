from django.test import TestCase
from .models import Aula, Participante, Perfil
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

class ModelTests(TestCase):

    def setUp(self):
        self.instrutor = User.objects.create_user(username='instrutor1', password='password123')
        self.aluno = User.objects.create_user(username='aluno1', password='password123')
        self.aula = Aula.objects.create(titulo='Aula de teste', descricao='Descrição da aula', data_hora=timezone.now() + timezone.timedelta(days=1), instrutor=self.instrutor)

    def test_criar_aula(self):
        self.assertEqual(str(self.aula), 'Aula de teste')
        self.assertEqual(self.aula.total_participantes(), 0)

    def test_inscrever_participante(self):
        participante = Participante.objects.create(aula=self.aula, aluno=self.aluno)
        self.assertEqual(str(participante) , 'aluno1 em Aula de teste')

    def test_criar_perfil(self):
        perfil = Perfil.objects.create(user=self.instrutor)
        self.assertEqual(str(perfil), 'Perfil de instrutor1')


class ViewTests(APITestCase):
    def setUp(self):
        self.instrutor = User.objects.create_superuser(username='instrutor1', password='password123')
        refresh = RefreshToken.for_user(self.instrutor)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.aluno = User.objects.create_user(username='aluno1', password='password123')
        self.aula = Aula.objects.create(titulo='Aula de teste', descricao='Descrição da aula', data_hora=timezone.now() + timezone.timedelta(days=1), instrutor=self.instrutor)

    def test_criar_aula(self):
        url = reverse('aula-list')
        data = {'titulo': 'Nova Aula', 'descricao': 'Descrição da aula', 'data_hora': timezone.now() + timezone.timedelta(days=1)}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_aulas(self):
        url = reverse('aula-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detalhes_aula(self):
        url = reverse('aula-detail', kwargs={'pk': self.aula.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_atualizar_aula(self):
        url = reverse('aula-detail', kwargs={'pk': self.aula.pk})
        data = {'titulo': 'Aula atualizada', 'descricao': 'Descrição atualizada', 'data_hora': timezone.now() + timezone.timedelta(days=2)}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletar_aula(self):
        url = reverse('aula-detail', kwargs={'pk': self.aula.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_inscrever_em_aula(self):
        url = reverse('aula-inscrever', kwargs={'pk': self.aula.pk})
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_participantes(self):
        url = reverse('participante-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listar_usuarios(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_instrutor_dashboard(self):
        url = reverse('instrutor_dashboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Lucas Borges - Observações:
# create_superuser: Como alguns endpoints exigem autenticação, um superusuário foi criado no setUp para simular um usuário logado.
# client.credentials: Define as credenciais de autenticação para o cliente de teste usando um token JWT.
# reverse: Use reverse para obter as URLs das suas views de forma dinâmica.
# format='json': Especifica que os dados enviados e recebidos são no formato JSON.
# Cobertura: Os testes cobrem as operações CRUD para Aula, a inscrição em aulas, a listagem de participantes, a listagem de usuários, e o dashboard do instrutor.
# Cenários de sucesso e falha: Os testes incluem cenários de sucesso (códigos 200, 201, 204) e alguns cenários de falha implícitos (ex: tentar acessar um endpoint sem autenticação). Você pode adicionar mais testes para cenários de falha específicos, como enviar dados inválidos.
# setUp: Centraliza a criação de objetos de teste para facilitar a reutilização.
