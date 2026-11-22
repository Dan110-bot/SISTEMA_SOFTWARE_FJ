from datetime import datetime


class Reserva:

    contador = 1

    def __init__(self, cliente, servicio, cantidad):

        if cliente is None:
            raise ValueError("Debe seleccionar un cliente")

        if servicio is None:
            raise ValueError("Debe seleccionar un servicio")

        costo = servicio.calcular_costo(cantidad)

        self._codigo = Reserva.contador
        Reserva.contador += 1

        self._cliente = cliente
        self._servicio = servicio
        self._cantidad = cantidad
        self._fecha = datetime.now()
        self._estado = "Activa"
        self._costo = costo

    @property
    def codigo(self):
        return self._codigo

    @property
    def estado(self):
        return self._estado

    def mostrar_reserva(self):

        return (
            f"Codigo de reserva: {self._codigo}\n"
            f"Cliente: {self._cliente.nombre}\n"
            f"Servicio: {self._servicio.describir_servicio()}\n"
            f"Cantidad: {self._cantidad}\n"
            f"Fecha: {self._fecha.strftime('%d/%m/%Y %H:%M')}\n"
            f"Estado: {self._estado}\n"
            f"Costo: ${self._costo:.2f}"
        )

    def cancelar_reserva(self):

        if self._estado == "Cancelada":
            raise ValueError("La reserva ya esta cancelada")

        self._estado = "Cancelada"

    def calcular_total(self):
        return self._costo

    def cambiar_cantidad(self, nueva_cantidad):

        nuevo_costo = self._servicio.calcular_costo(nueva_cantidad)

        self._cantidad = nueva_cantidad
        self._costo = nuevo_costo