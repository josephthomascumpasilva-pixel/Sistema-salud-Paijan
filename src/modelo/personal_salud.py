# Subclase PersonalSalud: Hereda de Persona y sobrescribe obtener_rol() (Tema 2)
from modelo.persona import Persona
from excepciones.errores_clinicos import DatoClinicoInvalidoError


class PersonalSalud(Persona):
    def __init__(self, dni: str, nombre_completo: str, colegiatura: str, especialidad: str):
        super().__init__(dni, nombre_completo)
        self._colegiatura = ""
        self._especialidad = ""
        self.set_colegiatura(colegiatura)
        self.set_especialidad(especialidad)

    def get_colegiatura(self) -> str:
        return self._colegiatura

    def get_especialidad(self) -> str:
        return self._especialidad

    def set_colegiatura(self, colegiatura: str) -> None:
        if not isinstance(colegiatura, str) or len(colegiatura.strip()) < 4:
            raise DatoClinicoInvalidoError("La colegiatura debe tener al menos 4 caracteres.")
        self._colegiatura = colegiatura.strip()

    def set_especialidad(self, especialidad: str) -> None:
        if not isinstance(especialidad, str) or len(especialidad.strip()) < 3:
            raise DatoClinicoInvalidoError("La especialidad no puede estar vacía.")
        self._especialidad = especialidad.strip()

    def obtener_rol(self) -> str:
        return f"Personal Asistencial [{self._especialidad} | Col. {self._colegiatura}]"