from django.shortcuts import render, redirect
from .forms import create_evento_form
from .models import create_evento

# Create your views here.
def list(request):
    lista = create_evento.objects.all()
    return render(request, 'list_create_event.html', {
        "lista": lista
    })

def create(request):
    if request.method != "GET":
        salida = create_evento_form(request.POST)
        salida.save()
        return redirect('list_create_event')

    return render(request, 'create_create_event.html', {
        "form": create_evento_form
    })

