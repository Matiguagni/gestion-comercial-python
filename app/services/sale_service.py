from app.models.sale import Sale, SaleStatus


class SaleService:
    def confirmar_venta(self, venta:Sale) -> None:
        if venta is None:
            raise ValueError("Error, venta vacia")
        
        if not isinstance(venta, Sale):
            raise ValueError("Error, venta invalida")

        if venta.estado != SaleStatus.PENDIENTE:
            raise ValueError("Error, estado invalido")

        if not venta.detalles:
            raise ValueError("Error, venta sin detalles")

        # 1. Validamos todos los productos, que haya stock, se interrumpe
        # si algun producto no cuenta con el stock
        cant_por_producto = {}        
        for detalle in venta.detalles:
            producto = detalle.producto
            producto_id = producto.id
            # Comprobamos que no exista dicha clave en nuestro diccionario
            # para crearla
            if producto_id not in cant_por_producto:
                cant_por_producto[producto_id] = {
                    "producto": producto,
                    "cantidad": 0,
                }
            # Si nuestra clave existe (id), directamente
            # se acumula la cantidad
            cant_por_producto[producto_id]["cantidad"] += detalle.cantidad

        for producto_id, datos in cant_por_producto.items():
            producto = datos["producto"]
            cantidad_total = datos["cantidad"]
            if cantidad_total > producto.stock:
                raise ValueError("Error, stock insuficiente")

        # 2. Recien si TODOS son validos, modificamos dicho stock
        for producto_id, datos in cant_por_producto.items():
            producto = datos["producto"]
            cantidad_total = datos["cantidad"]
            producto.reducir_stock(cantidad_total)

        # 3. Confirmamos el estado de la venta
        venta.pagar()
