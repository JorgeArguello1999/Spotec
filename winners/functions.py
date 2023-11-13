from .models import Ganadores
from competence.models import Competencia

"""

    genero = models.CharField(max_length=1)
    categoria = models.CharField(max_length=3)
    prueba = models.CharField(max_length=3)
    distancia = models.CharField(max_length=3)

    tiempo_registro = models.FloatField(blank=True, null=True)
    tiempo_competencia = models.FloatField(blank=True, null=True)

    puesto = models.IntegerField(blank=True, null=True)
    puntaje = models.IntegerField(blank=True, null=True)


"""

def create_ganadores(data):
    competidores = None
    if data["especial"] == "NO": competidores = Competencia.objects.filter(
        distancia=data["distancia"], genero=data["genero"], categoria=data["categoria"], prueba=data["prueba"]
    ).order_by("tiempo_competencia")

    if "REL" in data["especial"]: competidores = Competencia.objects.filter(categoria=data["categoria"], prueba=data["prueba"]).order_by("tiempo_competencia")

    if "COM" in data["especial"]: competidores = Competencia.objects.filter(
        genero=data["genero"], categoria=data["categoria"], prueba=data["prueba"]
    ).order_by("tiempo_competencia")

    puesto = 1
    puntos = 9
    for i in competidores:
        datos = {
            "id_student": i.id,
            "cedula": i.cedula,
            "nombre": i.nombre,
            "provincia": i.provincia,
            "escuela": i.escuela,
            "genero": i.genero,
            "categoria": i.categoria,
            "prueba": i.prueba,
            "distancia": i.distancia,
            "tiempo_registro": i.tiempo_registro,
            "tiempo_competencia": i.tiempo_competencia,
            "puesto": puesto,
            "puntaje": puntos 
        }
        if puesto == 1: puntos = puntos - 2
        else: puntos = puntos - 1 
        puesto = puesto + 1 

        objeto = Ganadores.objects.create(**datos)
        objeto.save()