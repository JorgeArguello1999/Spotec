from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Estudiante
from schools.models import Escuelas
from .forms import Estudiante_form
from competence import functions
from competence.models import Competencia

# Create your views here.
@login_required
def list(request):
    lista = Estudiante.objects.all()
    return render(request, 'list_insert_students.html', {
        "lista": lista
    })

@login_required
def create(request):
    if request.method != "GET":
        # Pasamos los datos obtenidos a una función para insertarlo en la tabla competencia
        functions.insert_student_in_compentence(request.POST)

        # Guardamos al Estudiante en la tabla estudiante
        salida = Estudiante_form(request.POST, escuelas_choices=[('', '---------')] + [(escuela.nombre, escuela.nombre) for escuela in Escuelas.objects.all()])
        salida.save()
        return redirect("list_insert_students")
    
    escuelas_choices = [('','---------')] + [(escuela.nombre, escuela.nombre) for escuela in Escuelas.objects.all()]
    form = Estudiante_form(escuelas_choices=escuelas_choices)
    return render(request, 'create_insert_students.html', {
        'form': form, 
        'escuelas_choices': escuelas_choices
    })

@login_required
def delete(request, cedula):
    student = get_object_or_404(Estudiante, cedula=cedula)
    student.delete()

    competence = Competencia.objects.filter(cedula=cedula)
    competence.delete()

    return redirect("list_insert_students")
