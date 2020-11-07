from django.db import models

# Create your models here.
class Propietario(models.Model):
    cedula_propietario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    correo_electronico = models.EmailField(max_length=70)
    direccion = models.CharField(max_length=70)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Proveedor(models.Model):
    id_proveedor = models.AutoField(auto_created=True, primary_key=True)
    cedula_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    nombre_proveedor = models.CharField(max_length=70)
    direccion = models.CharField(max_length=70)
    telefono = models.IntegerField()
    correo_electronico = models.EmailField(max_length=70)

class Tipo_Trabajador(models.Model):
    id_tipo = models.AutoField(auto_created=True, primary_key=True)
    tipo_trabajador = models.CharField(max_length=70)

class Salario_Trabajador(models.Model):
    id_salario = models.AutoField(auto_created=True, primary_key=True)
    sueldo_base = models.FloatField()
    honorarios = models.FloatField()
    seguro_social = models.FloatField()
    pensiones = models.FloatField()
    sueldo_total = models.FloatField()

class Trabajador(models.Model):
    cedula_trabajador = models.IntegerField(primary_key=True)
    id_salario = models.ForeignKey(Salario_Trabajador, on_delete=models.CASCADE)
    id_tipo = models.ForeignKey(Tipo_Trabajador, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    correo_electronico = models.EmailField(max_length=70)
    direccion = models.CharField(max_length=70)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Tipo_Producto(models.Model):
    id_tipo = models.AutoField(auto_created=True, primary_key=True)
    nombre_tipo = models.CharField(max_length=70)

class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    id_tipo = models.ForeignKey(Tipo_Producto, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=70)
    cantidad_producto = models.PositiveIntegerField()
    descripcion_producto = models.CharField(max_length=300)
    precio_unit = models.FloatField()

class Mensajero(models.Model):
    cedula_mensajero = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    correo_electronico = models.EmailField(max_length=70)
    direccion = models.CharField(max_length=70)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Ciudad(models.Model):
    id_ciudad = models.AutoField(auto_created=True, primary_key=True)
    nombre_ciudad = models.CharField(max_length=70)

class Comprador(models.Model):
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    cedula_comprador = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    correo_electronico = models.EmailField(max_length=70)
    direccion = models.CharField(max_length=70)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Factura(models.Model):
    id_factura = models.AutoField(auto_created=True, primary_key=True)
    id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cedula_comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    cedula_mensajero = models.ForeignKey(Mensajero, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    subtotal = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()

class Especificacion_Factura(models.Model):
    id_especificacion = models.AutoField(auto_created=True, primary_key=True)
    id = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    cantidad_compra = models.IntegerField()
    importe = models.FloatField()
