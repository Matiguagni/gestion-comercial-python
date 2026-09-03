from app.models.product import Product


class SaleDetail:
    def __init__(self, producto:Product, cantidad:int):
        #Comprobamos que el objeto exista
        if producto is None:
            raise ValueError("Error, producto nulo")
        #Comprobamos que corresponda a un product valido
        if not isinstance(producto, Product):
            raise ValueError("Error, producto invalido")
        if cantidad <= 0:
            raise ValueError("Error, cantidad invalida")
        
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = producto.precio
        self.subtotal = self.precio_unitario * cantidad
