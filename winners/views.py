from django.shortcuts import render
from .models import Ganadores

# Create your views here.
def list_all(request):
    lista = Ganadores.objects.all()

    return render(request, "list_winners.html", {
        "titulo": "Ganadores",
        "lista": lista
    })
