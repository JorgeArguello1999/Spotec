from django.urls import path
from . import views

urlpatterns = [
    path("", views.list, name="list_insert_students"),
    path("create/", views.create, name="create_insert_students"), 
    path("delete/<str:cedula>", views.delete, name="delete_students")
]