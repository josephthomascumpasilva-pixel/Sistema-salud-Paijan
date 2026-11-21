# Clase base Persona: Ley N.° 29733
import re
from excepciones.errores_clinicos import DniInvalidoError, DatoClinicoInvalidoError


class Persona:
    def __init__(self, dni: str, nombre_completo: str):
        self._dni = ""
        self._nombre_completo = ""
        self.set_dni(dni)
        self.set_nombre_completo(nombre_completo)

    def get_dni_enmascarado(self) -> str:
        """Ley N.° 29733: Oculta los primeros 4 dígitos del DNI (ej. ****4521)."""
        return "****" + self._dni[-4:]

    def get_nombre_completo(self) -> str:
        return self._nombre_completo

    def set_dni(self, dni: str) -> None:
        # Tema 1: Validación con expresión regular (exactamente 8 dígitos)
        if not isinstance(dni, str) or re.fullmatch(r"\d{8}", dni.strip()) is None:
            raise DniInvalidoError(f"DNI inválido ('{dni}'). Debe tener 8 dígitos numéricos.")
        self._dni = dni.strip()

    def set_nombre_completo(self, nombre: str) -> None:
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise DatoClinicoInvalidoError("El nombre completo debe tener al menos 3 caracteres.")
        self._nombre_completo = nombre.strip()

    def obtener_rol(self) -> str:
        """Método base que será sobrescrito por las subclases (polimorfismo)."""
        return "Persona - Centro de Salud Paiján"
    