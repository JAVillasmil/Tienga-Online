from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Proveedor as Prove
from django.contrib import messages
from tienda.models import Producto, Categoria_Prod


######## PROVEEDOR ########

def Proveedor(request):
    return render(request, "proveedor/crear_proveedor.html")

def Crear_Proveedor(request):
    proveedor = Prove.objects.all().filter(usuario_id=request.user.id)
    creado = len(proveedor)
    contexto = {"proveedor": proveedor, "creado": creado}
    if request.method == "POST":
        try:
            nombre = request.POST["nombre_proveedor"]
            cif = request.POST["cif_proveedor"]
            correo = request.POST["correo_proveedor"]
            direccion = request.POST["direccion_proveedor"]
            usuario = request.user
            Prove.objects.create(nombre=nombre,
                                 cif=cif,
                                 correo=correo,
                                 direccion=direccion,
                                 usuario=usuario)
            messages.success(request, "Provedor Guardado")
        except IntegrityError as e:
            messages.error(request, "el CIF ya existe")
        return redirect("/proveedor/Crear_Proveedor")
    else:
        return render(request, "proveedor/crear_proveedor.html", contexto)


def Visualizar_Proveedor(request):
    creado = len(Prove.objects.all().filter(usuario_id=request.user.id))
    print(creado)
    if creado > 0:
        proveedor = Prove.objects.get(usuario_id=request.user.id)
        contexto = {"proveedor": proveedor, "creado": creado}
        return render(request, "proveedor/visual_prove.html", contexto)
    else:
        proveedor = Prove.objects.all().filter(usuario_id=request.user.id)
        contexto = {"proveedor": proveedor, "creado": creado}
        return render(request, "proveedor/visual_prove.html", contexto)

def Borrar_Proveedor(request, id):
    prove = Prove.objects.get(id=id)
    prove.delete()
    messages.warning(request, "Proveedor Borrado")
    return redirect("/proveedor/Verificar_Proveedor")


def Editar_Proveedor(request, id):
    prove = Prove.objects.get(id=id)
    return render(request, 'proveedor/edit_proveedor.html', {'prove': prove})


def Actualizar_Proveedor(request, id):
    prove = Prove.objects.get(id=id)
    prove.nombre = request.POST["nombre_proveedor"]
    prove.cif = request.POST["cif_proveedor"]
    prove.correo = request.POST["correo_proveedor"]
    prove.direccion = request.POST["direccion_proveedor"]
    prove.save()
    messages.success(request, "Proveedor Actualizado")
    return render(request, 'proveedor/edit_proveedor.html', {'prove': prove})


######## PRODUCTOS ########

def Crear_Producto(request):
    prove = Prove.objects.all().filter(usuario_id=request.user.id)
    if len(prove) == 0:
        creado = 0
    else:
        creado = 1
    categoria = Categoria_Prod.objects.all()
    haycate = 1
    if len(categoria) == 0:
        haycate = 0
    contexto = {"categoria": categoria, "creado": creado,
                "prove": prove, "haycate": haycate}
    if request.method == "POST":
        nombre = request.POST["nombre_producto"]
        id_categoria = request.POST["categoria_producto"]
        categorias = Categoria_Prod.objects.get(id=id_categoria)
        proveedor = Prove.objects.get(usuario_id=request.user.id)
        imagen = request.FILES.get("imagen_producto")
        precio = request.POST["precio_producto"]
        precio_reci = float(precio)
        if precio_reci <= 100:
            comision_crea = 0.15
        if 100 < precio_reci <= 1000:
            comision_crea = 0.12
        if precio_reci > 1000:
            comision_crea = 0.08
        ganancia_empresa = round((precio_reci * comision_crea), 2)
        ganancia_proveedor = round((precio_reci - ganancia_empresa), 2)
        stock = request.POST["stock_producto"]
        stock_min = int(stock) * 0.1
        if stock_min < 1:
            stock_min = 1
        descripcion = request.POST["descripcion_producto"]
        Producto.objects.create(nombre=nombre,
                                categorias=categorias,
                                proveedor=proveedor,
                                ganancia_empresa=ganancia_empresa,
                                ganancia_proveedor=ganancia_proveedor,
                                imagen=imagen,
                                precio=precio,
                                stock_min=stock_min,
                                stock=stock,
                                descripcion=descripcion)

        messages.success(request, "Producto Guardado")
    return render(request, "producto/creado_producto.html", contexto)


def Visualizar_Productos_Proveedor(request):
    try:
        proveedor = Prove.objects.get(usuario_id=request.user.id)
        productos = Producto.objects.all().filter(proveedor_id=proveedor.id)
        creado = 1
        contexto = {"productos": productos, "creado": creado}
    except:
        creado = 0
        contexto = {"creado": creado}
    return render(request, "producto/visual_productos_proveedor.html", contexto)



def Borrar_Producto(request, id):
    product = Producto.objects.get(id=id)
    product.delete()
    return redirect("/proveedor/Verificar_Productos")




def Editar_Producto(request, id):
    product = Producto.objects.get(id=id)
    categoria = Categoria_Prod.objects.all()
    contexto = {'product': product, "categoria": categoria}
    return render(request, 'producto/edit_producto.html', contexto)


def Actualizar_Producto(request, id):
    product = Producto.objects.get(id=int(id))
    nombre = request.POST["nombre_producto"]
    if nombre is "":
        pass
    else:
        product.nombre = request.POST["nombre_producto"]
        product.save()
    categoria = request.POST["categoria_producto"]
    if categoria is "":
        pass
    else:
        categoria = (request.POST["categoria_producto"])
        categoria = Categoria_Prod.objects.get(id=categoria)
        product.categorias = categoria
        product.save()
    imagen = request.FILES.get("imagen_producto")
    if imagen is None:
        pass
    else:
        product.imagen = request.FILES.get("imagen_producto")
        product.save()
    precio = request.POST["precio_producto"]
    if precio is "":
        pass
    else:
        product.precio = float(request.POST["precio_producto"])
        precio_reci = product.precio
        if precio_reci <= 100:
            comision_edi = 0.15
        if 100 < precio_reci <= 1000:
            comision_edi = 0.12
        if precio_reci > 1000:
            comision_edi = 0.08
        ganancia_empresa = round((precio_reci * comision_edi), 2)
        ganancia_proveedor = round((precio_reci - ganancia_empresa), 2)
        product.ganancia_empresa = round(ganancia_empresa, 2)
        product.ganancia_proveedor = round(ganancia_proveedor, 2)
        product.save()

    stock = request.POST["stock_producto"]
    if stock is "":
        pass
    else:
        product.stock = int(request.POST["stock_producto"])
        product.stock_min = int(request.POST["stock_producto"]) * 0.1
        if product.stock_min < 1:
            product.stock_min = 1
        product.save()
    descripcion = request.POST["descripcion_producto"]
    if descripcion is "":
        pass
    else:
        product.descripcion = request.POST["descripcion_producto"]
        product.save()
    categoria = Categoria_Prod.objects.all()
    messages.success(request, "Producto Actualizado")
    contexto = {'product': product, "categoria": categoria}
    return render(request, 'producto/edit_producto.html', contexto)

