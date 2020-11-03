from django.shortcuts import render, HttpResponseRedirect
from .forms import ProductRegistration
from .models import Product

#Esta función agrega y muestra elementos de la tabla productos
def add_show(request):
    if request.method == 'POST':
        fm = ProductRegistration(request.POST)
        if fm.is_valid():
            np = fm.cleaned_data['nombre_producto']
            cp = fm.cleaned_data['cantidad_producto']
            dp = fm.cleaned_data['descripcion_producto']
            pu = fm.cleaned_data['precio_unit']
            reg = Product(nombre_producto=np, cantidad_producto=cp, descripcion_producto=dp, precio_unit=pu)
            reg.save()
            fm = ProductRegistration()
    else:
        fm = ProductRegistration()
    prod = Product.objects.all()
    return render(request, 'enroll/addproduct.html', {'form':fm, 'pro':prod})
#Esta función actualiza los datos de la malparida tabla
def update_data(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        fm = ProductRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Product.objects.get(pk=id)
        fm = ProductRegistration(instance=pi)
    return render(request, 'enroll/updateproduct.html', {'form':fm})

#Esta función elimina elementos de la tabla productos
def delete_data(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')