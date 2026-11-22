import logging
import os

from entidades import Cliente
from servicios import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)
from reservas import Reserva
from excepciones import (
    ErrorSistema,
    ClienteNoEncontrado,
    ReservaNoEncontrada,
    ServicioNoDisponible,
    DatosInvalidos
)


# CONFIGURACION DEL SISTEMA DE REGISTRO

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=os.path.join("logs", "sistema.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)


# LISTAS DEL SISTEMA

clientes = []
servicios = []
reservas = []


# CONTROL DE OPERACIONES

def ejecutar_operacion(numero, descripcion, funcion):

    print("\n" + "=" * 55)
    print(f"OPERACION {numero}: {descripcion}")
    print("=" * 55)

    try:
        funcion()

    except ErrorSistema as error:
        print(f"Error controlado: {error}")
        logging.warning(str(error))

    except ValueError as error:
        print(f"Error de validacion: {error}")
        logging.warning(str(error))

    except Exception as error:
        print(f"Error inesperado: {error}")
        logging.exception("Error inesperado")

    else:
        print("Operacion ejecutada correctamente.")
        logging.info(f"Operacion {numero} ejecutada correctamente")

    finally:
        print("Operacion finalizada.")


# BUSCAR CLIENTE POR IDENTIFICACION

def buscar_cliente(identificacion):

    for cliente in clientes:

        if cliente.identificacion == identificacion:
            return cliente

    raise ClienteNoEncontrado(
        "El cliente no se encuentra registrado"
    )


# BUSCAR SERVICIO POR TIPO

def buscar_servicio(tipo_servicio):

    for servicio in servicios:

        if isinstance(servicio, tipo_servicio):
            return servicio

    raise ServicioNoDisponible(
        "El servicio solicitado no esta disponible"
    )


# BUSCAR RESERVA POR CODIGO

def buscar_reserva(codigo):

    for reserva in reservas:

        if reserva.codigo == codigo:
            return reserva

    raise ReservaNoEncontrada(
        "La reserva no existe"
    )


# OPERACION 1

def registrar_primer_cliente():

    cliente = Cliente(
        "1001",
        "Carlos Ramirez",
        "3001234567",
        "carlos@gmail.com"
    )

    clientes.append(cliente)
    print("Cliente registrado correctamente.")


# OPERACION 2

def registrar_cliente_invalido():

    try:
        Cliente(
            "",
            "Cliente de prueba",
            "3001234567",
            "prueba@gmail.com"
        )

    except ValueError as error:
        raise DatosInvalidos(str(error))


# OPERACION 3

def registrar_segundo_cliente():

    cliente = Cliente(
        "1002",
        "Maria Lopez",
        "3101234567",
        "maria@gmail.com"
    )

    clientes.append(cliente)
    print("Segundo cliente registrado correctamente.")


# OPERACION 4

def mostrar_clientes():

    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print("\n" + cliente.mostrar_informacion())


# OPERACION 5

def actualizar_telefono():

    cliente = buscar_cliente("1001")

    cliente.actualizar_telefono("3209876543")

    print("Telefono actualizado correctamente.")
    print(cliente.mostrar_informacion())


# OPERACION 6

def registrar_servicios():

    sala = ServicioSala(
        "S01",
        "Reserva de salas",
        25000
    )

    equipo = ServicioEquipo(
        "E01",
        "Alquiler de equipos",
        15000
    )

    asesoria = ServicioAsesoria(
        "A01",
        "Asesoria especializada",
        40000
    )

    servicios.extend([sala, equipo, asesoria])

    print("Servicios registrados correctamente.")


# OPERACION 7

def crear_reserva_sala():

    cliente = buscar_cliente("1001")
    servicio = buscar_servicio(ServicioSala)

    reserva = Reserva(cliente, servicio, 2)

    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# OPERACION 8

def crear_reserva_equipo():

    cliente = buscar_cliente("1002")
    servicio = buscar_servicio(ServicioEquipo)

    reserva = Reserva(cliente, servicio, 2)

    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# OPERACION 9

def crear_reserva_asesoria():

    cliente = buscar_cliente("1001")
    servicio = buscar_servicio(ServicioAsesoria)

    reserva = Reserva(cliente, servicio, 1)

    reservas.append(reserva)

    print(reserva.mostrar_reserva())


# OPERACION 10

def cancelar_reserva():

    reserva = buscar_reserva(1)

    reserva.cancelar_reserva()

    print("Reserva cancelada correctamente.")


# OPERACION 11

def cancelar_reserva_nuevamente():

    reserva = buscar_reserva(1)

    reserva.cancelar_reserva()


# OPERACION 12

def crear_reserva_invalida():

    cliente = buscar_cliente("1001")
    servicio = buscar_servicio(ServicioSala)

    Reserva(cliente, servicio, 0)


# OPERACION 13

def mostrar_reservas():

    if not reservas:
        print("No hay reservas registradas.")
        return

    for reserva in reservas:
        print("\n" + reserva.mostrar_reserva())


# OPERACION 14

def probar_cliente_inexistente():

    buscar_cliente("9999")


# INICIAR SISTEMA

def iniciar_sistema():

    print("\n")
    print("*" * 55)
    print("       SISTEMA INTEGRAL DE GESTION SOFTWARE FJ")
    print("*" * 55)

    operaciones = [
        ("Registrar primer cliente", registrar_primer_cliente),
        ("Registrar cliente invalido", registrar_cliente_invalido),
        ("Registrar segundo cliente", registrar_segundo_cliente),
        ("Mostrar clientes", mostrar_clientes),
        ("Actualizar telefono", actualizar_telefono),
        ("Registrar servicios", registrar_servicios),
        ("Crear reserva de sala", crear_reserva_sala),
        ("Crear reserva de equipo", crear_reserva_equipo),
        ("Crear reserva de asesoria", crear_reserva_asesoria),
        ("Cancelar reserva", cancelar_reserva),
        ("Cancelar reserva nuevamente", cancelar_reserva_nuevamente),
        ("Crear reserva invalida", crear_reserva_invalida),
        ("Mostrar reservas", mostrar_reservas),
        ("Buscar cliente inexistente", probar_cliente_inexistente)
    ]

    for numero, (descripcion, funcion) in enumerate(operaciones, start=1):
        ejecutar_operacion(numero, descripcion, funcion)

    print("\n")
    print("*" * 55)
    print("       SISTEMA FINALIZADO")
    print("*" * 55)

    print("\nRegistro guardado en logs/sistema.log")


if __name__ == "__main__":
    iniciar_sistema()