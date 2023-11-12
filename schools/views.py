from django.shortcuts import render, redirect
from .models import Escuelas
from .forms import Escuela_form

# Create your views here.
def list_all(request):
    lista = Escuelas.objects.all() 
    return render(request, 'list_schools.html', {
        "lista": lista,
        "titulo": "Lista de Escuelas"
    })

def create(request):
    if request.method != "GET":
        salida = Escuela_form(request.POST)
        salida.save()
        return redirect("list_all_schools")

    return render(request, 'create_schools.html', {
        "form": Escuela_form
    }) 

def delete(request, school_id):
    school = Escuelas.objects.get(id=school_id)
    school.delete()
    return redirect("list_all_schools")
