from django.core import validators
from django import forms
from .models import Product

class ProductRegistration(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nombre_producto', 'cantidad_producto', 'descripcion_producto','precio_unit']
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad_producto': forms.NumberInput(attrs={'class':'form-control'}),
            'descripcion_producto': forms.TextInput(attrs={'class':'form-control'}),
            'precio_unit': forms.NumberInput(attrs={'class':'form-control'}),
        }