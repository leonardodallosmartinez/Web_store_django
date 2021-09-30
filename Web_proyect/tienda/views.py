from django.shortcuts import render
from .models import CategoriaProd, Producto

# Create your views here.
def tienda(request):

    productos = Producto.objects.all() # importando todo los productos guardados en la DDBB.
    return render(request, 'tienda.html', {'productos':productos})