from django.shortcuts import render
from .models import Competencia
from . import functions

# Create your views here.
def list(request):
    lista = Competencia.objects.all()
    print(lista)
    # functions.insert_student_in_compentence(lista)
    return render(request, 'list_competence.html', {
        "lista": "lista"
    })

def create(request):
    return render(request, 'create_competence.html', {
        "list":"list"
    })