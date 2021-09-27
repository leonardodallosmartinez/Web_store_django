from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name="blog"), # el parametro name es opcional
    path('categoria/<int:categoria_id>', views.categoria, name="categoria"), # parametro categoria_id de la tabla categorias llevarlo en la peticion
]