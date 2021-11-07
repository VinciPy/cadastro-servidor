from django.views.generic import DetailView, ListView
from .models import Server
from .forms import ServerFormAdd
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


class ServerListView(ListView):
    model = Server


def ServerAddView(request):
    form = ServerFormAdd
    return render(request, "server/add.html", {'form': form})
