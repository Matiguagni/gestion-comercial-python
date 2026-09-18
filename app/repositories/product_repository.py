from app.models.product import Product


class ProductRepository:
    def __init__(self):
        self.productos = {}

    def guardar(self, producto: Product) -> None:
        if producto is None:
            raise ValueError("Error, producto vacio")
        
        if not isinstance(producto, Product):
            raise ValueError("Error, producto invalido")

        self.productos[producto.id] = producto

    def obtener_por_id(self, id:int) -> Product | None:
        if id <= 0:
            raise ValueError("Error, id invalido")
        if id in self.productos:
            return self.productos[id]
        return None
        

    def listar(self) -> list[Product]:
        return list(self.productos.values())
        

    def eliminar(self, id:int) -> None:
        if id <= 0:
            raise ValueError("Error, id invalido")

        if id not in self.productos:
            raise ValueError("Error, producto inexistente")

        del self.productos[id]
