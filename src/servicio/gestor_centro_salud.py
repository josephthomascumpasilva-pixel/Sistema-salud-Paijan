from functools import reduce
from modelo.centro_salud import CentroSalud
from modelo.paciente import Paciente
from modelo.personal_salud import PersonalSalud
from modelo.ficha_atencion import FichaAtencion
from excepciones.errores_clinicos import DatoClinicoInvalidoError


def calcular_imc(peso_kg: float, talla_m: float) -> tuple[float, str]:
    """
    Función pura (Tema 4): No modifica variables externas y siempre devuelve
    el mismo resultado (tupla inmutable) para los mismos parámetros.
    """
    if talla_m <= 0:
        raise DatoClinicoInvalidoError("La talla debe ser mayor a cero para calcular el IMC.")
    imc = round(peso_kg / (talla_m ** 2), 2)
    if imc < 18.5:
        estado = "Bajo peso"
    elif imc < 25.0:
        estado = "Normal"
    elif imc < 30.0:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"
    return (imc, estado)


class GestorCentroSalud:
    _instancia = None

    def __new__(cls):
        # Patrón Singleton: garantiza una única instancia del gestor en todo el sistema
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self):
        if self._inicializado:
            return
        self.centro = CentroSalud("Centro de Salud Paiján", "Paiján - Ascope")
        self._pacientes: list[Paciente] = []
        self._fichas: list[FichaAtencion] = []
        self._cargar_datos_ficticios()
        self._inicializado = True

    def _cargar_datos_ficticios(self) -> None:
        """Datos 100 % ficticios para pruebas iniciales (Ley N.° 29733)."""
        enf1 = PersonalSalud("40112233", "Lic. Carla Mendoza Ríos", "CEP-88412", "Enfermería - Triaje")
        med1 = PersonalSalud("40998877", "Dr. Jorge Paredes Luna", "CMP-65120", "Medicina General")
        self.centro.agregar_personal(enf1)
        self.centro.agregar_personal(med1)

        p1 = Paciente("71234501", "Lucía Quispe Valverde", "HC-1001", "Penicilina")
        p2 = Paciente("72345602", "Mateo Rojas Salazar", "HC-1002", "Ninguna")
        self._pacientes.extend([p1, p2])

        f1 = FichaAtencion("FA-001", p1, enf1)
        f1.registrar_triaje(58.0, 1.60, 38.6)  # Con fiebre
        f1.agregar_medicamento("Paracetamol 500mg", 10)
        f1.agregar_medicamento("Sales de Rehidratación", 3)

        f2 = FichaAtencion("FA-002", p2, med1)
        f2.registrar_triaje(74.0, 1.72)  # Usa temperatura por defecto 36.5 °C
        f2.agregar_medicamento("Ibuprofeno 400mg", 6)

        self._fichas.extend([f1, f2])

    def registrar_paciente(self, paciente: Paciente) -> None:
        self._pacientes.append(paciente)

    def buscar_paciente_por_historia(self, nro_historia: str) -> Paciente:
        for p in self._pacientes:
            if p.get_nro_historia() == nro_historia.strip():
                return p
        raise DatoClinicoInvalidoError(f"No existe un paciente con historia '{nro_historia}'.")

    def registrar_ficha(self, ficha: FichaAtencion) -> None:
        self._fichas.append(ficha)

    def get_pacientes(self) -> list[Paciente]:
        return list(self._pacientes)

    def get_fichas(self) -> list[FichaAtencion]:
        return list(self._fichas)

    # --- Operaciones de Programación Funcional (Tema 4) ---

    def filtrar_fichas_con_fiebre(self) -> list[FichaAtencion]:
        """Uso de filter + lambda: selecciona fichas con temperatura >= 38.0 °C."""
        return list(filter(lambda f: f.get_temperatura_c() >= 38.0, self._fichas))

    def generar_reporte_anonimizado(self) -> tuple[str, ...]:
        """Uso de map + lambda + tupla inmutable: resumen con DNI enmascarado."""
        lineas = map(
            lambda f: (
                f"[{f.get_codigo()}] {f.get_paciente().get_nombre_completo()} "
                f"(DNI: {f.get_paciente().get_dni_enmascarado()}) | "
                f"Temp: {f.get_temperatura_c()} °C | "
                f"IMC: {calcular_imc(f.get_peso_kg(), f.get_talla_m())[0]} "
                f"({calcular_imc(f.get_peso_kg(), f.get_talla_m())[1]}) | "
                f"Medicamentos: {f.total_unidades_dispensadas()} unid."
            ),
            self._fichas,
        )
        return tuple(lineas)

    def contar_total_medicamentos(self) -> int:
        """Uso de reduce + lambda: acumula el total de unidades dispensadas."""
        return reduce(lambda acc, f: acc + f.total_unidades_dispensadas(), self._fichas, 0)