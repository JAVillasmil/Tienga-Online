from django.contrib import admin
from .models import Linea_Pedido, Pedido


class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ['created']

class Linea_PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ['created']


admin.site.register(Pedido,PedidoAdmin)
admin.site.register(Linea_Pedido,Linea_PedidoAdmin)