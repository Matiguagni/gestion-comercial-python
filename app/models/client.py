import re

patron = r"^[^@\s.]+@[^@\s.]+\.[^@\s.]+$"
class Client:

    def __init__(
        self,
        id: int,
        dni: str,
        nombre_completo: str,
        email: str,
        direccion: str,
        codigo_postal: str,
    ):
        if id <= 0:
            raise ValueError(
                "Error, el id no puede iniciar con valor menor o igual a 0"
            )

        dni = dni.strip()
        if not dni:
            raise ValueError("Error, dni vacio")

        if not dni.isdigit():
            raise ValueError("Error, el dni debe contener solamente números")

        email = email.strip()
        if not email:
            raise ValueError("Error, formato del email incorrecto")
        
        if not re.fullmatch(patron, email):
            raise ValueError("Error, formato del email incorrecto")

        nombre_completo = nombre_completo.strip()
        if not nombre_completo:
            raise ValueError("Error, nombre vacio")

        direccion = direccion.strip()
        if not direccion:
            raise ValueError("Error, direccion vacia")

        codigo_postal = codigo_postal.strip()
        if not codigo_postal:
            raise ValueError("Error, codigo postal vacio")

        self.id = id
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.email = email
        self.direccion = direccion
        self.codigo_postal = codigo_postal

    def actualizar_nombre(self, nuevo_nombre: str) -> None:
        nuevo_nombre = nuevo_nombre.strip()
        if not nuevo_nombre:
            raise ValueError("Error, nuevo nombre vacio")
        self.nombre_completo = nuevo_nombre

    def actualizar_email(self, nuevo_email: str) -> None:
        nuevo_email = nuevo_email.strip()
        if not nuevo_email:
            raise ValueError("Error, formato del email incorrecto")
        if not re.fullmatch(patron, nuevo_email):
            raise ValueError("Error, formato del email incorrecto")
        self.email = nuevo_email

    def actualizar_direccion(self, nueva_direccion: str) -> None:
        if not nueva_direccion:
            raise ValueError("Error, direccion vacia")
        self.direccion = nueva_direccion
    

    def actualizar_codigo_postal(self, nuevo_codigo_postal: str) -> None:
        if not nuevo_codigo_postal:
            raise ValueError("Error, nuevo codigo postal vacio")
        self.codigo_postal = nuevo_codigo_postal
