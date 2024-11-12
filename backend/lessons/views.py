from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Aula, Participante, Perfil
from .serializers import AulaSerializer, ParticipanteSerializer, AulaInscricaoSerializer, UserSerializer, PerfilSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User, Group
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Prefetch, Count
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView


class IsInstrutor(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            instrutor_group = Group.objects.get(name='Instrutores')
            return request.user.groups.filter(id=instrutor_group.id).exists()
        except Group.DoesNotExist:
            return False

class IsAluno(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            aluno_group = Group.objects.get(name='Alunos')
            return request.user.groups.filter(id=aluno_group.id).exists()
        except Group.DoesNotExist:
            return False

class IsAdministrador(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            admin_group = Group.objects.get(name='Administradores')
            return request.user.groups.filter(id=admin_group.id).exists()
        except Group.DoesNotExist:
            return False


class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all().select_related('instrutor').prefetch_related(
        Prefetch('participantes', queryset=Participante.objects.select_related('aluno'))
    ).annotate(total_participantes=Count('participantes'))
    serializer_class = AulaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsInstrutor | IsAdministrador]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['instrutor__id']

    @swagger_auto_schema(
        operation_summary="Listar todas as aulas",
        operation_description="Retorna uma lista de todas as aulas disponíveis.",
        responses={200: AulaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Criar uma nova aula",
        operation_description="Cria uma nova aula com os dados fornecidos.",
        request_body=AulaSerializer,
        responses={201: AulaSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Recuperar uma aula",
        operation_description="Retorna os detalhes de uma aula específica.",
        responses={200: AulaSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Atualizar uma aula",
        operation_description="Atualiza os detalhes de uma aula específica.",
        request_body=AulaSerializer,
        responses={200: AulaSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Deletar uma aula",
        operation_description="Deleta uma aula específica.",
        responses={204: 'Aula deletada com sucesso.'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(instrutor=self.request.user)

    @swagger_auto_schema(
        operation_summary="Inscrever em uma aula",
        operation_description="Inscreve o usuário atual na aula especificada.",
        responses={201: '{"status": "inscrito"}'}
    )
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated, IsAluno])
    def inscrever(self, request, pk=None):
        aula = self.get_object()
        serializer = AulaInscricaoSerializer(data={'aula': aula.id}, context={'request': request})
        if serializer.is_valid():
            Participante.objects.get_or_create(aula=aula, aluno=request.user)
            return Response({'status': 'inscrito'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all().select_related('aula', 'aluno')
    serializer_class = ParticipanteSerializer
    permission_classes = [permissions.IsAuthenticated, IsAluno | IsAdministrador]


class UserViewSet(viewsets.ModelViewSet, APIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = User.objects.all().prefetch_related('perfil')
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return PerfilSerializer
        return UserSerializer

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated], url_path='me')
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class InstrutorDashboardViewSet(viewsets.ViewSet):
    permission_classes = [IsInstrutor]

    @swagger_auto_schema(
        operation_summary="Dashboard do Instrutor",
        operation_description="Retorna as aulas do instrutor e o número de participantes.",
        responses={200: AulaSerializer(many=True)}
    )
    def list(self, request):
        aulas = Aula.objects.filter(instrutor=request.user).prefetch_related(
            Prefetch('participantes', queryset=Participante.objects.select_related('aluno'))
        ).annotate(total_participantes=Count('participantes'))
        aulas_serializadas = AulaSerializer(aulas, many=True, context={'request': request})
        return Response(aulas_serializadas.data)
