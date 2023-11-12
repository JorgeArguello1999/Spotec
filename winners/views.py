from django.shortcuts import render
from .models import Ganadores
from competence.models import Competencia

# Create your views here.
def list_all(request):
    competidores = Competencia.objects.all().order_by("tiempo_competencia")
    # Recorre los competidores y actualiza los puntajes
    for i, competidor in enumerate(competidores):
        # Asigna puntajes según la posición en la clasificación
        puntaje = 9 - i
        # Competencia.objects.filter(id=competidor.id).update(puntos=puntaje)
        print(f"El jugador: {competidor.nombre} tiene:{puntaje}")
    
    print("Realizado")


    return render(request, "list_winners.html", {
        "titulo": "Ganadores",
        "lista": competidores
    })

def list_filter(request, distancia, genero, categoria, prueba):
    pass
