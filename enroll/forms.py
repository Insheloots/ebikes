from django.core import validators
from django import forms
from .models import Product, Propietario, Tipo_Producto, Proveedor, Comprador, Mensajero, Ciudad, Factura, Especificacion_Factura, Trabajador, Tipo_Trabajador, Salario_Trabajador

class ProductRegistration(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id_tipo','id_proveedor','nombre_producto','cantidad_producto', 'descripcion_producto','precio_unit']
        widgets = {
            'id_tipo': forms.NumberInput(attrs={'class':'form-control'}),
            'id_proveedor': forms.NumberInput(attrs={'class':'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad_producto': forms.NumberInput(attrs={'class':'form-control'}),
            'descripcion_producto': forms.TextInput(attrs={'class':'form-control'}),
            'precio_unit': forms.NumberInput(attrs={'class':'form-control'}),
        }

class PropietarioRegistration(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['cedula_propietario', 'nombre', 'apellido', 'correo_electronico', 'direccion', 'telefono', 'fecha_nacimiento']
        widgets = {
            'cedula_propietario': forms.NumberInput(attrs={'class':'form-control'}),  
            'nombre': forms.TextInput(attrs={'class':'form-control'}),  
            'apellido': forms.TextInput(attrs={'class':'form-control'}),  
            'correo_electronico': forms.EmailInput(attrs={'class':'form-control'}),  
            'direccion': forms.TextInput(attrs={'class':'form-control'}),  
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),  
            'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control'}),
        }

class Tipo_ProductoRegistration(forms.ModelForm):
    class Meta:
        model = Tipo_Producto
        fields = ['nombre_tipo']
        widgets = {
            'nombre_tipo': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProveedorRegistration(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['id_proveedor', 'cedula_propietario', 'nombre_proveedor', 'direccion', 'telefono', 'correo_electronico']
        widgets = {
            'id_proveedor': forms.NumberInput(attrs={'class':'form-control'}),  
            'cedula_propietario': forms.NumberInput(attrs={'class':'form-control'}),
            'nombre_proveedor': forms.TextInput(attrs={'class':'form-control'}),  
            'direccion': forms.TextInput(attrs={'class':'form-control'}),  
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),  
            'correo_electronico': forms.EmailInput(attrs={'class':'form-control'}),  
        }

class CompradorRegistration(forms.ModelForm):
    class Meta:
        model = Comprador
        fields = ['id_ciudad', 'cedula_comprador', 'nombre', 'apellido', 'correo_electronico', 'direccion', 'telefono', 'fecha_nacimiento']
        widgets = {
            'id_ciudad': forms.NumberInput(attrs={'class':'form-control'}),  
            'cedula_comprador': forms.NumberInput(attrs={'class':'form-control'}), 
            'nombre': forms.TextInput(attrs={'class':'form-control'}),  
            'apellido': forms.TextInput(attrs={'class':'form-control'}),  
            'correo_electronico': forms.EmailInput(attrs={'class':'form-control'}),  
            'direccion': forms.TextInput(attrs={'class':'form-control'}),  
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),  
            'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control'}), 
        }

class MensajeroRegistration(forms.ModelForm):
    class Meta:
        model = Mensajero
        fields = ['cedula_mensajero', 'nombre', 'apellido', 'correo_electronico', 'direccion', 'telefono', 'fecha_nacimiento']
        widgets ={
            'cedula_mensajero': forms.NumberInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),  
            'apellido': forms.TextInput(attrs={'class':'form-control'}),  
            'correo_electronico': forms.EmailInput(attrs={'class':'form-control'}),  
            'direccion': forms.TextInput(attrs={'class':'form-control'}),  
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),  
            'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control'}), 
        }

class CiudadRegistration(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['id_ciudad', 'nombre_ciudad']
        widgets = {
            'nombre_ciudad': forms.TextInput(attrs={'class':'form-control'}),  
        }

class FacturaRegistration(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['id_factura', 'id', 'cedula_comprador', 'cedula_mensajero', 'subtotal', 'iva', 'total']
        widgets = {
            'id': forms.NumberInput(attrs={'class':'form-control'}),  
            'cedula_comprador': forms.NumberInput(attrs={'class':'form-control'}),  
            'cedula_mensajero': forms.NumberInput(attrs={'class':'form-control'}),   
            'subtotal': forms.NumberInput(attrs={'class':'form-control'}),  
            'iva': forms.NumberInput(attrs={'class':'form-control'}),  
            'total': forms.NumberInput(attrs={'class':'form-control'}),  
        }

class Especificacion_FacturaRegistration(forms.ModelForm):
    class Meta:
        model = Especificacion_Factura
        fields = ['id_especificacion', 'id', 'id_factura', 'cantidad_compra', 'importe']
        widgets = {
            'id': forms.NumberInput(attrs={'class':'form-control'}),  
            'id_factura': forms.NumberInput(attrs={'class':'form-control'}),  
            'cantidad_compra': forms.NumberInput(attrs={'class':'form-control'}),  
            'importe': forms.NumberInput(attrs={'class':'form-control'}),  
        }

class TrabajadorRegistration(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['cedula_trabajador', 'id_tipo', 'nombre', 'apellido', 'correo_electronico', 'direccion', 'telefono', 'fecha_nacimiento']
        widgets = {
            'cedula_trabajador': forms.NumberInput(attrs={'class':'form-control'}),  
            'id_tipo': forms.NumberInput(attrs={'class':'form-control'}),  
            'nombre': forms.TextInput(attrs={'class':'form-control'}),  
            'apellido': forms.TextInput(attrs={'class':'form-control'}),  
            'correo_electronico': forms.EmailInput(attrs={'class':'form-control'}),  
            'direccion': forms.TextInput(attrs={'class':'form-control'}),  
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),  
            'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control'}), 
        }

class Tipo_TrabajadorRegistration(forms.ModelForm):
    class Meta:
        model = Tipo_Trabajador
        fields = ['tipo_trabajador']
        widgets = {
            'tipo_trabajador': forms.TextInput(attrs={'class':'form-control'}),  
        }

class Salario_TrabajadorRegistration(forms.ModelForm):
    class Meta:
        model = Salario_Trabajador
        fields = ['sueldo_base', 'honorarios', 'seguro_social', 'pensiones', 'sueldo_total']
        widgets = {
            'sueldo_base': forms.NumberInput(attrs={'class':'form-control'}),  
            'honorarios': forms.NumberInput(attrs={'class':'form-control'}),  
            'seguro_social': forms.NumberInput(attrs={'class':'form-control'}),  
            'pensiones': forms.NumberInput(attrs={'class':'form-control'}),  
            'sueldo_total': forms.NumberInput(attrs={'class':'form-control'}),  
        }