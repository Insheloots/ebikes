from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    #Index y vistas de productos
    path('admin/', admin.site.urls),
    path('', views.add_show, name="addproduct" ),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),

    #Vistas de propietario
    path('propietarios/', views.add_propietario, name="addpropietario" ),
    path('propietarios/delete/<int:cedula_propietario>/', views.delete_propietario, name="deletepropietario"),
    path('propietarios/<int:cedula_propietario>/', views.update_propietario, name="updatepropietario"),

    #Vistas de tipo de producto
    path('tipoproducto/', views.add_tipoproducto, name="addtipoproducto" ),
    path('tipoproducto/delete/<int:id_tipo>/', views.delete_tipoproducto, name="deletetipoproducto"),
    path('tipoproducto/<int:id_tipo>/', views.update_tipoproducto, name="updatetipoproducto"),

    #Vistas de Proveedor
    path('proveedor/', views.add_proveedor, name="addproveedor" ),
    path('proveedor/delete/<int:id_proveedor>/', views.delete_proveedor, name="deleteproveedor"),
    path('proveedor/<int:id_proveedor>/', views.update_proveedor, name="updateproveedor"),

    #Vistas de Comprador
    path('comprador/', views.add_comprador, name="addcomprador" ),
    path('comprador/delete/<int:cedula_comprador>/', views.delete_comprador, name="deletecomprador"),
    path('comprador/<int:cedula_comprador>/', views.update_comprador, name="updatecomprador"),

    #Vistas de Mensajeros
    path('mensajero/', views.add_mensajero, name="addmensajero" ),
    path('mensajero/delete/<int:cedula_mensajero>/', views.delete_mensajero, name="deletemensajero"),
    path('mensajero/<int:cedula_mensajero>/', views.update_mensajero, name="updatemensajero"),

    #Vistas de ciudad
    path('ciudad/', views.add_ciudad, name="addciudad" ),
    path('ciudad/delete/<int:id_ciudad>/', views.delete_ciudad, name="deleteciudad"),
    path('ciudad/<int:id_ciudad>/', views.update_ciudad, name="updateciudad"),
]
