from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.

def Crear_Perfil(request):
    if request.method == "POST":
        nombre = request.POST["nombre_perfil"]
        apellido = request.POST["apellido_perfil"]
        correo = request.POST["correo_perfil"]
        direccion = request.POST["direccion_perfil"]
        usuario = request.user
        Cliente.objects.create(nombre=nombre,
                               apellido=apellido,
                               correo=correo,
                               direccion=direccion,
                               usuario=usuario)
        messages.success(request, "Perfil Guardado")
    return render(request, "clientes/crear_cliente.html")


def Visualizar_Perfil(request):
    perfiles = Cliente.objects.all().filter(usuario_id=request.user.id)
    if len(perfiles) == 0: #condicional para mostrado de html.
        creado = 0
    else:
        creado = 1
    contexto = {"perfiles": perfiles, "creado": creado}
    return render(request, "clientes/visual_cliente.html", contexto)


def Borrar_Perfil(request, id):
    client = Cliente.objects.get(id=id)
    client.delete()
    return redirect("/clientes/Verificar_Perfil")


def Editar_Perfil(request, id):
    perfil = Cliente.objects.get(id=id)
    print(perfil.nombre)
    return render(request, 'clientes/editar_cliente.html', {'perfil': perfil})


def Actualizar_Perfil(request, id):
    perfil = Cliente.objects.get(id=id)
    perfil.nombre = request.POST["nombre_perfil"]
    perfil.apellido = request.POST["apellido_perfil"]
    perfil.correo = request.POST["correo_perfil"]
    perfil.direccion = request.POST["direccion_perfil"]
    perfil.save()
    messages.success(request, "Perfil Actualizado")
    return render(request, 'clientes/editar_cliente.html', {'perfil': perfil})
