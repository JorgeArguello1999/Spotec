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

# Create your models here.
class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255, null=True)
    escuela = models.CharField(max_length=255, null=True)
    genero = models.CharField(max_length=1, choices=Genero)
    categoria = models.CharField(max_length=3, choices=Categorias)

    # Desde aquí se puede modificar dependiendo que pruebas existan
    # Las categorias a las que se inscriban va a depender de su edad

    # Eventos en la mañana 
    combinado_100m = models.FloatField(blank=True, null=True)
    
    espalda_25m = models.FloatField(blank=True, null=True)
    espalda_50m = models.FloatField(blank=True, null=True)
    espalda_100m = models.FloatField(blank=True, null=True)

    mariposa_25m = models.FloatField(blank=True, null=True)
    mariposa_50m = models.FloatField(blank=True, null=True)
    mariposa_100m = models.FloatField(blank=True, null=True)

    # Eventos en la tarde
    libre_25m_tarde = models.FloatField(blank=True, null=True)
    libre_50m_tarde = models.FloatField(blank=True, null=True)
    libre_100m_tarde = models.FloatField(blank=True, null=True)

    pecho_25m_tarde = models.FloatField(blank=True, null=True)
    pecho_50m_tarde = models.FloatField(blank=True, null=True)
    pecho_100m_tarde = models.FloatField(blank=True, null=True)

    # Extras
    relevos_4x50_libre_mixto = models.FloatField(blank=True, null=True)

    snorkel_libre_25m = models.FloatField(blank=True, null=True)
    snorkel_libre_50m = models.FloatField(blank=True, null=True)
    snorkel_libre_100m = models.FloatField(blank=True, null=True)