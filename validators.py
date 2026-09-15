"""Funciones de validacion para entradas del sistema."""


def validar_texto(texto: str, campo: str) -> str:
    """Valida que un texto no este vacio."""
    texto = texto.strip()
    if not texto:
        raise ValueError(f"El campo {campo} no puede estar vacio.")
    return texto


def validar_entero_positivo(valor: str, campo: str) -> int:
    """Convierte y valida un numero entero positivo."""
    try:
        numero = int(valor)
    except ValueError as exc:
        raise ValueError(f"El campo {campo} debe ser un numero entero.") from exc
    if numero < 0:
        raise ValueError(f"El campo {campo} no puede ser negativo.")
    return numero


def validar_precio(valor: str) -> float:
    """Convierte y valida un precio mayor o igual a cero."""
    try:
        precio = float(valor)
    except ValueError as exc:
        raise ValueError("El precio debe ser numerico.") from exc
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    return precio
