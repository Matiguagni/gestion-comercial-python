class Product:
    def __init__(
        self, id: int, nombre: str, precio: float, stock: int, categoria: str
    ):
        if id <= 0:
            raise ValueError(
                "Error, el id no puede iniciar con valor menor o igual a 0"
            )
        if not nombre.strip():
            raise ValueError("Error, nombre de producto vacio")
        if precio <= 0:
            raise ValueError("Error, formato de precio incorrecto")
        if stock <= 0:
            raise ValueError("Error, cantidad de stock incorrecta")
        if not categoria.strip():
            raise ValueError("Error, categoria vacia")
        # A posterior podria comprobarse si pertenece a la lista de categorias.

        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def reducir_stock(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("Error, la cantidad debe ser 100%")
        if self.stock < cantidad:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad

    def actualizar_precio(self, nuevo_precio: float) -> None:
        if nuevo_precio <= 0:
            raise ValueError("Valor incorrecto")
        self.precio = nuevo_precio

    def cambiar_categoria(self, categoria: str) -> None:
        self.categoria = categoria

    def aplicar_descuento(self, descuento: int) -> None:
        if not 0 < descuento <= 100:
            raise ValueError("El descuento debe ser entre 1% y 100%")

        valor_descuento = self.precio * (descuento / 100)
        self.precio -= valor_descuento
