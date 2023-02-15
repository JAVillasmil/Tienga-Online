from django.db import models
from proveedor.models import Proveedor

# Create your models here.

class Categoria_Prod(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="tienda/categoria", null=True, blank=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        db_table = "Categorias_Productos"
        verbose_name="Categoria Producto"
        verbose_name_plural="Categorias Productos"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(Categoria_Prod,on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to="tienda/producto",null=True, blank=True)
    precio = models.FloatField()
    ganancia_empresa = models.FloatField()
    ganancia_proveedor = models.FloatField()
    stock = models.PositiveIntegerField()
    stock_min = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Productos"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre