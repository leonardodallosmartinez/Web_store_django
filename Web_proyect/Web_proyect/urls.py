from django.contrib import admin
from django.urls import path, include
from web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #path('web_app/', include('web_app.urls')), #se ingresa con web_app/names
    path('', include('web_app.urls')), #se ingresa sin nombre de la app
    path('web_servicios/', include('web_app_servicios.urls')), #llama las urls de la seunda aplicacion
]
