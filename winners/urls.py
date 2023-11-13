from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_all, name="list_winners"),
    path("create/", views.create, name="create_winners"),
    path("<str:distancia>/<str:genero>/<str:categoria>/<str:prueba>", views.list_filter, name="list_filter"),
    path("<str:school_name>/", views.list_schools_filter, name="list_school_filter"),
]