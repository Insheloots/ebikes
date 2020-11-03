from django.db import models

# Create your models here.
class Product(models.Model):
    nombre_producto = models.CharField(max_length=70)
    cantidad_producto = models.PositiveIntegerField()
    descripcion_producto = models.CharField(max_length=300)
    precio_unit = models.FloatField(max_length=20)