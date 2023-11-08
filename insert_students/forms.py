from django.forms import ModelForm
from .models import Estudiante

class Estudiante_form(ModelForm):
    class Meta:
        model = Estudiante 
        fields = ["nombre", "cedula", "provincia", 
            "escuela", "mariposa_hombre", "espalda_hombre",
            "libre_hombre", "mariposa_mujer", "espalda_mujer",
            "libre_mujer"
        ]