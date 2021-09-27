from django.shortcuts import render
from contacto.forms import Formulario_contacto

# Create your views here.
def contacto(request):
    formulario_contacto = Formulario_contacto()

    return render(request, 'contacto.html', {'formulario_contacto':formulario_contacto})