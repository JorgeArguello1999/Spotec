from django.shortcuts import render
from . import functions

# Create your views here.
def list(request):
    return render(request, 'list_competence.html', {
        "lista": "lista"
    })

def create(request):
    return render(request, 'create_competence.html', {
        "list":"list"
    })