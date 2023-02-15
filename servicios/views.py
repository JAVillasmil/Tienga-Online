from django.shortcuts import render
from tienda.models import *

# Create your views here.

def Servicios(request):
    categoria = Categoria_Prod.objects.all()
    creado = 1
    if len(categoria) == 0:
        creado = 0
    contexto = {"categoria": categoria, "creado": creado}
    return render(request, "servicios/mostrar_categorias.html", contexto)


def Productos_Categoria(request, id):
    categoria = Categoria_Prod.objects.get(id=id)
    productos = Producto.objects.all().filter(categorias=id)
    contexto = {"categoria": categoria, "productos": productos}
    return render(request, "servicios/productos_por_categorias.html", contexto)
