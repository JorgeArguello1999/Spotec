from .models import Ganadores
from competence.models import Competencia
import json

def create_ganadores(data):
    competidores = None
    if data["especial"] == "NO": competidores = Competencia.objects.filter(
        distancia=data["distancia"], genero=data["genero"], categoria=data["categoria"], prueba=data["prueba"]
    )

    if "REL" in data["especial"]: competidores = Competencia.objects.filter(categoria=data["categoria"], prueba=data["prueba"])

    if "COM" in data["especial"]: competidores = Competencia.objects.filter(genero=data["genero"], categoria=data["categoria"], prueba=data["prueba"])

    print(competidores)