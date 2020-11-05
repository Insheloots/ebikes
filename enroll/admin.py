from django.contrib import admin
from .models import Product, Propietario, Proveedor, Tipo_Trabajador, Trabajador

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_producto', 'cantidad_producto','descripcion_producto', 'precio_unit')

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('cedula_propietario', 'nombre', 'apellido','correo', 'telefono', 'fecha_nacimiento')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor','cedula_propietario', 'nombre_proveedor','telefono', 'correo')

@admin.register(Tipo_Trabajador)
class Tipo_TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('id_tipo','tipo_trabajador')

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('cedula_trabajador', 'id_tipo', 'nombre', 'apellido','correo', 'telefono', 'fecha_nacimiento')