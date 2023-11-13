from django.db import models

# Create your models here.
class Ganadores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    datos = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}-{self.nombre}"