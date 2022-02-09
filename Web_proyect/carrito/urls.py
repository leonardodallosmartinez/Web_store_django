from django.urls import path
from carrito import views

app_name = 'carrito' #namespace para llamar este conjunto de urls. || app_name: nombre de variable reservado para asignar namespace.

urlpatterns = [
    #path('', views.carrito, name='carrito'),
    path('agregar/<int:producto_id>', views.agregar_producto, name='agregar'),
    path('eliminar/<int:producto_id>', views.eliminar_producto , name='eliminar'),
    path('restar/<int:producto_id>', views.restar_producto, name='restar'),
    path('limpiar/', views.limpiar_carrito, name='limpiar'),
]