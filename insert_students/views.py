from django.shortcuts import render, redirect
from .models import create_student
from .forms import create_student_form

# Create your views here.
def list(request):
    lista = create_student.objects.all()
    return render(request, 'list_insert_students.html', {
        "lista": lista
    })

def create(request):
    if request.method != "GET":
        salida = create_student_form(request.POST)
        salida.save()
        return redirect("list_insert_students")
    
    return render(request, 'create_insert_students.html', {
        "form": create_student_form
    })