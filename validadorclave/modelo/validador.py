from abc import ABC, abstractmethod


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self.longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) <= self.longitud_esperada:
            return False
        else:
            return True

    def _contiene_mayuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isupper():
                return True

        return False

    def _contiene_minuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.islower():
                return True

        return False

    def _contiene_numero(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isdigit():
                return True

        return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        caracteres_especiales = ["@", "_", "#", "$", "%"]
        for caracter in clave:
            if caracter in caracteres_especiales:
                return True
            else:
                return False

    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:
        pass

    def es_valida(self, clave: str) -> bool:
        pass


class Validador:

    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        pass
