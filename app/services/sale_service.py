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
        for detalle in venta.detalles:
            if detalle.cantidad > detalle.producto.stock:
                raise ValueError("Error, stock insuficiente")

        # 2. Recien si TODOS son validos, modificamos dicho stock
        for detalle in venta.detalles:
            detalle.producto.reducir_stock(detalle.cantidad)

        # 3. Confirmamos el estado de la venta
        venta.pagar()
