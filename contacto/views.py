from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib import messages


# Create your views here.
def Contacto(request):
    if request.method == "POST":
        nombre = request.POST["nombre_contacto"]
        email = request.POST["correo_contacto"]
        contenido = request.POST["contenido_contacto"]
        print("/////////////////////", nombre, email, contenido)
        email = EmailMessage(" Mensaje desde Gestión de Pedidos -- PFJV",
                             "Usuario: {}\n"
                             "Correo: {}\n"
                             "Contenido:\n"
                             "{}".format(nombre,
                                         email,
                                         contenido),
                             "", ["djangoyayo@gmail.com"], reply_to=[email])
        try:
            email.send()
            messages.success(request, "Mensaje Enviado")
        except:
            messages.error(request, "No se ha podido enviar")
    return render(request, "contacto/contacto.html")
