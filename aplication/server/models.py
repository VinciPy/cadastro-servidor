from django.db import models

# Create your models here.


class Categorias(models.Model):
    TIPOS = (
        ('HARDWARE', 'Hardware'),
        ('SOFTWARE', 'Software'),
    )
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255, choices=TIPOS)

    def __str__(self):
        return self.nome


class Configuracoes(models.Model):

    nome = models.CharField(max_length=255)
    tipo = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Aplicativos(models.Model):

    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Server(models.Model):

    nome = models.CharField(max_length=255)
    config = models.ManyToManyField(Configuracoes)
    apps = models.ManyToManyField(Aplicativos)
    local = models.CharField(max_length=255)
