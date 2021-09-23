from django.db import models
from django.contrib.auth.models import User # Importando el modelo User, que guarda los usuarios del panel.

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True) # Fecha que se agrega automaticamente // DateTime solo resulta en la fecha sin hora
    updated = models.DateTimeField(auto_now=True) # auto_now_add: agrega la fecha de creacio, auto_now: agrega la fecha de actualizacion.


    class Meta:  # clase para definir los parametros meta de la tabla/modelo 
        verbose_name = 'categoria' # visualizacion en el panel.
        verbose_name_plural = 'categorias'

    def __str__(self): # mostrar informacion del modelo al ser consultado mediante el shell
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) # Fecha que se agrega automaticamente // DateTime solo resulta en la fecha sin hora
    updated = models.DateTimeField(auto_now=True) # auto_now_add: agrega la fecha de creacio, auto_now: agrega la fecha de actualizacion.
    autor = models.ForeignKey(User, on_delete=models.CASCADE) # relacion de uno a muchos, autor-post, se borran los post del autor al borrar autor.
    categoria = models.ManyToManyField(Categoria) # relacion de muchos a muchos blog-categorias


    class Meta:  # clase para definir los parametros meta de la tabla/modelo 
        verbose_name = 'post' # visualizacion en el panel.
        verbose_name_plural = 'posts'

    def __str__(self): # mostrar informacion del modelo al ser consultado mediante el shell
        return self.titulo

