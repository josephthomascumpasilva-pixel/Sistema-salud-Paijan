class DniInvalidoError(Exception):
    """Se lanza cuando el DNI no tiene exactamente 8 dígitos numéricos."""
    pass


class DatoClinicoInvalidoError(Exception):
    """Se lanza cuando un dato médico o administrativo está vacío o fuera de rango."""
    pass