# Ceando clase para controlar el carrito de compras, uso de sesiones
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')

        if not carrito: # verifica si no existe el carrito, si no existe crea uno nuevo.
            carrito = self.session['carrito'] = {}
        # else:
        #     self.carrito = carrito
        self.carrito = carrito # de esta manera se asegura que se cree la variable carrito.

    def agregar(self, producto): #Agregar productos al carrito, si el producto ya esta agregado no se vuelve a agregar, solo se aumenta su cantidad. Todos los valores de un producto del carrito se dejan como string a excepcion de la cantidad.
        if (str(producto.id) not in self.carrito.keys()): # condicional si el producto no esta en el carro.
            self.carrito[producto.id] = {
                'producto_id' : producto.id,
                'nombre' : producto.nombre,
                'precio' : str(producto.precio),
                'cantidad' : 1,
                'imagen' : producto.imagen.url
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad'] + 1
                    value['precio'] = float(value['precio'])+(producto.precio)
                    break
        self.guardar_carrito() # guarda el carrito modificado en session.

    def guardar_carrito(self): # guarda el carrito en la variable session
        self.session['carrito'] = self.carrito
        self.session.modified = True # Para que surja efecto la instruccion anterior. | no es necesario si se hace usando la clave de la sesion.

    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar_carrito()

    def restar_producto(self, producto):
        for key, value in self.carrito.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad'] - 1
                    value['precio'] = float(value['precio'])-(producto.precio)
                    if value['cantidad'] < 1: # condicional para eliminar el producto si la cantidad es 1 al querer restar.
                        self.eliminar(producto)
                    break
        self.guardar_carrito()

    def limpiar_carrito(self):
        self.session['carrito'] = {}
        self.session.modified = True # Para que surja efecto la instruccion anterior. | no es necesario si se hace usando la clave de la sesion.