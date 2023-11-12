from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_all, name="list_winners"),
    path("<str:distancia>/<str:genero>/<str:categoria>/<str:prueba>", views.list_filter, name="list_filter"),
    # path("delete/<str:cedula>", views.delete, name="delete_students")
]