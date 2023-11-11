from django.shortcuts import render, HttpResponse
from .models import Competencia
from django.http import JsonResponse
from .functions import *

def list_all(request):
    lista = Competencia.objects.all()
    lista = lista.order_by("genero", "categoria", "prueba", "distancia", "tiempo_registro")

    return render(request, 'list_competence.html', {
        "lista": lista,
        "titulo": "Todas las competencias",
    })

def list_filter(request, distancia, genero, categoria, prueba):
    lista = Competencia.objects.filter(distancia=distancia, genero=genero, categoria=categoria, prueba=prueba)

    if prueba == "REL":
        # En relevos se aceptan Hombre y Mujeres y la distancia es fija
        lista = Competencia.objects.filter(categoria=categoria, prueba=prueba)
    
    if prueba == "COM":
        # En combinados la distancia es fija
        lista = Competencia.objects.filter(genero=genero, categoria=categoria, prueba=prueba)

    lista = lista.order_by("distancia")
    return render(request, 'list_competence.html', {
        "lista": lista,
        "titulo": f"{genero} - {categoria} - {prueba} - {distancia}"
    })

# Esta función es para insertar las actualizaciones 
def update(request):
    if request.method == "POST":
        pass

    return HttpResponse(status=404)