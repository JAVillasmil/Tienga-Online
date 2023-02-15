from django.shortcuts import render
from .models import Producto
from proveedor.models import Proveedor as Prove


# Create your views here.

def Tienda(request):
    productos = Producto.objects.all()
    creado = 1
    if len(productos) == 0:
        creado = 0
    contexto = {"productos": productos, "creado": creado}
    return render(request, "tienda/tienda.html", contexto)


def Conocer_Proveedor(request, id):
    prove = Prove.objects.get(id=id)
    return render(request, "tienda/proveedor_y_productos.html", {'prove': prove})
