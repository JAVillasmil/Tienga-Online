from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.Proveedor, name="Proveedor"),
    # PROVEEDOR
    path('Crear_Proveedor', Crear_Proveedor, name="Crear_Proveedor"),
    path('Verificar_Proveedor', views.Visualizar_Proveedor, name="Verificar_Proveedor"),
    path('Borrar_Proveedor/<int:id>', Borrar_Proveedor, name="Borrar_Proveedor"),
    path('Editar_Proveedor/<int:id>', Editar_Proveedor, name="Editar_Proveedor"),
    path('Actualizar_Proveedor/<int:id>', Actualizar_Proveedor, name="Actualizar_Proveedor"),

    # PRODUCTO
    path('Crear_Producto', Crear_Producto, name="Crear_Producto"),
    path('Verificar_Productos', views.Visualizar_Productos_Proveedor, name="Verificar_Productos"),
    path('Borrar_Producto/<int:id>', Borrar_Producto, name="Borrar_Producto"),
    path('Editar_Producto/<int:id>', Editar_Producto, name="Editar_Producto"),
    path('Actualizar_Producto/<int:id>', Actualizar_Producto, name="Actualizar_Producto"),

]
