from django.contrib import admin
from .models import Product, Propietario, Proveedor, Tipo_Trabajador, Trabajador, Salario_Trabajador, Tipo_Producto, Mensajero, Ciudad, Comprador, Factura, Especificacion_Factura

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_producto', 'cantidad_producto','descripcion_producto', 'precio_unit')

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('cedula_propietario', 'nombre', 'apellido','correo_electronico', 'direccion', 'telefono', 'fecha_nacimiento')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor','cedula_propietario', 'nombre_proveedor', 'direccion','telefono', 'correo_electronico')

@admin.register(Tipo_Trabajador)
class Tipo_TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('id_tipo','tipo_trabajador')

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('cedula_trabajador', 'id_tipo', 'nombre', 'apellido','correo_electronico', 'direccion', 'telefono', 'fecha_nacimiento')

@admin.register(Salario_Trabajador)
class Salario_TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('id_salario', 'sueldo_base', 'honorarios', 'seguro_social', 'pensiones', 'sueldo_total')

@admin.register(Tipo_Producto)
class Tipo_ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_tipo', 'nombre_tipo')

@admin.register(Mensajero)
class MensajeroAdmin(admin.ModelAdmin):
    list_display = ('cedula_mensajero', 'nombre', 'apellido','correo_electronico', 'direccion', 'telefono', 'fecha_nacimiento')

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id_ciudad', 'nombre_ciudad')

@admin.register(Comprador)
class CompradorAdmin(admin.ModelAdmin):
    list_display = ('cedula_comprador', 'nombre', 'apellido','correo_electronico', 'id_ciudad', 'direccion', 'telefono', 'fecha_nacimiento')

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id_factura', 'id', 'cedula_comprador', 'cedula_mensajero', 'fecha_emision', 'subtotal', 'iva', 'total')

@admin.register(Especificacion_Factura)
class Especificacion_FacturaAdmin(admin.ModelAdmin):
    list_display = ('id_especificacion', 'id', 'id_factura', 'cantidad_compra', 'importe')