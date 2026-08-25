import pytest

from app.models.product import Product


@pytest.fixture
def product():
    return Product(
        id=1,
        nombre="Mouse",
        precio=20000,
        stock=10,
        categoria="Perifericos",
    )


def test_reducir_stock(product):
    product.reducir_stock(2)
    assert product.stock == 8


def test_reducir_stock_insuficiente(product):
    with pytest.raises(ValueError, match="Stock insuficiente"):
        product.reducir_stock(15)
    assert product.stock == 10


def test_reducir_stock_cantidad_invalida(product):
    with pytest.raises(ValueError):
        product.reducir_stock(-1)
    assert product.stock == 10


def test_cambiar_precio(product):
    product.actualizar_precio(25000)
    assert product.precio == 25000


def test_aplicar_descuento(product):
    product.aplicar_descuento(10)
    assert product.precio == 18000


def test_actualizar_precio_negativo(product):
    with pytest.raises(ValueError, match="Valor incorrecto"):
        product.actualizar_precio(-100)
    assert product.precio == 20000


def test_aplicar_descuento_invalido(product):
    with pytest.raises(
        ValueError, match="El descuento debe ser entre 1% y 100%"
    ):
        product.aplicar_descuento(101)
    assert product.precio == 20000
