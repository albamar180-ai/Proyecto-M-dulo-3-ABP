"""Modulo para cargar y guardar productos desde archivos CSV."""
import csv
from pathlib import Path

CAMPOS = ("codigo", "nombre", "categoria", "cantidad", "precio")


def cargar_productos(ruta_archivo: str) -> list[dict]:
    """Carga productos desde un CSV. Si no existe, retorna lista vacia."""
    ruta = Path(ruta_archivo)
    if not ruta.exists():
        return []

    productos = []
    with ruta.open("r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos.append({
                "codigo": fila["codigo"],
                "nombre": fila["nombre"],
                "categoria": fila["categoria"],
                "cantidad": int(fila["cantidad"]),
                "precio": float(fila["precio"]),
            })
    return productos


def guardar_productos(ruta_archivo: str, productos: list[dict]) -> None:
    """Guarda la lista de productos en formato CSV."""
    ruta = Path(ruta_archivo)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(productos)
