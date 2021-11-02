from django.contrib import admin
from .models import Aplicativos, Categorias, Configuracoes, Server
# Register your models here.

admin.site.register(Aplicativos)
admin.site.register(Categorias)
admin.site.register(Configuracoes)
admin.site.register(Server)