from .models import Competencia

Genero = (
    ("M", "Masculino"),
    ("F", "Femenino"),
)

Categorias = (
    ("MEN", "Menores 6 años"),
    ("7-8", "7-8 años"),
    ("9NO", "9 años novatos"),
    ("9CL", "9 años clasificados"),
    ("10N", "10 años novatos"),
    ("10C", "10 años clasificados"),
    ("11N", "11 años novatos"),
    ("11C", "11 años clasificados"),
    ("12N", "12 años novatos"),
    ("12C", "12 años clasificados"),
    ("34N", "13-14 años novatos"),
    ("34C", "13-14 años clasificados"),
    ("57N", "15-17 años novatos"),
    ("57C", "15-17 años clasificados"),
    ("18N", "18 en adelante novatos"),
    ("18C", "18 en adelante clasificados")
)

PruebasManana = (
    ("MAR", "Mariposa"),
    ("ESP", "Espalda"),
    ("COM", "Combinado"),
)

PruebasTarde = (
    ("LIB", "Libre"),
    ("PEC", "Pecho"),
)

PruebasOpcionales = (
    ("REL", "Relevos"),
    ("SNO", "Snorkel"),
)

Distancia = (
    ("25M", "25 metros"),
    ("50M", "50 metros"),
    ("10M", "100 metros"),
)

# Creamos una estructura de diccionario para almacenar la información
def insert_student_in_compentence(data):
    if data["tarde1_prueba"] != "":
        diccionario = {
            "cedula": data["cedula"],
            "nombre": data["nombre"],
            "provincia": data["provincia"],
            "escuela": data["escuela"],
            "genero": data["genero"],
            "categoria": data["categoria"],
            "prueba": data["tarde1_prueba"],
            "distancia": data["tarde1_distancia"],
            "tiempo_registro": float(data["tarde1_tiempo"]),
        }
        Competencia.objects.create(**diccionario)

    if data["tarde2_prueba"] != "":
        diccionario = {
            "cedula": data["cedula"],
            "nombre": data["nombre"],
            "provincia": data["provincia"],
            "escuela": data["escuela"],
            "genero": data["genero"],
            "categoria": data["categoria"],
            "prueba": data["tarde2_prueba"],
            "distancia": data["tarde2_distancia"],
            "tiempo_registro": float(data["tarde2_tiempo"]),
        }
        Competencia.objects.create(**diccionario)

    if data["manana1_prueba"] != "":
        diccionario = {
            "cedula": data["cedula"],
            "nombre": data["nombre"],
            "provincia": data["provincia"],
            "escuela": data["escuela"],
            "genero": data["genero"],
            "categoria": data["categoria"],
            "prueba": data["manana1_prueba"],
            "distancia": data["manana1_distancia"],
            "tiempo_registro": float(data["manana1_tiempo"]),
        }
        Competencia.objects.create(**diccionario)
       
    if data["manana2_prueba"] != "":
        diccionario = {
            "cedula": data["cedula"],
            "nombre": data["nombre"],
            "provincia": data["provincia"],
            "escuela": data["escuela"],
            "genero": data["genero"],
            "categoria": data["categoria"],
            "prueba": data["manana2_prueba"],
            "distancia": data["manana2_distancia"],
            "tiempo_registro": float(data["manana2_tiempo"]),
        }
        Competencia.objects.create(**diccionario)

    if data["opcional1_prueba"] != "":
        diccionario = {
            "cedula": data["cedula"],
            "nombre": data["nombre"],
            "provincia": data["provincia"],
            "escuela": data["escuela"],
            "genero": data["genero"],
            "categoria": data["categoria"],
            "prueba": data["opcional1_prueba"],
            "distancia": data["opcional1_distancia"],
            "tiempo_registro": float(data["opcional1_tiempo"]),
        }
        Competencia.objects.create(**diccionario)

    if data["opcional2_prueba"] != "":
        diccionario = {
            "cedula": data["cedula"],
            "nombre": data["nombre"],
            "provincia": data["provincia"],
            "escuela": data["escuela"],
            "genero": data["genero"],
            "categoria": data["categoria"],
            "prueba": data["opcional2_prueba"],
            "distancia": data["opcional2_distancia"],
            "tiempo_registro": float(data["opcional2_tiempo"]),
        }
        Competencia.objects.create(**diccionario)