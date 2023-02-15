from django.db.models import Sum
from django.shortcuts import render, redirect
from pedidos.models import Pedido, Linea_Pedido
from carro.carro import Carro
from django.contrib import messages
from clientes.models import Cliente
from tienda.models import Producto
from .models import Pedido, Linea_Pedido
from proveedor.models import Proveedor as Prove
from django.conf import settings
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.db.models import Sum, Count

# SECCION PEDIDOS

def Carro_Detallado(request):
    perfiles = Cliente.objects.all().filter(usuario_id=request.user.id)
    if len(perfiles) == 0:
        creado = 0
    else:
        creado = 1
    contexto = {"creado": creado}
    return render(request, "cliente/carro_detallado.html", contexto)


def Select_Perfil(request):
    todos_perfiles = Cliente.objects.all().filter(usuario_id=request.user.id)
    contexto = {"todos_perfiles": todos_perfiles}
    if request.method == "POST":
        perfil = request.POST["select_perfil"]
        buscado = Cliente.objects.all().filter(id=perfil)
        contexto = {"todos_perfiles": todos_perfiles, "buscado": buscado}
    return render(request, "cliente/select_perfil.html", contexto)


def Procesar_Pedido(request, id):
    # GENERACION DE PEDIDO A UN CLIENTE
    cliente = Cliente.objects.get(id=id)
    carro = Carro(request)
    total_list = []
    for key, value in carro.carro.items():
        precio_cantidad = value["precio_cantidad"]
        total_list.append(precio_cantidad)
    total = sum(total_list)
    pedido = Pedido.objects.create(cliente=cliente, total_pedido=total)
    # GENERACION DE LAS LINEAS DEL PEDIDO DE LOS DIFERENTES ELEMENTOS.
    list_pedido = []
    for key, value in carro.carro.items():  # CREADO DE LISTADO DE PRODUCTOS PARA PEDIDOS
        cantidad_product = value["cantidad"]
        producto = Producto.objects.get(id=key)
        ganancia_empresa = round(int(cantidad_product) * float(producto.ganancia_empresa), 2)
        ganancia_proveedor = round(int(cantidad_product) * float(producto.ganancia_proveedor), 2)
        total_producto = round(int(cantidad_product) * float(producto.precio), 2)
        # CREADO DE LISTA DE LINEAS DE PEDIDOS
        list_pedido.append(Linea_Pedido(
            producto=Producto.objects.get(id=key),
            cantidad=cantidad_product,
            pedido=Pedido.objects.get(id=pedido.id),
            total_producto=total_producto,
            total_proveedor=ganancia_proveedor,
            total_empresa=ganancia_empresa,
        ))
        # ACTUALIZACIÓN DEL STOCK
        producto.stock = int(producto.stock) - int(cantidad_product)
        producto.save()
        # ALERTA STOCK MIN
        stock_min = producto.stock_min
        if producto.stock <= stock_min:  # ENVIADO DE ALERTA EMAIL
            nombre_producto = producto.nombre
            id_producto = producto.proveedor_id
            proveedor = Prove.objects.get(id=id_producto)
            proveedor_nombre = proveedor.nombre
            email = proveedor.correo
            email = str(email)
            contenido = """
            Estimado {}, \n \n
            Su producto {} ha llegado a su stock min, 
            agradecemos de reponer el mismo lo antes posible.\n

            Para ello debe logearse, e ir a su apartado de PRODUCTOS AGREGADOS,
            EDITADO DE PRODUCTO, y actualizar el stock del cual dispondremos, \n
            Muchas Gracias
            """.format(proveedor_nombre, nombre_producto)
            contenido = str(contenido)
            try:
                send_mail(
                    'ALERTA - Producto ha llegado a su min de stock',
                    contenido,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=True
                )
            except:
                nombre = proveedor_nombre
                email = proveedor.correo
                contenido = "Se requiere revision por parte del proveedor."
                email = EmailMessage(" PROVEEDOR CON CORREO ERONEO",
                                     "Proveedr: {}\n"
                                     "Correo: {} fallido\n"
                                     "Contenido:\n"
                                     "{}".format(nombre,
                                                 email,
                                                 contenido),
                                     "", ["djangoyayo@gmail.com"], reply_to=[email])
                email.send()
        else:
            pass
    # CREADO DE LINEA DE PEDIDO POR LISTADO
    Linea_Pedido.objects.bulk_create(list_pedido)
    carro.Limpiado()
    messages.success(request, "El pedidos se ha creado correctamente.")
    return redirect("/pedidos/Pedido_Detalle")

# SECCION CLIENTES

def Visualizar_Pedidos_Clientes(request):
    perfiles = Cliente.objects.all().filter(usuario_id=request.user)
    todos_pedidos = Pedido.objects.filter(cliente_id__usuario_id=request.user.id).order_by('created').reverse()
    nombre_perfil = "Todos"
    cantidad = len(todos_pedidos)
    labels = ["Total pedidos"]
    for p in perfiles:
        labels.append(p.nombre)
    data = [len(todos_pedidos)]
    pedidos_perfil = todos_pedidos.values('cliente_id').annotate(Count('id')).order_by()
    print(pedidos_perfil)
    for perfil in pedidos_perfil:
        cliente_pedido_count = perfil.get('id__count')
        data.append(cliente_pedido_count)
    creado = 1
    if cantidad == 0:
        creado = 0
    contexto = {"todos_pedidos": todos_pedidos, "perfiles": perfiles, "nombre_perfil": nombre_perfil,
                "cantidad": cantidad, "creado": creado, "labels":labels, "data":data}
    if request.method == "POST":
        if request.POST["select_perfil"] == "Todos":
            pass
        else:
            perfil = int(request.POST["select_perfil"])
            nombre_perfil = Cliente.objects.get(id=perfil).nombre
            todos_pedidos = Pedido.objects.all().filter(cliente_id=perfil).order_by('created').reverse()
            cantidad = len(todos_pedidos)
            contexto = {"todos_pedidos": todos_pedidos, "perfiles": perfiles, "nombre_perfil": nombre_perfil,
                        "cantidad": cantidad, "creado": creado, "labels":labels, "data":data}

    return render(request, "cliente/visual_pedidos_realizados.html", contexto)


def Detalle_Linea_Pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    detalle = Linea_Pedido.objects.all().filter(pedido_id=pedido.id)
    total_list = []
    for det in detalle:
        cantidad = det.cantidad
        precio = det.producto.precio
        total = cantidad * precio
        total_list.append(total)
    total_list = sum(total_list)
    contexto = {"pedido": pedido, "detalle": detalle, "total_list": total_list}
    return render(request, "cliente/visual_pedidos_detalle.html", contexto)

# SECCION PROVEEDOR

def Visualizar_Ventas(request):
    productos = Producto.objects.all().filter(proveedor_id__usuario=request.user)
    lineas_venta = Linea_Pedido.objects.all().filter(producto_id__proveedor_id__usuario=request.user)
    total_list = []
    todas_lineas = lineas_venta.values('producto_id').annotate(cantidad_vendida=Sum('cantidad'))
    comision = "N/A"
    label = []
    list_data = []
    data = []
    for lineas in todas_lineas:
        id = lineas.get('producto_id')
        cantidad_producto = lineas.get('cantidad_vendida')
        producto = Producto.objects.get(id=id)
        ganancia_producto = round((cantidad_producto * producto.ganancia_proveedor), 2)
        total_list.append(ganancia_producto)
        label.append(producto.nombre)
    list_data = total_list
    ganancia = round(sum(total_list),2)
    for li in list_data:
        data.append((str(li)).replace(",",".")) #problemas de formato con la grafica en floatante , por .
    # TOP 5 VENDIDOS
    top_5 = lineas_venta.values('producto_id').annotate(
        cantidad_vendida=Sum('cantidad')).order_by('cantidad_vendida').reverse()[:5]
    for prod in top_5:  # agregado de nombre en el diccionario.
        id = prod.get('producto_id')
        nombre_producto = Producto.objects.get(id=id).nombre
        prod["nombre"] = nombre_producto
    lineas_venta = lineas_venta.order_by('created')
    cantidad = len(lineas_venta)
    producto_buscado = "Todos Tus Productos"
    if request.method == "POST":
        if request.POST["select_product"] == "Todos":
            pass
        else:  # Producto en Especifico
            total_list = []
            id_buscado = request.POST["select_product"]
            lineas_venta = Linea_Pedido.objects.all().filter(producto_id=id_buscado)
            cantidad = len(lineas_venta)
            todas_lineas = lineas_venta.values('producto_id').annotate(cantidad_vendida=Sum('cantidad'))
            for lineas in todas_lineas:
                id = lineas.get('producto_id')
                cantidad_producto = lineas.get('cantidad_vendida')
                producto = Producto.objects.get(id=id)
                producto_buscado = producto.nombre
                ganancia_producto = round((cantidad_producto * producto.ganancia_proveedor), 2)
                comision = round(((producto.ganancia_empresa / producto.precio) * 100), 2)
                total_list.append(ganancia_producto)
            ganancia = sum(total_list)
    contexto = {"top_5": top_5, "lineas_venta": lineas_venta, "producto_buscado": producto_buscado,
                "productos": productos, "cantidad": cantidad, "ganancia": ganancia, "comision": comision,
                "label":label, "data":data}
    return render(request, "proveedor/visualizar_ventas.html", contexto)
