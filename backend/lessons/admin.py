from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Aula, Participante, Perfil

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfil'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (PerfilInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_foto_perfil')
    list_select_related = ('perfil', ) # Para otimizar a query

    def get_foto_perfil(self, instance):
        if instance.perfil.foto_perfil:
            return instance.perfil.foto_perfil.url  # Exibe o URL da imagem
        return '-'  # Ou algum texto se não houver imagem

    get_foto_perfil.short_description = 'Foto de Perfil'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instrutor', 'data_hora', 'total_participantes')
    list_filter = ('instrutor', 'data_hora')
    search_fields = ('titulo', 'descricao')

    def total_participantes(self, obj):
        return obj.participantes.count()

    total_participantes.short_description = 'Total de Participantes'


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('aula', 'aluno', 'data_inscricao')
    list_filter = ('aula', 'aluno')
    search_fields = ('aula__titulo', 'aluno__username')  # Busca pelo título da aula e username do aluno
