from django.shortcuts import render
from .models import Competencia
from . import functions

def list(request):
    lista = Competencia.objects.all()
    return render(request, 'list_competence.html', {
        "lista": lista,
        "titulo": "Todas las competencias"
    })

def list_filter(request, distancia, genero, categoria, prueba):
    lista = Competencia.objects.filter(distancia=distancia, genero=genero, categoria=categoria, prueba=prueba)
    return render(request, 'list_competence.html', {
        "lista": lista,
        "titulo": f"{genero} - {categoria} - {prueba} - {distancia}"
    })

def create(request):
    return render(request, 'create_competence.html', {
        "list":"list"
    })