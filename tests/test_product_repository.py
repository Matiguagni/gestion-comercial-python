import pytest

from app.models.product import Product
from app.repositories.product_repository import ProductRepository


@pytest.fixture
def repository():
    return ProductRepository()


@pytest.fixture
def mouse():
    return Product(
        id=1,
        nombre="Mouse",
        precio=30000,
        stock=100,
        categoria="Perifericos",
    )


@pytest.fixture
def teclado():
    return Product(
        id=2,
        nombre="Teclado",
        precio=30000,
        stock=5,
        categoria="Perifericos",
    )


def test_repository_inicia_vacio(repository):
    assert repository.listar() == []


def test_guardar_producto(repository, mouse):
    repository.guardar(mouse)

    producto = repository.obtener_por_id(mouse.id)

    assert producto == mouse


def test_obtener_producto_inexistente(repository):
    producto = repository.obtener_por_id(999)

    assert producto is None


def test_listar_productos(repository, teclado, mouse):
    repository.guardar(mouse)
    repository.guardar(teclado)

    productos = repository.listar()

    assert productos == [mouse, teclado]


def test_eliminar_producto(repository, mouse):
    repository.guardar(mouse)
    repository.eliminar(mouse.id)

    assert repository.obtener_por_id(mouse.id) is None


def test_eliminar_producto_inexistente(repository):
    with pytest.raises(ValueError, match="Error, producto inexistente"):
        repository.eliminar(9999)


@pytest.mark.parametrize(
    "producto_invalido, mensaje",
    [
        (None, "Error, producto vacio"),
        (123, "Error, producto invalido"),
        ("Mouse", "Error, producto invalido"),
    ],
)
def test_guardar_producto_invalido(producto_invalido, mensaje, repository):
    with pytest.raises(ValueError, match=mensaje):
        repository.guardar(producto_invalido)


@pytest.mark.parametrize(
    "id_invalido",
    [0, -123, -1],
)
def test_obtener_por_id_invalido(repository, id_invalido):
    with pytest.raises(ValueError, match="Error, id invalido"):
        repository.obtener_por_id(id_invalido)


@pytest.mark.parametrize(
    "id_invalido",
    [0, -1, -100],
)
def test_eliminar_id_invalido(repository, id_invalido):
    with pytest.raises(ValueError, match="Error, id invalido"):
        repository.eliminar(id_invalido)
