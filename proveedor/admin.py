from django.contrib import admin
from .models import Proveedor

# Register your models here.

class Proveedor_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Proveedor, Proveedor_Admin)
