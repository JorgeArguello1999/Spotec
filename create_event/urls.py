from django.urls import path
from . import views

urlpatterns = [
    path("", views.list, name="list_create_event"),
    path("create/", views.create, name="create_create_event")
]