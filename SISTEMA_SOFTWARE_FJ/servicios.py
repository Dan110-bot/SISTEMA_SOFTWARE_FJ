from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, codigo, nombre, precio_base):
        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        self._codigo = codigo
        self._nombre = nombre
        self._precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad, descuento=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, cantidad):
        pass


class ServicioSala(Servicio):

    def calcular_costo(self, cantidad, descuento=0):
        self.validar_parametros(cantidad)

        if not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100")

        total = self._precio_base * cantidad
        return total - (total * descuento / 100)

    def describir_servicio(self):
        return "Reserva de salas"

    def validar_parametros(self, cantidad):
        if (not isinstance(cantidad, (int, float))
                or isinstance(cantidad, bool) or cantidad <= 0):
            raise ValueError("La cantidad de horas no es valida")


class ServicioEquipo(Servicio):

    def calcular_costo(self, cantidad, descuento=0):
        self.validar_parametros(cantidad)

        if not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100")

        total = self._precio_base * cantidad
        return total - (total * descuento / 100)

    def describir_servicio(self):
        return "Alquiler de equipos"

    def validar_parametros(self, cantidad):
        if (not isinstance(cantidad, int)
                or isinstance(cantidad, bool) or cantidad <= 0):
            raise ValueError("La cantidad de equipos no es valida")


class ServicioAsesoria(Servicio):

    def calcular_costo(self, cantidad, descuento=0):
        self.validar_parametros(cantidad)

        if not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100")

        total = self._precio_base * cantidad
        return total - (total * descuento / 100)

    def describir_servicio(self):
        return "Asesoria especializada"

    def validar_parametros(self, cantidad):
        if (not isinstance(cantidad, int)
                or isinstance(cantidad, bool) or cantidad <= 0):
            raise ValueError("La cantidad de asesorias no es valida")