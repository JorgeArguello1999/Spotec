from django.shortcuts import render, redirect, HttpResponse
from .models import Competencia
from .functions import *
import json

def list_all(request):
    lista = Competencia.objects.all()
    lista = lista.order_by("genero", "categoria", "prueba", "distancia", "tiempo_registro")

    return render(request, 'list_competence_all.html', {
        "lista": lista,
        "titulo": "Todas las competencias",
    })

def list_filter(request, distancia, genero, categoria, prueba):
    lista = Competencia.objects.filter(distancia=distancia, genero=genero, categoria=categoria, prueba=prueba)
    especial = "NO"

    if prueba == "REL":
        # En relevos se aceptan Hombre y Mujeres y la distancia es fija
        lista = Competencia.objects.filter(categoria=categoria, prueba=prueba)
        especial = "REL, no Genero, no distancia"
    
    if prueba == "COM":
        # En combinados la distancia es fija
        lista = Competencia.objects.filter(genero=genero, categoria=categoria, prueba=prueba)
        especial = "COM, no distancia"

    lista = lista.order_by("distancia")
    return render(request, 'list_competence.html', {
        "lista": lista,
        "titulo": f"{genero}-{categoria}-{prueba}-{distancia}",
        "distancia": distancia,
        "genero": genero,
        "categoria": categoria,
        "prueba": prueba,
        "especial": especial
    })

# Esta función es para insertar las actualizaciones 
def update(request, student_id, tiempo):
    registro = Competencia.objects.get(id=student_id)
    try:
        registro.tiempo_competencia = float(tiempo)
    except:
        registro.tiempo_competencia = float(0)
        
    registro.save()

    return HttpResponse("<script>window.close();</script>")