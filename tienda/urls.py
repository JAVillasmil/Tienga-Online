from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('',views.Tienda, name="Tienda"),
    path('Conocer_Proveedor/<int:id>', Conocer_Proveedor, name="Conocer_Proveedor"),
]