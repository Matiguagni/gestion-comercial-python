import pytest

from app.models.client import Client
from app.models.product import Product
from app.models.sale import Sale, SaleStatus
from app.models.sale_detail import SaleDetail
from app.services.sale_service import SaleService


@pytest.fixture
def cliente():
    return Client(
        id=123,
        dni="44123456",
        nombre_completo="Pepe Messi",
        email="pepe@gmail.com",
        direccion="calle falsa 123",
        codigo_postal="3500",
    )


@pytest.fixture
def mouse():
    return Product(
        id=1234,
        nombre="mouse",
        precio=30000,
        stock=100,
        categoria="Perifericos",
    )


@pytest.fixture
def mouse_sin_stock():
    return Product(
        id=1234, nombre="mouse", precio=30000, stock=1, categoria="Perifericos"
    )


@pytest.fixture
def teclado():
    return Product(
        id=2345,
        nombre="teclado",
        precio=50000,
        stock=80,
        categoria="Perifericos",
    )


@pytest.fixture
def detalle_mouse(mouse):
    return SaleDetail(producto=mouse, cantidad=2)


@pytest.fixture
def detalle_mouse_sin_stock(mouse_sin_stock):
    return SaleDetail(producto=mouse_sin_stock, cantidad=2)


@pytest.fixture
def detalle_teclado(teclado):
    return SaleDetail(producto=teclado, cantidad=3)


@pytest.fixture
def venta(cliente, detalle_mouse, detalle_teclado):
    venta = Sale(id=123, cliente=cliente)
    venta.agregar_detalle(detalle_mouse)
    venta.agregar_detalle(detalle_teclado)
    return venta


@pytest.fixture
def venta_sin_stock(cliente, detalle_mouse_sin_stock, detalle_teclado):
    venta = Sale(id=123, cliente=cliente)
    venta.agregar_detalle(detalle_mouse_sin_stock)
    venta.agregar_detalle(detalle_teclado)
    return venta


@pytest.fixture
def venta_cancelada(cliente, detalle_mouse, detalle_teclado):
    venta = Sale(id=123, cliente=cliente)
    venta.agregar_detalle(detalle_mouse)
    venta.agregar_detalle(detalle_teclado)
    venta.cancelar()
    return venta


@pytest.fixture
def venta_sin_detalles(cliente):
    venta = Sale(id=123, cliente=cliente)
    return venta


@pytest.fixture
def sale_service():
    return SaleService()


def test_confirmar_venta_valida(sale_service, venta, mouse, teclado):
    sale_service.confirmar_venta(venta)
    assert mouse.stock == 98
    assert teclado.stock == 77
    assert venta.estado == SaleStatus.PAGADA


def test_confimar_venta_stock_insuficiente(
    sale_service, venta_sin_stock, mouse_sin_stock, teclado
):
    with pytest.raises(ValueError, match="Error, stock insuficiente"):
        sale_service.confirmar_venta(venta_sin_stock)
    assert mouse_sin_stock.stock == 1
    assert teclado.stock == 80
    assert venta_sin_stock.estado == SaleStatus.PENDIENTE


@pytest.mark.parametrize(
    "venta_invalida, mensaje",
    [
        (None, "Error, venta vacia"),
        ("Venta", "Error, venta invalida"),
        (123, "Error, venta invalida"),
    ],
)
def test_confirmar_venta_invalida(sale_service, venta_invalida, mensaje):
    with pytest.raises(ValueError, match=mensaje):
        sale_service.confirmar_venta(venta_invalida)


def test_confirmar_venta_estado_invalido(sale_service, venta_cancelada):
    with pytest.raises(ValueError, match="Error, estado invalido"):
        sale_service.confirmar_venta(venta_cancelada)
    assert venta_cancelada.estado == SaleStatus.CANCELADA


def test_confirmar_venta_sin_detalles(sale_service, venta_sin_detalles):
    with pytest.raises(ValueError, match="Error, venta sin detalles"):
        sale_service.confirmar_venta(venta_sin_detalles)
    assert venta_sin_detalles.estado == SaleStatus.PENDIENTE
