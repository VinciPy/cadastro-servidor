from django.db import models

# Create your models here.
class Categorias(models.Model):
    TIPOS = (
        ('HARDWARE', 'Hardware'),
        ('SOFTWARE', 'Software'),
    )
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255, choices=TIPOS)

class Configuracoes(models.Model):
    
    nome = models.CharField(max_length=255)
    tipo = models.ForeignKey(Categorias, on_delete=models.CASCADE)

class Aplicativos(models.Model):

    nome = models.CharField(max_length=255)


class Server(models.Model):
    
    nome = models.CharField(max_length=255)
    config = models.ManyToManyField(Configuracoes)
    apps = models.ForeignKey(Aplicativos, on_delete=models.CASCADE)
    local = models.CharField(max_length=255)

