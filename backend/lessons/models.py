from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    foto_perfil = models.ImageField(upload_to='../../frontend/public/fotos_perfil/', blank=True, null=True)
    # first_name = models.CharField(max_length=30, blank=True)
    # last_name = models.CharField(max_length=30, blank=True)
    # email = models.EmailField(blank=True)

    def get_foto_perfil(self):
        if self.foto_perfil:
            return self.foto_perfil.url
        return None

    def __str__(self):
        return f"Perfil de {self.user.username}"


class Aula(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    instrutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aulas_ministradas')

    def __str__(self):
        return self.titulo

    def total_participantes(self):
        return self.participantes.count()


class Participante(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name='participantes')
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aulas_participadas')
    data_inscricao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('aula', 'aluno') # Impede inscrições duplicadas

    def __str__(self):
        return f"{self.aluno.username} em {self.aula.titulo}"
