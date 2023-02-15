from django.contrib.auth.models import User
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "Clientes"
        verbose_name="Cliente"
        verbose_name_plural="Clientes"

    def __str__(self):
        return"{}".format(self.nombre)
