# CentroSalud: Relación de Agregación con PersonalSalud (Tema 3)
from modelo.personal_salud import PersonalSalud


class CentroSalud:
    def __init__(self, nombre: str, distrito: str):
        self._nombre = nombre
        self._distrito = distrito
        # Agregación: el personal existe fuera del establecimiento y puede rotar
        self._personal: list[PersonalSalud] = []

    def agregar_personal(self, profesional: PersonalSalud) -> None:
        self._personal.append(profesional)

    def get_personal(self) -> list[PersonalSalud]:
        return list(self._personal)

    def get_nombre(self) -> str:
        return self._nombre

    def get_distrito(self) -> str:
        return self._distrito