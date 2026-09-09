from enum import Enum

from app.models.client import Client
from app.models.sale_detail import SaleDetail


class SaleStatus(Enum):
    PENDIENTE = "PENDIENTE"
    PAGADA = "PAGADA"
    CANCELADA = "CANCELADA"
    ENTREGADA = "ENTREGADA"


class Sale:
    def __init__(
        self,
        id: int,
        cliente: Client,
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
        self.estado = SaleStatus.PENDIENTE

    def agregar_detalle(self, detalle: SaleDetail) -> None:
        # Validar
        if detalle is None:
            raise ValueError("Error, detalle vacio")
        if not isinstance(detalle, SaleDetail):
            raise ValueError("Error, detalle invalido")
        self.detalles.append(detalle)

    def calcular_total(self) -> float:
        total = sum(detalle.subtotal for detalle in self.detalles)
        return total

    def pagar(self) -> None:
        if self.estado != SaleStatus.PENDIENTE:
            raise ValueError("Error, la venta no puede ser pagada")

        self.estado = SaleStatus.PAGADA

    def cancelar(self) -> None:
        if self.estado != SaleStatus.PENDIENTE:
            raise ValueError("Error, la venta no puede ser cancelada")

        self.estado = SaleStatus.CANCELADA

    def entregar(self) -> None:
        if self.estado != SaleStatus.PAGADA:
            raise ValueError("Error, la venta no puede ser entregada")

        self.estado = SaleStatus.ENTREGADA
