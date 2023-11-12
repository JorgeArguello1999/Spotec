from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_all, name="list_winners"),
    # path("create/", views.create, name="create_insert_students"), 
    # path("delete/<str:cedula>", views.delete, name="delete_students")
]