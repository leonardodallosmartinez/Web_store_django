from django.urls import path
from web_app_servicios import views

urlpatterns = [
    path('', views.home_ser , name="home_serv"), # el parametro name es opcional
    
]