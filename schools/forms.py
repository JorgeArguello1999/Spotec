from .models import Escuelas
from django.forms import ModelForm

class Escuela_form(ModelForm):
    class Meta():
        model = Escuelas
        fields = [
            "id", "nombre"
        ]
