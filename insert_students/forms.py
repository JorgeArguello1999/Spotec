from django.forms import ModelForm
from .models import Estudiante

class Estudiante_form(ModelForm):
    class Meta:
        model = Estudiante 
        fields = [
            "id", "cedula", "nombre", "provincia", "escuela", "categoria", "genero",
            "manana1_prueba", "manana1_distancia", "manana1_tiempo",
            "manana2_prueba", "manana2_distancia", "manana2_tiempo",
            "tarde1_prueba", "tarde1_distancia", "tarde1_tiempo",
            "tarde2_prueba", "tarde2_distancia", "tarde2_tiempo",
            "opcional1_prueba", "opcional1_distancia", "opcional1_tiempo",
            "opcional2_prueba", "opcional2_distancia", "opcional2_tiempo",
        ]