from django.db import models

class EspaldaHombre(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    escuela_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class BrazaHombre(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    escuela_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class MariposaHombre(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    escuela_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class LibreHombre(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    escuela_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class MariposaMujer(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    escuela_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class EspaldaMujer(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    escuela_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class BrazaMujer(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    escuela_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante

class LibreMujer(models.Model):
    id_estudiante = models.IntegerField()
    nombre_estudiante = models.TextField(max_length=255)
    provincia_estudiante = models.TextField(max_length=255)
    escuela_estudiante = models.TextField(max_length=255)
    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre_estudiante