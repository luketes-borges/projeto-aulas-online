from rest_framework import serializers
from .models import Aula, Participante, Perfil
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'perfil']


class PerfilSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Perfil
        fields = ['id', 'user', 'foto_perfil', 'first_name', 'last_name', 'email']
        read_only_fields = ['id', 'user']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user

        # Atualiza os dados do perfil
        instance.foto_perfil = validated_data.get('foto_perfil', instance.foto_perfil)
        instance.save()

        # Atualiza os dados do usuário
        user.email = user_data.get('email', user.email)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)

        user.save()

        return instance


class AulaSerializer(serializers.ModelSerializer):
    instrutor = UserSerializer(read_only=True)
    participantes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    total_participantes = serializers.IntegerField(source='participantes.count', read_only=True)


    class Meta:
        model = Aula
        fields = '__all__'


class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'


class AulaInscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ['aula']
