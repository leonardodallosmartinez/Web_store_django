from django.urls import path
from contacto import views

urlpatterns = [
    path('', views.contacto, name="contacto"), # el parametro name es opcional   
]