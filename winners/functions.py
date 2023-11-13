from .models import Ganadores
from competence.models import Competencia

def create_ganadores(data):
    competidores = None
    if data["especial"] == "NO": competidores = Competencia.objects.filter(
        distancia=data["distancia"], genero=data["genero"], categoria=data["categoria"], prueba=data["prueba"]
    ).order_by("tiempo_competencia")

    if "REL" in data["especial"]: competidores = Competencia.objects.filter(
        categoria=data["categoria"], prueba=data["prueba"]
    ).order_by("tiempo_competencia")

    if "COM" in data["especial"]: competidores = Competencia.objects.filter(
        genero=data["genero"], categoria=data["categoria"], prueba=data["prueba"]
    ).order_by("tiempo_competencia")

    puesto = 1
    puntos = 9
    for i in competidores:
        if i.tiempo_competencia == None or i.tiempo_competencia == float(0):
            pass
        else:
            datos = {
                "id": i.id,
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
            elif puesto == 0: puntos = 0
            else: puntos = puntos - 1 
            puesto = puesto + 1 

            # Falla al actualizar el registro
            try:
                Ganadores.objects.update_or_create(**datos)
            except:
                obj = Ganadores.objects.get(id=i.id)
                obj.delete()
                Ganadores.objects.create(**datos)

    return {
        "distancia":data["distancia"], "genero":data["genero"], 
        "categoria":data["categoria"], "prueba":data["prueba"]
    }