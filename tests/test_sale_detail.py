import pytest

from app.models.product import Product
from app.models.sale_detail import SaleDetail


@pytest.fixture
def mouse():
    return Product(
        id=123, nombre="Mouse", precio=20000, stock=10, categoria="Perifericos"
    )


@pytest.fixture
def sale_detail(mouse):
    return SaleDetail(producto=mouse, cantidad=2)


def test_sale_detail_valido(sale_detail, mouse):
    assert sale_detail.producto == mouse
    assert sale_detail.cantidad == 2
    assert sale_detail.precio_unitario == 20000
    assert sale_detail.subtotal == 40000


@pytest.mark.parametrize(
    "campo, valor, mensaje",
    [
        ("producto", None, "Error, producto nulo"),
        ("producto", "Mouse", "Error, producto invalido"),
        ("producto", 1234, "Error, producto invalido"),
        ("cantidad", 0, "Error, cantidad invalida"),
        ("cantidad", -1, "Error, cantidad invalida"),
        ("cantidad", -10, "Error, cantidad invalida"),
    ],
)
def test_sale_detail_constructor_invalido(mouse, campo, valor, mensaje):
    datos = {
        "producto": mouse,
        "cantidad": 2,
    }
    datos[campo] = valor

    with pytest.raises(ValueError, match=mensaje):
        SaleDetail(**datos)
