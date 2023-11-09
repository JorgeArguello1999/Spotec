from django.db import models

# Importamos lass categorias, Generos, Pruebas y Distancias
from competence.functions import *

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