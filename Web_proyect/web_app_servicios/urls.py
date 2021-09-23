from django.urls import path
from web_app_servicios import views

urlpatterns = [
    path('', views.servicios , name="servicios"), # el parametro name es opcional
    #path('servicios/', views.servicios, name="servicios"),
]