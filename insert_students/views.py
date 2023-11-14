from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Estudiante
from .forms import Estudiante_form
from competence import functions
from competence.models import Competencia
from schools.models import Escuelas

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

        data_dict = {
            'cedula': request.POST['cedula'],
            'nombre': request.POST['nombre'],
            'provincia': request.POST.get('provincia', None),
            'escuela': request.POST.get('escuela', None),
            'genero': request.POST['genero'],
            'categoria': request.POST['categoria'],
            'manana1_prueba': request.POST.get('manana1_prueba', None),
            'manana1_distancia': request.POST.get('manana1_distancia', None),
            'manana1_tiempo': request.POST.get('manana1_tiempo', None),
            'manana2_prueba': request.POST.get('manana2_prueba', None),
            'manana2_distancia': request.POST.get('manana2_distancia', None),
            'manana2_tiempo': request.POST.get('manana2_tiempo', None),
            'tarde1_prueba': request.POST.get('tarde1_prueba', None),
            'tarde1_distancia': request.POST.get('tarde1_distancia', None),
            'tarde1_tiempo': request.POST.get('tarde1_tiempo', None),
            'tarde2_prueba': request.POST.get('tarde2_prueba', None),
            'tarde2_distancia': request.POST.get('tarde2_distancia', None),
            'tarde2_tiempo': request.POST.get('tarde2_tiempo', None),
            'opcional1_prueba': request.POST.get('opcional1_prueba', None),
            'opcional1_distancia': request.POST.get('opcional1_distancia', None),
            'opcional1_tiempo': request.POST.get('opcional1_tiempo', None),
            'opcional2_prueba': request.POST.get('opcional2_prueba', None),
            'opcional2_distancia': request.POST.get('opcional2_distancia', None),
            'opcional2_tiempo': request.POST.get('opcional2_tiempo', None),
        }
        print(request.POST)
        print(data_dict)

        # Guardamos al Estudiante en la tabla estudiante
        try:
            salida = Estudiante_form(data_dict)
            salida.save()
        except:
            salida = Estudiante.objects.create(data_dict)
            salida.save()
        return redirect("list_insert_students")
    
    # Devolvemos el formulario
    escuelas_choices = [('','---------')] + [(escuela.nombre, escuela.nombre) for escuela in Escuelas.objects.all()]
    form = Estudiante_form()
    form.fields['escuela'].choices = escuelas_choices
    
    return render(request, 'create_insert_students.html', {
        "form": Estudiante_form,
        "escuelas_choices": escuelas_choices
    })

@login_required
def delete(request, cedula):
    student = get_object_or_404(Estudiante, cedula=cedula)
    student.delete()

    competence = Competencia.objects.filter(cedula=cedula)
    competence.delete()

    return redirect("list_insert_students")