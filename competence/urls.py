from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_all, name="list_all"),
    path("<str:distancia>/<str:genero>/<str:categoria>/<str:prueba>", views.list_filter, name="list_filter"),
    path("update/<str:student_id>/<str:tiempo>", views.update, name="update")
]