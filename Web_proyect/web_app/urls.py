from django.urls import path
from web_app import views

urlpatterns = [
    path('', views.home, name="home"), # el parametro name es opcional
    path('tienda/', views.tienda, name="tienda"),
    path('blog/', views.blog, name="blog"),
    path('contacto/', views.contacto, name="contacto"),
]