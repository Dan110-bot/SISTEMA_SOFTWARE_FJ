class ErrorSistema(Exception):
    pass


class ClienteNoEncontrado(ErrorSistema):
    pass


class ReservaNoEncontrada(ErrorSistema):
    pass


class ServicioNoDisponible(ErrorSistema):
    pass


class DatosInvalidos(ErrorSistema):
    pass