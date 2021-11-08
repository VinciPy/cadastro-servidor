from django.views.generic import DetailView, ListView
from .models import Server
from .forms import ServerFormAdd
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


class ServerListView(ListView):
    model = Server


def ServerAddView(request):
    form = ServerFormAdd()
    if request.method == "POST":
        formset = ServerFormAdd(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
        return HttpResponseRedirect("/")
    return render(request, "server/add.html", {'form': form})
