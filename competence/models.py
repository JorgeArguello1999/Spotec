from django.db import models

class Competencia(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255, null=True)
    escuela = models.CharField(max_length=255, null=True)

    genero = models.CharField(max_length=1)
    categoria = models.CharField(max_length=3)
    prueba = models.CharField(max_length=3)
    distancia = models.CharField(max_length=3)

    tiempo_registro = models.FloatField(blank=True, null=True)
    tiempo_competencia = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}-{self.categoria}-{self.genero}-{self.prueba}-{self.distancia}"