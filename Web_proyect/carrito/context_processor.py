from .carrito import Carrito

def importe_total_carrito(request):
    carrito = Carrito(request)
    total = 0
    # if request.user.is_authenticated: # se usara cuando se cree un sistema de autentificación.
    for key, value in request.session['carrito'].items():
        total = total + float(value['precio'])
    return {"importe_total_carrito":total}