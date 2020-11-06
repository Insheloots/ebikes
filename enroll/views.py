from django.shortcuts import render, HttpResponseRedirect
from .forms import ProductRegistration, PropietarioRegistration
from .models import Product, Propietario

#----Vistas de productos----
#Esta función agrega y muestra elementos de la tabla productos
def add_show(request):
    if request.method == 'POST':
        fm = ProductRegistration(request.POST)
        if fm.is_valid():
            it = fm.cleaned_data['id_tipo']
            ip = fm.cleaned_data['id_proveedor']
            np = fm.cleaned_data['nombre_producto']
            cp = fm.cleaned_data['cantidad_producto']
            dp = fm.cleaned_data['descripcion_producto']
            pu = fm.cleaned_data['precio_unit']
            reg = Product(id_tipo=it, id_proveedor=ip, nombre_producto=np, cantidad_producto=cp, descripcion_producto=dp, precio_unit=pu)
            reg.save()
            fm = ProductRegistration()
    else:
        fm = ProductRegistration()
    productos = Product.objects.all()
    return render(request, 'enroll/addproduct.html', {'form':fm, 'producto':productos})

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


#----Vistas de propietarios----
#Esta función agrega y muestra elementos de la tabla propietario
def add_propietario(request):
    if request.method == 'POST':
        fm = PropietarioRegistration(request.POST)
        if fm.is_valid():
            cp = fm.cleaned_data['cedula_propietario']
            nm = fm.cleaned_data['nombre']
            ap = fm.cleaned_data['apellido']
            ce = fm.cleaned_data['correo_electronico']
            di = fm.cleaned_data['direccion']
            te = fm.cleaned_data['telefono']
            fn = fm.cleaned_data['fecha_nacimiento']
            reg = Propietario(cedula_propietario=cp, nombre=nm, apellido=ap, correo_electronico=ce, direccion=di, telefono=te, fecha_nacimiento=fn)
            reg.save()
            fm = PropietarioRegistration()
    else:
        fm = PropietarioRegistration()
    propietario_add = Propietario.objects.all()
    return render(request, 'enroll/addpropietario.html', {'form':fm, 'propietario':propietario_add})

#Esta función actualiza los datos de la malparida tabla
def update_propietario(request, cedula_propietario):
    if request.method == 'POST':
        pi = Propietario.objects.get(pk=cedula_propietario)
        fm = PropietarioRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Propietario.objects.get(pk=cedula_propietario)
        fm = PropietarioRegistration(instance=pi)
    return render(request, 'enroll/updatepropietario.html', {'form':fm})

#Esta función elimina elementos de la tabla productos
def delete_propietario(request, cedula_propietario):
    if request.method == 'POST':
        pi = Propietario.objects.get(pk=cedula_propietario)
        pi.delete()
        return HttpResponseRedirect('/propietarios')