from django.contrib import admin
from .models import Cliente

# Register your models here.
class Cliente_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Cliente, Cliente_Admin)
