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

    tiempo_registro = models.FloatField()
    tiempo_competencia = models.FloatField()

    def __str__(self):
        return self.nombre