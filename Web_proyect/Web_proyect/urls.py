from django.contrib import admin
from django.urls import path, include
from web_app import views

from django.conf import settings # Importar la ruta del contenido multimedia
from django.conf.urls.static import static # Importe para usar metodos de los archivos estaticos para contenido multimedia

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #path('web_app/', include('web_app.urls')), #se ingresa con web_app/names
    path('', include('web_app.urls')), #se ingresa sin nombre de la app
    path('web_servicios/', include('web_app_servicios.urls')), #llama las urls de la seunda aplicacion
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # Añadir la ruta del contenido multimedia.