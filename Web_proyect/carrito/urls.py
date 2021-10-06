from django.urls import path
from carrito import views

urlpatterns = [
    path('', views.carrito, name='carrito'),
]