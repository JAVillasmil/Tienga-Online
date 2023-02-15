from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente
from tienda.models import Producto
from proveedor.models import Proveedor

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    total_pedido = models.FloatField()

    class Meta:
        db_table = "Pedido"
        verbose_name = "pedidos"
        verbose_name_plural = "pedidos"
        ordering = ["id"]


class Linea_Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    total_producto = models.FloatField()
    total_proveedor = models.FloatField()
    total_empresa = models.FloatField()
    cantidad = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Lineas_Pedidos"
        verbose_name = "Linea Pedido"
        verbose_name_plural = "Linea Pedidos"
        ordering = ["id"]
