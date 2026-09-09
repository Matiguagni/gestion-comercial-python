import pytest

from app.models.client import Client
from app.models.product import Product
from app.models.sale import Sale, SaleStatus
from app.models.sale_detail import SaleDetail


@pytest.fixture
def cliente1():
    return Client(
        id=123,
        dni="44123456",
        nombre_completo="Pepe Messi",
        email="pepe@gmail.com",
        direccion="calle falsa 123",
        codigo_postal="3500",
    )


@pytest.fixture
def venta1(cliente1):
    return Sale(id=1, cliente=cliente1)


def test_sale_valido(cliente1, venta1):
    assert venta1.id == 1
    assert venta1.cliente == cliente1
    assert venta1.detalles == []
    assert venta1.estado == SaleStatus.PENDIENTE


@pytest.fixture
def mouse():
    return Product(
        id=123, nombre="Mouse", precio=20000, stock=10, categoria="Perifericos"
    )


@pytest.fixture
def teclado():
    return Product(
        id=234,
        nombre="Teclado",
        precio=50000,
        stock=10,
        categoria="Perifericos",
    )


@pytest.fixture
def detalle_mouse(mouse):
    return SaleDetail(producto=mouse, cantidad=2)


@pytest.fixture
def detalle_teclado(teclado):
    return SaleDetail(producto=teclado, cantidad=1)


def test_agregar_detalle(venta1, detalle_mouse, detalle_teclado):
    venta1.agregar_detalle(detalle_mouse)
    venta1.agregar_detalle(detalle_teclado)
    assert venta1.detalles == [detalle_mouse, detalle_teclado]


def test_calcular_total(venta1, detalle_mouse, detalle_teclado):
    venta1.agregar_detalle(detalle_mouse)
    venta1.agregar_detalle(detalle_teclado)

    total = venta1.calcular_total()
    assert total == 90000


def test_calcular_total_sin_detalles(venta1):
    assert venta1.calcular_total() == 0


@pytest.mark.parametrize(
    "campo, valor, mensaje",
    [
        ("id", -20, "Error, id invalido"),
        ("id", 0, "Error, id invalido"),
        ("cliente", None, "Error, cliente vacio"),
        ("cliente", "Pedro", "Error, cliente invalido"),
        ("cliente", 123, "Error, cliente invalido"),
    ],
)
def test_sale_constructor_invalido(cliente1, campo, valor, mensaje):
    datos = {"id": 1, "cliente": cliente1}
    datos[campo] = valor

    with pytest.raises(ValueError, match=mensaje):
        Sale(**datos)


@pytest.mark.parametrize(
    "detalle, mensaje",
    [
        (None, "Error, detalle vacio"),
        ("Mouse", "Error, detalle invalido"),
        (123, "Error, detalle invalido"),
    ],
)
def test_agregar_detalle_invalido(venta1, detalle, mensaje):
    with pytest.raises(ValueError, match=mensaje):
        venta1.agregar_detalle(detalle)


def test_pagar_valido(venta1):
    venta1.pagar()
    assert venta1.estado == SaleStatus.PAGADA


def test_cancelar_valido(venta1):
    venta1.cancelar()
    assert venta1.estado == SaleStatus.CANCELADA


def test_entregar_valido(venta1):
    venta1.pagar()
    venta1.entregar()
    assert venta1.estado == SaleStatus.ENTREGADA


def test_pagar_invalido(venta1):
    venta1.cancelar()
    with pytest.raises(
        ValueError, match="Error, la venta no puede ser pagada"
    ):
        venta1.pagar()
    assert venta1.estado == SaleStatus.CANCELADA


def test_cancelar_invalido(venta1):
    venta1.pagar()
    with pytest.raises(
        ValueError, match="Error, la venta no puede ser cancelada"
    ):
        venta1.cancelar()
    assert venta1.estado == SaleStatus.PAGADA


def test_entregar_invalido(venta1):
    with pytest.raises(
        ValueError, match="Error, la venta no puede ser entregada"
    ):
        venta1.entregar()
    assert venta1.estado == SaleStatus.PENDIENTE
