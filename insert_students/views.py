from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Estudiante
from .forms import Estudiante_form
from competence import functions
from competence.models import Competencia

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

def delete(request, cedula):
    student = get_object_or_404(Estudiante, cedula=cedula)
    student.delete()

    competence = Competencia.objects.filter(cedula=cedula)
    competence.delete()

    return redirect("list_insert_students")