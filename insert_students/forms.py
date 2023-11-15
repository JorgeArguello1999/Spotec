from django import forms
from .models import Estudiante
from schools.models import Escuelas
from competence.functions import Genero, Categorias, PruebasManana, PruebasTarde, PruebasOpcionales, Distancia

import random

class Estudiante_form(forms.ModelForm):
    class Meta:
        model = Estudiante 
        fields = [
            "nombre", "cedula", "provincia", "escuela", "categoria", "genero",
            "manana1_prueba", "manana1_distancia", "manana1_tiempo",
            "manana2_prueba", "manana2_distancia", "manana2_tiempo",
            "tarde1_prueba", "tarde1_distancia", "tarde1_tiempo",
            "tarde2_prueba", "tarde2_distancia", "tarde2_tiempo",
            "opcional1_prueba", "opcional1_distancia", "opcional1_tiempo",
            "opcional2_prueba", "opcional2_distancia", "opcional2_tiempo",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Establece valores predeterminados para los campos de tiempo
        for field_name in [
            'manana1_tiempo', 'manana2_tiempo',
            'tarde1_tiempo', 'tarde2_tiempo',
            'opcional1_tiempo', 'opcional2_tiempo',
        ]:
            self.fields[field_name].initial = 0
        
        self.fields["cedula"].initial = random.randint(1, 1000000000)
        self.fields["escuela"].initial = "No colocar nada aqui"
