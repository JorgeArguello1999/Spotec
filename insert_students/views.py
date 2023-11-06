from django.shortcuts import render, redirect
from .models import create_student
from .forms import create_student_form

# Create your views here.
def list(request):
    lista = create_student.objects.all()
    return render(request, 'list.html', {
        "lista": lista
    })

def create(request):
    if request.method != "GET":
        salida = create_student_form(request.POST)
        salida.save()
        return redirect("list")
    
    return render(request, 'create.html', {
        "form": create_student_form
    })