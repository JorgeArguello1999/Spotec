from django.urls import path
from . import views

urlpatterns = [
    path("", views.list, name="list"),
    path("<str:distancia>/<str:genero>/<str:categoria>/<str:prueba>", views.list_filter, name="list_filter"),
    path("create/", views.create, name="create")
]