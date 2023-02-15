from django.urls import path
from . import views
from .views import Limpiar_Carro_Cliente

app_name = "carro"

urlpatterns = [
    path('Agregar_Producto/<int:producto_id>', views.Agregar_Producto, name="Agregar_Producto"),
    path('Eliminar_Producto/<int:producto_id>', views.Eliminar_Producto, name="Eliminar_Producto"),
    path('Restar_Producto/<int:producto_id>', views.Restar_Producto, name="Restar_Producto"),
    ########## carro detallado
    path('Agregar_Producto_Cliente/<int:producto_id>', views.Agregar_Producto_Cliente, name="Agregar_Producto_Cliente"),
    path('Eliminar_Producto_Cliente/<int:producto_id>', views.Eliminar_Producto_Cliente, name="Eliminar_Producto_Cliente"),
    path('Restar_Producto_Cliente/<int:producto_id>', views.Restar_Producto_Cliente, name="Restar_Producto_Cliente"),
    path('Limpiar_Carro_Cliente/', Limpiar_Carro_Cliente, name="Limpiar_Carro_Cliente"),
]
