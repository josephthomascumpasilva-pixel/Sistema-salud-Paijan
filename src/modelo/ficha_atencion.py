# FichaAtencion: Asociación (Paciente, PersonalSalud), Composición (ItemMedicamento)
# y Sobrecarga simulada en registrar_triaje() mediante parámetro por defecto
import re
from modelo.paciente import Paciente
from modelo.personal_salud import PersonalSalud
from modelo.item_medicamento import ItemMedicamento
from excepciones.errores_clinicos import DatoClinicoInvalidoError


class FichaAtencion:
    def __init__(self, codigo: str, paciente: Paciente, responsable: PersonalSalud):
        if not isinstance(codigo, str) or re.fullmatch(r"FA-\d{3}", codigo.strip()) is None:
            raise DatoClinicoInvalidoError("El código de ficha debe tener formato FA-000 (ej. FA-001).")
        if not isinstance(paciente, Paciente):
            raise DatoClinicoInvalidoError("Debe asignar un paciente válido a la ficha.")
        if not isinstance(responsable, PersonalSalud):
            raise DatoClinicoInvalidoError("Debe asignar un personal de salud válido.")

        self._codigo = codigo.strip()
        # Asociación: referencias a objetos existentes
        self._paciente = paciente
        self._responsable = responsable
        self._peso_kg = 0.0
        self._talla_m = 0.0
        self._temperatura_c = 36.5
        # Composición: lista de ítems creados y controlados exclusivamente por esta ficha
        self._medicamentos: list[ItemMedicamento] = []

    def registrar_triaje(self, peso_kg: float, talla_m: float, temperatura_c: float = 36.5) -> None:
        """Sobrecarga en Python: si no se envía temperatura_c, asume 36.5 °C por defecto."""
        if peso_kg <= 0 or peso_kg > 300:
            raise DatoClinicoInvalidoError("El peso debe estar entre 1 y 300 kg.")
        if talla_m <= 0.3 or talla_m > 2.5:
            raise DatoClinicoInvalidoError("La talla debe estar entre 0.30 y 2.50 metros.")
        if temperatura_c < 34.0 or temperatura_c > 43.0:
            raise DatoClinicoInvalidoError("La temperatura debe estar entre 34.0 y 43.0 °C.")

        self._peso_kg = round(peso_kg, 2)
        self._talla_m = round(talla_m, 2)
        self._temperatura_c = round(temperatura_c, 1)

    def agregar_medicamento(self, nombre: str, cantidad: int) -> None:
        """Composición: la ficha crea el objeto ItemMedicamento internamente."""
        nuevo_item = ItemMedicamento(nombre, cantidad)
        self._medicamentos.append(nuevo_item)

    def total_unidades_dispensadas(self) -> int:
        return sum(item.get_cantidad() for item in self._medicamentos)

    def get_codigo(self) -> str:
        return self._codigo

    def get_paciente(self) -> Paciente:
        return self._paciente

    def get_responsable(self) -> PersonalSalud:
        return self._responsable

    def get_peso_kg(self) -> float:
        return self._peso_kg

    def get_talla_m(self) -> float:
        return self._talla_m

    def get_temperatura_c(self) -> float:
        return self._temperatura_c

    def get_medicamentos(self) -> list[ItemMedicamento]:
        return list(self._medicamentos)