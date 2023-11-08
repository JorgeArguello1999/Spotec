from django.db import models

# Create your models here.
class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255, null=True)
    escuela = models.CharField(max_length=255, null=True)

    # Desde aquí se puede modificar dependiendo que pruebas existan
    mariposa_hombre = models.FloatField(null=True, blank=True)
    espalda_hombre = models.FloatField(null=True, blank=True)
    braza_hombre = models.FloatField(null=True, blank=True)
    libre_hombre = models.FloatField(null=True, blank=True)

    mariposa_mujer = models.FloatField(null=True, blank=True)
    espalda_mujer = models.FloatField(null=True, blank=True)
    braza_mujer = models.FloatField(null=True, blank=True)
    libre_mujer = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class LibreHombre(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class EspaldaHombre(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class BrazaHombre(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class LibreHombre(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class MariposaMujer(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class EspaldaMujer(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class BrazaMujer(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class LibreMujer(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante