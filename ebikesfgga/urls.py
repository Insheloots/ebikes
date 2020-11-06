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
]
