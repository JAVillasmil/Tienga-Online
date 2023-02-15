from django import forms
from django.http import request
from .models import Proveedor
from tienda.models import Producto

class Proveedor_Form(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"

class Producto_Form(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
