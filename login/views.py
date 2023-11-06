from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.
def login_page(request):
    return render(request, 'login.html', {
        "form": UserCreationForm
    })