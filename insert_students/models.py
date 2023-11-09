from django.db import models

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

# Create your models here.
class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255, null=True)
    escuela = models.CharField(max_length=255, null=True)
    genero = models.CharField(max_length=1, choices=Genero)
    categoria = models.CharField(max_length=3, choices=Categorias)

    # Elegimos las categorias para la mañana
    manana1_prueba = models.CharField(max_length=3, choices=PruebasManana, null=True, blank=True)
    manana1_distancia = models.CharField(max_length=3, choices=Distancia, null=True, blank=True)
    manana1_tiempo = models.FloatField(null=True, blank=True)

    manana2_prueba = models.CharField(max_length=3, choices=PruebasManana, null=True, blank=True)
    manana2_distancia = models.CharField(max_length=3, choices=Distancia, null=True, blank=True)
    manana2_tiempo = models.FloatField(null=True, blank=True)

    # Elegimos las categorias para la tarde
    tarde1_prueba = models.CharField(max_length=3, choices=PruebasTarde, null=True, blank=True)
    tarde1_distancia = models.CharField(max_length=3, choices=Distancia, null=True, blank=True)
    tarde1_tiempo = models.FloatField(null=True, blank=True)

    tarde2_prueba = models.CharField(max_length=3, choices=PruebasTarde, null=True, blank=True)
    tarde2_distancia = models.CharField(max_length=3, choices=Distancia, null=True, blank=True)
    tarde2_tiempo = models.FloatField(null=True, blank=True)

    # Elegimos la categoria opcional
    opcional1_prueba = models.CharField(max_length=3, choices=PruebasOpcionales, null=True, blank=True)
    opcional1_distancia = models.CharField(max_length=3, choices=Distancia, null=True, blank=True)
    opcional1_tiempo = models.FloatField(null=True, blank=True)

    opcional2_prueba = models.CharField(max_length=3, choices=PruebasOpcionales, null=True, blank=True)
    opcional2_distancia = models.CharField(max_length=3, choices=Distancia, null=True, blank=True)
    opcional2_tiempo = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nombre