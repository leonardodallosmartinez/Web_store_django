from django.shortcuts import render
from web_app_servicios.models import Servicio # importando modelos de la aplicacaion web_app_servicios para mostrarlos en una plantilla

# Create your views here.
def home_ser(request):

    return render(request, 'home_serv.html')

def servicios(request):

    servicios = Servicio.objects.all() # Importnado todos los servicios guardados en la tabla Servicios de la DDBB

    return render(request, 'servicios.html', {'servicios': servicios})