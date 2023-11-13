from django.shortcuts import render, redirect
from .models import Ganadores
from .functions import create_ganadores

# Create your views here.
def list_all(request):
    competidores = Ganadores.objects.all()
    lista = list(competidores.values())
    print(lista)

    return render(request, "list_winners.html", {
        "titulo": "Ganadores",
        "lista": lista
    })

def list_filter(request, distancia, genero, categoria, prueba):
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
    })

def create(request):
    if request.method != "GET":
        salida = create_ganadores(request.POST)

    return redirect("list_filter", distancia=salida["distancia"], genero=salida["genero"],
        categoria=salida["categoria"], prueba=salida["prueba"]
    ) 