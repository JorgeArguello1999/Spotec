from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import Estudiante_form

# Create your views here.
def list(request):
    lista = Estudiante.objects.all()
    return render(request, 'list_insert_students.html', {
        "lista": lista
    })

def create(request):
    if request.method != "GET":
        salida = Estudiante_form(request.POST)
        salida.save()
        return redirect("list_insert_students")
    
    return render(request, 'create_insert_students.html', {
        "form": Estudiante_form
    })