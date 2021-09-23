from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios') # para usar ImageField() se debe installar el modulo Pillow (pip install Pillow) // upload_to: crea una subcarpeta en la carpeta de MEDIA_URL py guarda ahi el contenido multimedia
    created = models.DateTimeField(auto_now_add=True) # Fecha que se agrega automaticamente // DateTime solo resulta en la fecha sin hora
    updated = models.DateTimeField(auto_now=True) # auto_now_add: agrega la fecha de creacio, auto_now: agrega la fecha de actualizacion.

    class Meta:  # clase para definir los parametros meta de la tabla/modelo 
        verbose_name = 'servicio' # visualizacion en el panel.
        verbose_name_plural = 'servicios'

    def __str__(self): # mostrar informacion del modelo al ser consultado mediante el shell
        return self.titulo