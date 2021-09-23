from django.contrib import admin
from blog import models


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','created', 'updated')
    search_fields = ('nombre', 'created', 'updated')
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido', 'imagen', 'created', 'updated')
    search_fields = ('titulo', 'contenido', 'created', 'updated')
    readonly_fields = ('created', 'updated')

# Register your models here.
admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Post, PostAdmin)
