from .models import Ganadores
from django.db.models import Sum
from competence.models import Competencia
from schools.models import Escuelas

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

def list_schools_winners():
    # Obtener todas las escuelas
    escuelas = Escuelas.objects.all()

    # Crear una lista para almacenar los diccionarios de resultados
    resultados = []

    for escuela in escuelas:
        # Obtener el nombre de la escuela
        nombre_escuela = escuela.nombre

        # Consultar la suma total de puntos para la escuela
        puntos_escuela = Ganadores.objects.filter(escuela=nombre_escuela).aggregate(suma_total=Sum('puntaje'))

        # Crear un diccionario con la información de la escuela y los puntos
        resultado_escuela = {
            'id': escuela.id,
            'nombre': nombre_escuela,
            'puntos': puntos_escuela['suma_total'] if puntos_escuela['suma_total'] else 0  # Manejar casos donde no hay puntaje
        }

        # Agregar el diccionario a la lista de resultados
        resultados.append(resultado_escuela)

    print(resultados)
    return resultados
