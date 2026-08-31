import pytest

from app.models.client import Client


@pytest.fixture
def client():
    return Client(
        id=123,
        dni="12345678",
        nombre_completo="Matias Raigg",
        email="mat@gmail.com",
        direccion="Calle falsa 123",
        codigo_postal="3500",
    )


def test_cliente_valido(client):
    assert client.nombre_completo == "Matias Raigg"
    assert client.email == "mat@gmail.com"
    assert client.dni == "12345678"
    assert client.id == 123
    assert client.codigo_postal == "3500"
    assert client.direccion == "Calle falsa 123"


# TEST CONSTRUCTOR INVALIDO
def test_cliente_id_invalido():
    with pytest.raises(
        ValueError,
        match="Error, el id no puede iniciar con valor menor o igual a 0",
    ):
        Client(
            id=0,
            dni="12345678",
            nombre_completo="Matias Raigg",
            email="mat@gmail.com",
            direccion="Calle falsa 123",
            codigo_postal="3500",
        )


def test_cliente_dni_vacio():
    with pytest.raises(ValueError, match="Error, dni vacio"):
        Client(
            id=123,
            dni="",
            nombre_completo="Matias Raigg",
            email="mat@gmail.com",
            direccion="Calle falsa 123",
            codigo_postal="3500",
        )


def test_cliente_dni_no_numerico():
    with pytest.raises(
        ValueError, match="Error, el dni debe contener solamente números"
    ):
        Client(
            id=123,
            dni="1111hola",
            nombre_completo="Matias Raigg",
            email="mat@gmail.com",
            direccion="Calle falsa 123",
            codigo_postal="3500",
        )


def test_cliente_nombre_vacio():
    with pytest.raises(ValueError, match="Error, nombre vacio"):
        Client(
            id=123,
            dni="12345678",
            nombre_completo="",
            email="mat@gmail.com",
            direccion="Calle falsa 123",
            codigo_postal="3500",
        )


def test_cliente_email_vacio():
    with pytest.raises(ValueError, match="Error, email vacio"):
        Client(
            id=123,
            dni="12345678",
            nombre_completo="Matias Raigg",
            email="",
            direccion="Calle falsa 123",
            codigo_postal="3500",
        )


def test_cliente_email_formato_invalido():
    with pytest.raises(ValueError, match="Error, formato incorrecto de email"):
        Client(
            id=123,
            dni="12345678",
            nombre_completo="Matias Raigg",
            email="matgmail.com",
            direccion="Calle falsa 123",
            codigo_postal="3500",
        )


def test_cliente_direccion_vacia():
    with pytest.raises(ValueError, match="Error, direccion vacia"):
        Client(
            id=123,
            dni="12345678",
            nombre_completo="Matias Raigg",
            email="mat@gmail.com",
            direccion="",
            codigo_postal="3500",
        )


def test_cliente_codigo_postal_vacio():
    with pytest.raises(ValueError, match="Error, codigo postal vacio"):
        Client(
            id=123,
            dni="12345678",
            nombre_completo="Matias Raigg",
            email="mat@gmail.com",
            direccion="Calle falsa 123",
            codigo_postal="",
        )


# Metodos modificadores


def test_actualizar_nombre(client):
    client.actualizar_nombre("Matias Guagni")
    assert client.nombre_completo == "Matias Guagni"


def test_actualizar_nombre_invalido(client):
    with pytest.raises(ValueError, match="Error, nuevo nombre vacio"):
        client.actualizar_nombre("")
    assert client.nombre_completo == "Matias Raigg"


def test_actualizar_email(client):
    client.actualizar_email("matias@gmail.com")
    assert client.email == "matias@gmail.com"


def test_actualizar_email_vacio(client):
    with pytest.raises(ValueError, match="Error, nuevo email vacio"):
        client.actualizar_email("")
    assert client.email == "mat@gmail.com"


def test_actualizar_email_formato_invalido(client):
    with pytest.raises(
        ValueError, match="Error en el formato del nuevo email"
    ):
        client.actualizar_email("matiasgmail.com")
    assert client.email == "mat@gmail.com"


def test_actualizar_direccion(client):
    client.actualizar_direccion("Calle real 123")
    assert client.direccion == "Calle real 123"


def test_actualizar_direccion_vacia(client):
    with pytest.raises(ValueError, match="Error, direccion vacia"):
        client.actualizar_direccion("")
    assert client.direccion == "Calle falsa 123"


def test_actualizar_codigo_postal(client):
    client.actualizar_codigo_postal("3100")
    assert client.codigo_postal == "3100"


def test_actualizar_codigo_postal_vacio(client):
    with pytest.raises(ValueError, match="Error, nuevo codigo postal vacio"):
        client.actualizar_codigo_postal("")
    assert client.codigo_postal == "3500"
