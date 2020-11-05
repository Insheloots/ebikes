from django.db import models

# Create your models here.
class Propietario(models.Model):
    cedula_propietario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    correo = models.EmailField(max_length=70)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Proveedor(models.Model):
    id_proveedor = models.AutoField(auto_created=True, primary_key=True)
    cedula_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    nombre_proveedor = models.CharField(max_length=70)
    telefono = models.IntegerField()
    correo = models.EmailField(max_length=70)

class Tipo_Trabajador(models.Model):
    id_tipo = models.AutoField(auto_created=True, primary_key=True)
    tipo_trabajador = models.CharField(max_length=70)

class Trabajador(models.Model):
    cedula_trabajador = models.IntegerField(primary_key=True)
    id_tipo = models.ForeignKey(Tipo_Trabajador, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    correo = models.EmailField(max_length=70)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Product(models.Model):
    nombre_producto = models.CharField(max_length=70)
    cantidad_producto = models.PositiveIntegerField()
    descripcion_producto = models.CharField(max_length=300)
    precio_unit = models.FloatField(max_length=20)