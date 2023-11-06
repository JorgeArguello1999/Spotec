from django.shortcuts import render
from .forms import create_evento_form
from .models import create_evento

# Create your views here.
def list(request):
    lista = create_evento.objects.all()
    return render(request, 'list.html', {
        "list": lista
    })

def create(request):
    return render(request, 'create.html', {
        "form": create_evento_form
    })