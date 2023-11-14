from django import forms
from .models import Estudiante
from schools.models import Escuelas
from competence.functions import Genero, Categorias, PruebasManana, PruebasTarde, PruebasOpcionales, Distancia

class Estudiante_form(forms.ModelForm):
    escuelas_choices = [('','---------')] + [(escuela.nombre, escuela.nombre) for escuela in Escuelas.objects.all()]
    escuela = forms.ChoiceField(choices=escuelas_choices, required=False)

    
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
        
        # Añade las opciones predefinidas a los campos de selección
        for field_name, choices in [
            ('genero', Genero),
            ('categoria', Categorias),
            ('manana1_prueba', PruebasManana),
            ('manana1_distancia', Distancia),
            # ... Añade otras opciones predefinidas según sea necesario
        ]:
            self.fields[field_name].choices = choices

        # Establece valores predeterminados para los campos de tiempo
        for field_name in [
            'manana1_tiempo', 'manana2_tiempo',
            'tarde1_tiempo', 'tarde2_tiempo',
            'opcional1_tiempo', 'opcional2_tiempo',
        ]:
            self.fields[field_name].initial = 0
