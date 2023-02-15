from django.urls import path
from .views import *

urlpatterns = [
    path('VRegistro_cliente',VRegistro_cliente.as_view(), name="VRegistro_cliente"),
    path('Autenticacion_prov', VRegistro_prov.as_view(), name="Autenticacion_prov"),
    path('Cerrar_Sesion',Cerrar_Sesion, name="Cerrar_Sesion"),
    path('Logear', Logear, name="Logear"),
]
