from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('Crear_Perfil', Crear_Perfil, name="Crear_Perfil"),
    path('Verificar_Perfil', views.Visualizar_Perfil, name="Verificar_Perfil"),
    path('Borrar_Perfil/<int:id>', Borrar_Perfil, name="Borrar_Perfil"),



    path('Editar_Perfil/<int:id>', Editar_Perfil, name="Editar_Perfil"),
    path('Actualizar_Perfil/<int:id>', Actualizar_Perfil, name="Actualizar_Perfil"),
]
