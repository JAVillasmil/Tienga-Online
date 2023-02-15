from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('Pedido_Detalle', Carro_Detallado, name="Pedido_Detalle"),
    path('Select_Perfil', Select_Perfil, name="Select_Perfil"),
    path('Procesar_Pedido/<int:id>', views.Procesar_Pedido, name="Procesar_Pedido"),
    path('Verificar_Pedidos', Visualizar_Pedidos_Clientes, name="Verificar_Pedidos"),
    path('Detalle_Linea_Pedido/<int:id>', views.Detalle_Linea_Pedido, name="Detalle_Linea_Pedido"),
    path('Verificar_Ventas', views.Visualizar_Ventas, name="Verificar_Ventas"),
]
