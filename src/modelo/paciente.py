# Subclase Paciente: Hereda de Persona y sobrescribe obtener_rol() (Tema 2)
import re
from modelo.persona import Persona
from excepciones.errores_clinicos import DatoClinicoInvalidoError


class Paciente(Persona):
    def __init__(self, dni: str, nombre_completo: str, nro_historia: str, alergias: str = "Ninguna"):
        super().__init__(dni, nombre_completo)
        self._nro_historia = ""
        self._alergias = ""
        self.set_nro_historia(nro_historia)
        self.set_alergias(alergias)

    def get_nro_historia(self) -> str:
        return self._nro_historia

    def get_alergias(self) -> str:
        return self._alergias

    def set_nro_historia(self, nro_historia: str) -> None:
        # Validación Regex: formato HC-0001
        if not isinstance(nro_historia, str) or re.fullmatch(r"HC-\d{4}", nro_historia.strip()) is None:
            raise DatoClinicoInvalidoError("El N.° de historia debe tener formato HC-0000 (ej. HC-1001).")
        self._nro_historia = nro_historia.strip()

    def set_alergias(self, alergias: str) -> None:
        texto = alergias.strip() if isinstance(alergias, str) else ""
        self._alergias = texto if texto else "Ninguna"

    def obtener_rol(self) -> str:
        return f"Paciente [Historia: {self._nro_historia} | Alergias: {self._alergias}]"