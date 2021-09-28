from django.shortcuts import render, HttpResponse

from web_app_servicios.models import Servicio # importando modelos de la aplicacaion web_app_servicios para mostrarlos en una plantilla

# Create your views here.
def home(request):

    return render(request, "home.html")
    # return HttpResponse("home")
