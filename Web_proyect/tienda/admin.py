from django.contrib import admin
from tienda import models

class CategoriaProdAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    search_fields = ('nombre', 'created', 'updated')
    readonly_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'imagen', 'precio', 'disponibilidad')
    search_fields = ('nombre', 'categoria', 'imagen', 'precio', 'disponibilidad')
    readonly_fields = ('created', 'updated')


# Register your models here.
admin.site.register(models.CategoriaProd, CategoriaProdAdmin)
admin.site.register(models.Producto, ProductoAdmin)