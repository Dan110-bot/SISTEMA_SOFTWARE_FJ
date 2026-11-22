from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, identificacion, nombre):
        self._identificacion = identificacion
        self._nombre = nombre

    @abstractmethod
    def mostrar_informacion(self):
        pass


class Cliente(Entidad):

    def __init__(self, identificacion, nombre, telefono, correo):

        if not isinstance(identificacion, str) or not identificacion.strip():
            raise ValueError("La identificacion es obligatoria")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre es obligatorio")

        if not isinstance(telefono, str) or not telefono.isdigit() or len(telefono) < 7:
            raise ValueError("El telefono no es valido")

        if not isinstance(correo, str) or "@" not in correo or "." not in correo:
            raise ValueError("El correo no es valido")

        super().__init__(identificacion, nombre)

        self._telefono = telefono
        self._correo = correo

    @property
    def identificacion(self):
        return self._identificacion

    @property
    def nombre(self):
        return self._nombre

    @property
    def telefono(self):
        return self._telefono

    @property
    def correo(self):
        return self._correo

    def mostrar_informacion(self):
        return (
            f"Identificacion: {self._identificacion}\n"
            f"Nombre: {self._nombre}\n"
            f"Telefono: {self._telefono}\n"
            f"Correo: {self._correo}"
        )

    def actualizar_telefono(self, nuevo_telefono):

        if (not isinstance(nuevo_telefono, str)
                or not nuevo_telefono.isdigit()
                or len(nuevo_telefono) < 7):
            raise ValueError("El telefono no es valido")

        self._telefono = nuevo_telefono

    def actualizar_correo(self, nuevo_correo):

        if (not isinstance(nuevo_correo, str)
                or "@" not in nuevo_correo
                or "." not in nuevo_correo):
            raise ValueError("El correo no es valido")

        self._correo = nuevo_correo