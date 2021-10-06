from django.shortcuts import render
from .carrito import Carrito #importando la clase que me controla el carrito
from tienda.models import Producto, CategoriaProd
from django.shortcuts import redirect # clase importada para hacer redireccionamiento a una pagina especifica.

# Create your views here.
def carrito(request):
    return render(request, 'carrito.html')

def agregar_producto(request, producto_id):
    carrito = Carrito(request) #creo el carrito, exista o no.
    producto = Producto.objects.get(id=producto_id) #obtengo el producto a agregar de la DDBB de acuerdo a el producto_id
    carrito.agregar(producto=producto) # agrego una unidad de producto al carrito

    return redirect('tienda.html') # redirecciono a la pagina tienda, que es de donde envie la solicitud de agregar al carrito.

def eliminar_producto(request, producto_id):
    carrito = Carrito(request) #creo el carrito, exista o no.
    producto = Producto.objects.get(id=producto_id) #obtengo el producto a agregar de la DDBB de acuerdo a el producto_id
    carrito.eliminar(producto=producto) # elimino el producto al carrito

    return redirect('tienda.html') # redirecciono a la pagina tienda, que es de donde envie la solicitud al carrito.

def restar_producto(request, producto_id):
    carrito = Carrito(request) #creo el carrito, exista o no.
    producto = Producto.objects.get(id=producto_id) #obtengo el producto a agregar de la DDBB de acuerdo a el producto_id
    carrito.restar_producto(producto=producto) # resto una unidad de producto al carrito

    return redirect('tienda.html') # redirecciono a la pagina tienda, que es de donde envie la solicitud al carrito.

def limpiar_carrito(request):
    carrito = Carrito(request) #creo el carrito, exista o no.
    carrito.limpiar_carrito() # Vacio el carrito

    return redirect('tienda.html') # redirecciono a la pagina tienda, que es de donde envie la solicitud al carrito.

