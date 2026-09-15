"""Operaciones principales del sistema de gestion de datos."""
from validators import validar_texto, validar_entero_positivo, validar_precio

CATEGORIAS_VALIDAS = ("hardware", "software", "servicio")


def buscar_producto(productos: list[dict], codigo: str) -> dict | None:
    """Busca un producto por codigo."""
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def agregar_producto(productos: list[dict], datos: dict) -> bool:
    """Agrega un producto validado. Retorna True si fue agregado."""
    codigo = validar_texto(datos["codigo"], "codigo")
    if buscar_producto(productos, codigo):
        return False

    nombre = validar_texto(datos["nombre"], "nombre")
    categoria = validar_texto(datos["categoria"].lower(), "categoria")
    if categoria not in CATEGORIAS_VALIDAS:
        raise ValueError(f"Categoria invalida. Opciones: {', '.join(CATEGORIAS_VALIDAS)}")

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": validar_entero_positivo(datos["cantidad"], "cantidad"),
        "precio": validar_precio(datos["precio"]),
    }
    productos.append(producto)
    return True


def actualizar_stock(productos: list[dict], codigo: str, nueva_cantidad: str) -> bool:
    """Actualiza la cantidad de un producto existente."""
    producto = buscar_producto(productos, codigo)
    if not producto:
        return False
    producto["cantidad"] = validar_entero_positivo(nueva_cantidad, "cantidad")
    return True


def eliminar_producto(productos: list[dict], codigo: str) -> bool:
    """Elimina un producto segun su codigo."""
    producto = buscar_producto(productos, codigo)
    if not producto:
        return False
    productos.remove(producto)
    return True


def listar_productos(productos: list[dict]) -> list[dict]:
    """Retorna productos ordenados por codigo."""
    return sorted(productos, key=lambda item: item["codigo"])


def categorias_unicas(productos: list[dict]) -> set[str]:
    """Retorna categorias sin duplicados usando set."""
    return {producto["categoria"] for producto in productos}


def resumen_inventario(productos: list[dict]) -> dict:
    """Calcula resumen general del inventario."""
    total_unidades = sum(producto["cantidad"] for producto in productos)
    valores = [producto["cantidad"] * producto["precio"] for producto in productos]
    total_valorizado = suma_recursiva(valores)
    return {
        "total_productos": len(productos),
        "total_unidades": total_unidades,
        "total_valorizado": total_valorizado,
        "categorias": tuple(sorted(categorias_unicas(productos))),
    }


def suma_recursiva(valores: list[float]) -> float:
    """Suma una lista de valores usando recursion."""
    if not valores:
        return 0
    return valores[0] + suma_recursiva(valores[1:])
