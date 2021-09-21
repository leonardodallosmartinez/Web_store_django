from django.contrib import admin
from web_app_servicios import models

class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido', 'imagen', 'created', 'updated')
    search_fields = ('titulo', 'contenido', 'imagen', 'created', 'updated')
    readonly_fields = ('created', 'updated')



# Register your models here.
admin.site.register(models.Servicio, ServiciosAdmin)