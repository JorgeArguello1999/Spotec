from django.shortcuts import render, redirect
from .models import Ganadores
from competence.models import Competencia

# Create your views here.
def list_all(request):
    competidores = Competencia.objects.all()

    return render(request, "list_winners.html", {
        "titulo": "Ganadores",
        "lista": competidores
    })

def list_filter(request, distancia, genero, categoria, prueba):
    pass

def create(request):
    if request.method != "GET":
        salida = request.POST
        print(salida["titulo"])
        print(salida["dataset"])
        print(type(salida["dataset"]))

    return redirect("list_winners") 