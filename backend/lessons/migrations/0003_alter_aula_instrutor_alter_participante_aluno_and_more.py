# Generated by Django 5.0.9 on 2024-11-10 16:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20241110_1130'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='instrutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aulas_ministradas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='participante',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aulas_participadas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL),
        ),
    ]
