from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_all, name="list_all_schools"),
    path("create/", views.create, name="create_school"), 
    path("delete/<int:school_id>", views.delete, name="delete_school")
]