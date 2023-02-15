from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    cif = models.CharField(max_length=9, unique=True)
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "Proveedor"
        verbose_name="Proveedor"
        verbose_name_plural="Proveedores"

    def __str__(self):
        return" {} ".format(self.nombre)
5