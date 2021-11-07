from django.forms import ModelForm
from .models import Server


class ServerFormAdd(ModelForm):
    class Meta:
        model = Server
        fields = ['nome', 'config', 'apps', 'local']
