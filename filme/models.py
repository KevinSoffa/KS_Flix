from django.contrib.auth.models import AbstractUser
from distutils.command.upload import upload
from django.utils import timezone
from email.policy import default
from django.db import models


# Create your models here.

LISTA_CATEGORIAS = (
    ('ANALISES', 'Análises'),
    ('PROGRAMACAO', 'Programação'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTROS','Outros'),
)

class Filme(models.Model):
    titulo = models.CharField(
        max_length=100
    )
    descricao = models.TextField(
        max_length=1000
    )
    categoria = models.CharField(
        max_length=15,
        choices=LISTA_CATEGORIAS
    )
    visualizacao = models.IntegerField(
        default=0
    )
    data_criacao = models.DateTimeField(
        default=timezone.now
    )
    thumb = models.ImageField(
        upload_to='thumb_filmes'
    )

    def __str__(self):
        return self.titulo


class Episodio(models.Model):
    filme_ref = models.ForeignKey(
        'Filme',
        related_name='episodios',
        on_delete = models.CASCADE
    )

    titulo = models.CharField(
        max_length=100
    )
    video = models.URLField()

    def __str__(self):
        return self.filme_ref.titulo + " | " + self.titulo



class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField(
        'Filme'
    )
