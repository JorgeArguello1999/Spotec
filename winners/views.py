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
    pass

def create(request):
    if request.method != "GET":
        create_ganadores(request.POST)

    return redirect("list_winners") 