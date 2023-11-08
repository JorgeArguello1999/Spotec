from django.forms import ModelForm
from .models import Estudiante

class Estudiante_form(ModelForm):
    class Meta:
        model = Estudiante 
        fields = [
                "id",
                "cedula",
                "nombre",
                "provincia",
                "escuela",
                "categoria",
                "genero",
                "combinado_100m",
                "espalda_25m",
                "espalda_50m",
                "espalda_100m",
                "mariposa_25m",
                "mariposa_50m",
                "mariposa_100m",
                "libre_25m_tarde",
                "libre_50m_tarde",
                "libre_100m_tarde",
                "pecho_25m_tarde",
                "pecho_50m_tarde",
                "pecho_100m_tarde",
                "relevos_4x50_libre_mixto",
                "snorkel_libre_25m",
                "snorkel_libre_50m",
                "snorkel_libre_100m"
        ]