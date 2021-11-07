from django.urls import path
from . import views

app_name = "server"

urlpatterns = [
    path("", views.ServerListView.as_view(), name="list"),
    path("add", views.ServerAddView, name="add")
]
