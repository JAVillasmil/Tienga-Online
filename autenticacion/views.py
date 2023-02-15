from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
class VRegistro_cliente(View):
    def get(self, request):
        dirigido = "cliente"
        form = UserCreationForm()
        contexto = {"form": form, "dirigido": dirigido}
        return render(request, "autenticacion/registro.html", contexto)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            group = Group.objects.get(name='Clientes')#Grupo, debe estar creado_previamente por admin
            usuario.groups.add(group)
            login(request, usuario)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.warning(request, form.error_messages[msg])
            return render(request, "autenticacion/registro.html", {"form": form})


class VRegistro_prov(View):
    def get(self, request):
        dirigido = "proveedor"
        form = UserCreationForm()
        contexto = {"form": form, "dirigido": dirigido}
        return render(request, "autenticacion/registro.html", contexto)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            group = Group.objects.get(name='Proveedor')#Grupo, debe estar creado_previamente por admin
            usuario.groups.add(group)
            login(request, usuario)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.warning(request, form.error_messages[msg])
            return render(request, "autenticacion/registro.html", {"form": form})


def Cerrar_Sesion(request):
    logout(request)
    return redirect('Home')


def Logear(request):
    if request.method == "POST":
        nombre_usuario = request.POST["usuario"]
        contra = request.POST["password"]
        usuario = authenticate(username=nombre_usuario, password=contra)
        if usuario is not None:
            login(request, usuario)
            return redirect('Home')
        else:
            messages.warning(request, "Usuario no valido")
    return render(request, "autenticacion/login.html")
