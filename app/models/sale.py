from app.models.client import Client
from app.models.sale_detail import SaleDetail


class Sale:
    def __init__(
            self,
            id:int,
            cliente:Client,
    ):
        if id <= 0:
            raise ValueError("Error, id invalido")
        if cliente is None:
            raise ValueError("Error, cliente vacio")
        if not isinstance(cliente, Client):
            raise ValueError("Error, cliente invalido")

        self.id = id
        self.cliente = cliente
        self.detalles = []

    def agregar_detalle(self, detalle:SaleDetail) -> None:
        #Validar
        if detalle is None:
            raise ValueError("Error, detalle vacio")
        if not isinstance(detalle, SaleDetail):
            raise ValueError("Error, detalle invalido")
        self.detalles.append(detalle)

    def calcular_total(self) -> float:
        total= sum(detalle.subtotal for detalle in self.detalles)
        return total

    