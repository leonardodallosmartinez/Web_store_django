from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField() # para usar ImageField() se debe installar el modulo Pillow (pip install Pillow)
    created = models.DateField(auto_now_add=True) # Fecha que se agrega automaticamente
    updated = models.DateField(auto_now_add=True)

    class Meta:  # clase para definir los parametros meta de la tabla/modelo 
        verbose_name = 'servicio' # isualizacion en el panel.
        verbose_name_plural = 'servicios'

    def __str__(self): # mostrar informacion del modelo al ser consultado mediante el shell
        return self.titulo