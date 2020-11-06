from django.core import validators
from django import forms
from .models import Product, Propietario

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