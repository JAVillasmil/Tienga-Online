from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import Producto

# Create your views here.

def Agregar_Producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.Agrega_1(producto=producto)
    return redirect("Tienda")

def Eliminar_Producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.Eliminado(producto=producto)
    return redirect("Tienda")

def Restar_Producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.Restado_1(producto=producto)
    return redirect("Tienda")

######### Para redirect de cliente

def Agregar_Producto_Cliente(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.Agrega_1(producto=producto)
    return redirect("/pedidos/Pedido_Detalle")

def Eliminar_Producto_Cliente(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.Eliminado(producto=producto)
    return redirect("/pedidos/Pedido_Detalle")

def Restar_Producto_Cliente(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.Restado_1(producto=producto)
    return redirect("/pedidos/Pedido_Detalle")

def Limpiar_Carro_Cliente(request):
    carro = Carro(request)
    carro.Limpiado()
    return redirect("/pedidos/Pedido_Detalle")