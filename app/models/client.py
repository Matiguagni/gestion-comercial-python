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

        if not dni:
            raise ValueError("Error, dni vacio")

        if not dni.isdigit():
            raise ValueError("Error, el dni debe contener solamente números")

        if not email:
            raise ValueError("Error, email vacio")

        if "@" not in email:
            raise ValueError("Error, formato incorrecto de email")

        if not nombre_completo:
            raise ValueError("Error, nombre vacio")

        if not direccion:
            raise ValueError("Error, direccion vacia")

        if not codigo_postal:
            raise ValueError("Error, codigo postal vacio")

        self.id = id
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.email = email
        self.direccion = direccion
        self.codigo_postal = codigo_postal

    def actualizar_nombre(self, nuevo_nombre: str) -> None:
        if not nuevo_nombre:
            raise ValueError("Error, nuevo nombre vacio")
        self.nombre_completo = nuevo_nombre

    def actualizar_email(self, nuevo_email: str) -> None:
        if not nuevo_email:
            raise ValueError("Error, nuevo email vacio")
        if "@" not in nuevo_email:
            raise ValueError("Error en el formato del nuevo email")
        self.email = nuevo_email

    def actualizar_direccion(self, nueva_direccion: str) -> None:
        if not nueva_direccion:
            raise ValueError("Error, direccion vacia")
        self.direccion = nueva_direccion

    def actualizar_codigo_postal(self, nuevo_codigo_postal: str) -> None:
        if not nuevo_codigo_postal:
            raise ValueError("Error, nuevo codigo postal vacio")
        self.codigo_postal = nuevo_codigo_postal
