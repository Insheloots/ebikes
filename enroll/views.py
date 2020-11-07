from django.shortcuts import render, HttpResponseRedirect
from .forms import ProductRegistration, PropietarioRegistration, Tipo_ProductoRegistration, PropietarioRegistration, ProveedorRegistration, CompradorRegistration, MensajeroRegistration, CiudadRegistration, FacturaRegistration, Especificacion_FacturaRegistration, TrabajadorRegistration, Tipo_TrabajadorRegistration, Salario_TrabajadorRegistration
from .models import Product, Propietario, Tipo_Producto, Propietario, Proveedor, Comprador, Mensajero, Ciudad, Factura, Especificacion_Factura, Trabajador, Tipo_Trabajador, Salario_Trabajador

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


#----Vistas de tipos de productos----
#Esta función agrega y muestra elementos de la tabla tipos de productos
def add_tipoproducto(request):
    if request.method == 'POST':
        fm = Tipo_ProductoRegistration(request.POST)
        if fm.is_valid():
            nt = fm.cleaned_data['nombre_tipo']
            reg = Tipo_Producto(nombre_tipo=nt)
            reg.save()
            fm = Tipo_ProductoRegistration()
    else:
        fm = Tipo_ProductoRegistration()
    tipoproducto_add = Tipo_Producto.objects.all()
    return render(request, 'enroll/addtipoproducto.html', {'form':fm, 'tipoproducto':tipoproducto_add})

#Esta función actualiza los datos de la malparida tabla
def update_tipoproducto(request, id_tipo):
    if request.method == 'POST':
        pi = Tipo_Producto.objects.get(pk=id_tipo)
        fm = Tipo_ProductoRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Tipo_Producto.objects.get(pk=id_tipo)
        fm = Tipo_ProductoRegistration(instance=pi)
    return render(request, 'enroll/updatetipoproducto.html', {'form':fm})

#Esta función elimina elementos de la tabla productos
def delete_tipoproducto(request, id_tipo):
    if request.method == 'POST':
        pi = Tipo_Producto.objects.get(pk=id_tipo)
        pi.delete()
        return HttpResponseRedirect('/tipoproducto')

#----Vistas de Proveedor----
def add_proveedor(request):
    if request.method == 'POST':
        fm = ProveedorRegistration(request.POST)
        if fm.is_valid():
            ip = fm.cleaned_data['id_proveedor']
            cp = fm.cleaned_data['cedula_propietario']
            np = fm.cleaned_data['nombre_proveedor']
            di = fm.cleaned_data['direccion']
            te = fm.cleaned_data['telefono']
            ce = fm.cleaned_data['correo_electronico']
            reg = Proveedor(id_proveedor=ip, cedula_propietario=cp, nombre_proveedor=np, direccion=di, telefono=te, correo_electronico=ce)
            reg.save()
            fm = ProveedorRegistration()
    else:
        fm = ProveedorRegistration()
    proveedor_add = Proveedor.objects.all()
    return render(request, 'enroll/addproveedor.html', {'form':fm, 'proveedor':proveedor_add})


def update_proveedor(request, id_proveedor):
    if request.method == 'POST':
        pi = Proveedor.objects.get(pk=id_proveedor)
        fm = ProveedorRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Proveedor.objects.get(pk=id_proveedor)
        fm = ProveedorRegistration(instance=pi)
    return render(request, 'enroll/updateproveedor.html', {'form':fm})


def delete_proveedor(request, id_proveedor):
    if request.method == 'POST':
        pi = Proveedor.objects.get(pk=id_proveedor)
        pi.delete()
        return HttpResponseRedirect('/proveedor')


#----Vistas de Comprador----
def add_comprador(request):
    if request.method == 'POST':
        fm = CompradorRegistration(request.POST)
        if fm.is_valid():
            ic = fm.cleaned_data['id_ciudad']
            cc = fm.cleaned_data['cedula_comprador']
            nm = fm.cleaned_data['nombre']
            ap = fm.cleaned_data['apellido']
            ce = fm.cleaned_data['correo_electronico']
            di = fm.cleaned_data['direccion']
            te = fm.cleaned_data['telefono']
            fn = fm.cleaned_data['fecha_nacimiento']
            reg = Comprador(id_ciudad = ic, cedula_comprador=cc, nombre=nm, apellido=ap, correo_electronico=ce, direccion=di, telefono=te, fecha_nacimiento=fn)
            reg.save()
            fm = CompradorRegistration()
    else:
        fm = CompradorRegistration()
    comprador_add = Comprador.objects.all()
    return render(request, 'enroll/addcomprador.html', {'form':fm, 'comprador':comprador_add})


def update_comprador(request, cedula_comprador):
    if request.method == 'POST':
        pi = Comprador.objects.get(pk=cedula_comprador)
        fm = CompradorRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Comprador.objects.get(pk=cedula_comprador)
        fm = CompradorRegistration(instance=pi)
    return render(request, 'enroll/updatecomprador.html', {'form':fm})


def delete_comprador(request, cedula_comprador):
    if request.method == 'POST':
        pi = Comprador.objects.get(pk=cedula_comprador)
        pi.delete()
        return HttpResponseRedirect('/comprador')


#----Vistas de mensajero----
def add_mensajero(request):
    if request.method == 'POST':
        fm = MensajeroRegistration(request.POST)
        if fm.is_valid():
            cm = fm.cleaned_data['cedula_mensajero']
            nm = fm.cleaned_data['nombre']
            ap = fm.cleaned_data['apellido']
            ce = fm.cleaned_data['correo_electronico']
            di = fm.cleaned_data['direccion']
            te = fm.cleaned_data['telefono']
            fn = fm.cleaned_data['fecha_nacimiento']
            reg = Mensajero(cedula_mensajero=cm, nombre=nm, apellido=ap, correo_electronico=ce, direccion=di, telefono=te, fecha_nacimiento=fn)
            reg.save()
            fm = MensajeroRegistration()
    else:
        fm = MensajeroRegistration()
    mensajero_add = Mensajero.objects.all()
    return render(request, 'enroll/addmensajero.html', {'form':fm, 'mensajero':mensajero_add})


def update_mensajero(request, cedula_mensajero):
    if request.method == 'POST':
        pi = Mensajero.objects.get(pk=cedula_mensajero)
        fm = MensajeroRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Mensajero.objects.get(pk=cedula_mensajero)
        fm = MensajeroRegistration(instance=pi)
    return render(request, 'enroll/updatemensajero.html', {'form':fm})


def delete_mensajero(request, cedula_mensajero):
    if request.method == 'POST':
        pi = Mensajero.objects.get(pk=cedula_mensajero)
        pi.delete()
        return HttpResponseRedirect('/mensajero')


#----Vistas de ciudad----
def add_ciudad(request):
    if request.method == 'POST':
        fm = CiudadRegistration(request.POST)
        if fm.is_valid():
            nc = fm.cleaned_data['nombre_ciudad']
            reg = Ciudad(nombre_ciudad=nc)
            reg.save()
            fm = CiudadRegistration()
    else:
        fm = CiudadRegistration()
    ciudad_add = Ciudad.objects.all()
    return render(request, 'enroll/addciudad.html', {'form':fm, 'ciudad':ciudad_add})

def update_ciudad(request, id_ciudad):
    if request.method == 'POST':
        pi = Ciudad.objects.get(pk=id_ciudad)
        fm = CiudadRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Ciudad.objects.get(pk=id_ciudad)
        fm = CiudadRegistration(instance=pi)
    return render(request, 'enroll/updateciudad.html', {'form':fm})

def delete_ciudad(request, id_ciudad):
    if request.method == 'POST':
        pi = Ciudad.objects.get(pk=id_ciudad)
        pi.delete()
        return HttpResponseRedirect('/ciudad')


#----Vistas de Factura----
def add_factura(request):
    if request.method == 'POST':
        fm = FacturaRegistration(request.POST)
        if fm.is_valid():
            ip = fm.cleaned_data['id']
            cc = fm.cleaned_data['cedula_comprador']
            cm = fm.cleaned_data['cedula_mensajero']
            fe = fm.cleaned_data['fecha_emision']
            sb = fm.cleaned_data['subtotal']
            iv = fm.cleaned_data['iva']
            tt = fm.cleaned_data['total']
            reg = Factura(id=ip, cedula_comprador=cc, cedula_mensajero=cm, fecha_emision=fe, subtotal=sb, iva=iv, total=tt)
            reg.save()
            fm = FacturaRegistration()
    else:
        fm = FacturaRegistration()
    factura_add = Factura.objects.all()
    return render(request, 'enroll/addfactura.html', {'form':fm, 'factura':factura_add})

def update_factura(request, id_factura):
    if request.method == 'POST':
        pi = Factura.objects.get(pk=id_factura)
        fm = FacturaRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Factura.objects.get(pk=id_factura)
        fm = FacturaRegistration(instance=pi)
    return render(request, 'enroll/updatefactura.html', {'form':fm})

def delete_factura(request, id_factura):
    if request.method == 'POST':
        pi = Factura.objects.get(pk=id_factura)
        pi.delete()
        return HttpResponseRedirect('/factura')


#----Vistas de Especificación de Factura----
def add_especificacionfactura(request):
    if request.method == 'POST':
        fm = Especificacion_FacturaRegistration(request.POST)
        if fm.is_valid():
            ie = fm.cleaned_data['id_especificacion']
            ip = fm.cleaned_data['id']
            ic = fm.cleaned_data['id_factura']
            cc = fm.cleaned_data['cantidad_compra']
            im = fm.cleaned_data['importe']
            reg = Especificacion_Factura(id_especificacion=ie, id=ip, id_factura=ic, cantidad_compra=cc, importe=im)
            reg.save()
            fm = Especificacion_FacturaRegistration()
    else:
        fm = Especificacion_FacturaRegistration()
    especificacionfactura_add = Especificacion_Factura.objects.all()
    return render(request, 'enroll/addespecificacionfactura.html', {'form':fm, 'especificacionfactura':especificacionfactura_add})

def update_especificacionfactura(request, id_especificacion):
    if request.method == 'POST':
        pi = Especificacion_Factura.objects.get(pk=id_especificacion)
        fm = Especificacion_FacturaRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Especificacion_Factura.objects.get(pk=id_especificacion)
        fm = Especificacion_FacturaRegistration(instance=pi)
    return render(request, 'enroll/updateespecificacionfactura.html', {'form':fm})

def delete_especificacionfactura(request, id_especificacion):
    if request.method == 'POST':
        pi = Especificacion_Factura.objects.get(pk=id_especificacion)
        pi.delete()
        return HttpResponseRedirect('/especificacionfactura')


#----Vistas de Trabajador----
def add_trabajador(request):
    if request.method == 'POST':
        fm = TrabajadorRegistration(request.POST)
        if fm.is_valid():
            ct = fm.cleaned_data['cedula_trabajador']
            ia = fm.cleaned_data['id_salario']
            it = fm.cleaned_data['id_tipo']
            nm = fm.cleaned_data['nombre']
            ap = fm.cleaned_data['apellido']
            ce = fm.cleaned_data['correo_electronico']
            di = fm.cleaned_data['direccion']
            te = fm.cleaned_data['telefono']
            fn = fm.cleaned_data['fecha_nacimiento']
            reg = Trabajador(cedula_trabajador=ct, id_salario=ia, id_tipo=it, nombre=nm, apellido=ap, correo_electronico=ce, direccion=di, telefono=te, fecha_nacimiento=fn)
            reg.save()
            fm = TrabajadorRegistration()
    else:
        fm = TrabajadorRegistration()
    trabajador_add = Trabajador.objects.all()
    return render(request, 'enroll/addtrabajador.html', {'form':fm, 'trabajador':trabajador_add})


def update_trabajador(request, cedula_trabajador):
    if request.method == 'POST':
        pi = Trabajador.objects.get(pk=cedula_trabajador)
        fm = TrabajadorRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Trabajador.objects.get(pk=cedula_trabajador)
        fm = TrabajadorRegistration(instance=pi)
    return render(request, 'enroll/updatetrabajador.html', {'form':fm})


def delete_trabajador(request, cedula_trabajador):
    if request.method == 'POST':
        pi = Trabajador.objects.get(pk=cedula_trabajador)
        pi.delete()
        return HttpResponseRedirect('/trabajador')


#----Vistas de Tipo trabajador----
def add_tipotrabajador(request):
    if request.method == 'POST':
        fm = Tipo_TrabajadorRegistration(request.POST)
        if fm.is_valid():
            tp = fm.cleaned_data['tipo_trabajador']
            reg = Tipo_Trabajador(tipo_trabajador=tp)
            reg.save()
            fm = Tipo_TrabajadorRegistration()
    else:
        fm = Tipo_TrabajadorRegistration()
    tipotrabajador_add = Tipo_Trabajador.objects.all()
    return render(request, 'enroll/addtipotrabajador.html', {'form':fm, 'tipotrabajador':tipotrabajador_add})

def update_tipotrabajador(request, id_tipo):
    if request.method == 'POST':
        pi = Tipo_Trabajador.objects.get(pk=id_tipo)
        fm = Tipo_TrabajadorRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Tipo_Trabajador.objects.get(pk=id_tipo)
        fm = Tipo_TrabajadorRegistration(instance=pi)
    return render(request, 'enroll/updatetipotrabajador.html', {'form':fm})

def delete_tipotrabajador(request, id_tipo):
    if request.method == 'POST':
        pi = Tipo_Trabajador.objects.get(pk=id_tipo)
        pi.delete()
        return HttpResponseRedirect('/tipotrabajador')


#----Vistas de Salarios----
def add_salario(request):
    if request.method == 'POST':
        fm = Salario_TrabajadorRegistration(request.POST)
        if fm.is_valid():
            ia = fm.cleaned_data['id_salario']
            sb = fm.cleaned_data['sueldo_base']
            ho = fm.cleaned_data['honorarios']
            ss = fm.cleaned_data['seguro_social']
            pe = fm.cleaned_data['pensiones']
            st = fm.cleaned_data['sueldo_total']
            reg = Salario_Trabajador(id_salario=ia, sueldo_base=sb, honorarios=ho, seguro_social=ss, pensiones=pe, sueldo_total=st)
            reg.save()
            fm = Salario_TrabajadorRegistration()
    else:
        fm = Salario_TrabajadorRegistration()
    salario_add = Salario_Trabajador.objects.all()
    return render(request, 'enroll/addsalario.html', {'form':fm, 'salario':salario_add})

def update_salario(request, id_salario):
    if request.method == 'POST':
        pi = Salario_Trabajador.objects.get(pk=id_salario)
        fm = Salario_TrabajadorRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Salario_Trabajador.objects.get(pk=id_salario)
        fm = Salario_TrabajadorRegistration(instance=pi)
    return render(request, 'enroll/updatesalario.html', {'form':fm})

def delete_salario(request, id_salario):
    if request.method == 'POST':
        pi = Salario_Trabajador.objects.get(pk=id_salario)
        pi.delete()
        return HttpResponseRedirect('/salario')