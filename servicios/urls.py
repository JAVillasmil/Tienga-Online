from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.Servicios, name="Servicios"),
    path('Productos_Categoria/<int:id>', Productos_Categoria, name="Productos_Categoria"),
]