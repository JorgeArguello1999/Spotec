from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import Estudiante_form
from competence import functions

# Create your views here.
def list(request):
    lista = Estudiante.objects.all()
    return render(request, 'list_insert_students.html', {
        "lista": lista
    })

def create(request):
    if request.method != "GET":
        # Pasamos los datos obtenidos a una función para insertarlo en la tabla competencia
        functions.insert_student_in_compentence(request.POST)

        # Guardamos al Estudiante en la tabla estudiante
        salida = Estudiante_form(request.POST)
        salida.save()
        return redirect("list_insert_students")
    
    return render(request, 'create_insert_students.html', {
        "form": Estudiante_form
    })