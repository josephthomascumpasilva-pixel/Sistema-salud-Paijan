# Clase parte en la relación de Composición con FichaAtencion (Tema 3)
from excepciones.errores_clinicos import DatoClinicoInvalidoError


class ItemMedicamento:
    def __init__(self, nombre: str, cantidad: int):
        if not isinstance(nombre, str) or len(nombre.strip()) < 2:
            raise DatoClinicoInvalidoError("El nombre del medicamento es obligatorio.")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise DatoClinicoInvalidoError("La cantidad dispensada debe ser mayor a 0.")
        self._nombre = nombre.strip()
        self._cantidad = cantidad

    def get_nombre(self) -> str:
        return self._nombre

    def get_cantidad(self) -> int:
        return self._cantidad

    def detalle(self) -> str:
        return f"{self._nombre} ({self._cantidad} unid.)"