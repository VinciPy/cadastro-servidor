from django.views.generic import DetailView, ListView
from .models import Server
# Create your views here.

class ServerListView(ListView):
    model = Server