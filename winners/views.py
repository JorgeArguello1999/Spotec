from django.shortcuts import render, redirect
from .models import Ganadores
from .functions import create_ganadores
from .functions import list_schools_winners 
from schools.models import Escuelas

# Todas las escuelas

# Create your views here.
def list_all(request):
    competidores = Ganadores.objects.all()
    lista = list(competidores.values())

    escuelas = list_schools_winners()

    return render(request, "list_winners.html", {
        "titulo": "Ganadores",
        "lista": lista,
        "escuelas": escuelas
    })

def list_filter(request, distancia, genero, categoria, prueba):
    escuelas = list_schools_winners()

    lista = Ganadores.objects.filter(distancia=distancia, genero=genero, categoria=categoria, prueba=prueba)

    if prueba == "REL":
        # En relevos se aceptan Hombre y Mujeres y la distancia es fija
        lista = Ganadores.objects.filter(categoria=categoria, prueba=prueba)
    
    if prueba == "COM":
        # En combinados la distancia es fija
        lista = Ganadores.objects.filter(genero=genero, categoria=categoria, prueba=prueba)

    lista = lista.order_by("puesto")
    return render(request, 'list_winners.html', {
        "lista": lista,
        "titulo": f"{genero}-{categoria}-{prueba}-{distancia}",
        "escuelas": escuelas
    })

def list_schools_filter(request, school_name):
    escuelas = list_schools_winners()

    puntos_escuela = Ganadores.objects.raw(f"SELECT id, SUM(puntaje) AS suma_total FROM winners_ganadores where escuela = '{school_name}';")
    competencias_escuela = Ganadores.objects.filter(escuela=school_name)

    print(puntos_escuela)

    return render(request, 'list_schools_filter.html', {
        "name": school_name,
        "escuelas": escuelas, 
        "puntos": puntos_escuela,
        "lista": competencias_escuela
    })

def create(request):
    if request.method != "GET":
        salida = create_ganadores(request.POST)

    return redirect("list_filter", distancia=salida["distancia"], genero=salida["genero"],
        categoria=salida["categoria"], prueba=salida["prueba"]
    ) 