"""Sistema de gestion de datos - Proyecto Modulo 3 ABP."""
from data_manager import cargar_productos, guardar_productos
from operations import (
    agregar_producto,
    actualizar_stock,
    eliminar_producto,
    listar_productos,
    resumen_inventario,
)

RUTA_DATOS = "data/productos.csv"


def mostrar_menu() -> None:
    print("\n SISTEMA DE GESTION DE DATOS ")
    print("1. Listar productos")
    print("2. Agregar producto")
    print("3. Actualizar stock")
    print("4. Eliminar producto")
    print("5. Ver resumen")
    print("0. Salir")


def mostrar_productos(productos: list[dict]) -> None:
    if not productos:
        print("No existen productos registrados.")
        return
    print(f"{'CODIGO':<10} {'NOMBRE':<20} {'CATEGORIA':<12} {'CANT.':<8} {'PRECIO':<10}")
    for producto in listar_productos(productos):
        print(
            f"{producto['codigo']:<10} {producto['nombre']:<20} "
            f"{producto['categoria']:<12} {producto['cantidad']:<8} "
            f"${producto['precio']:,.0f}"
        )


def pedir_datos_producto() -> dict:
    return {
        "codigo": input("Codigo: "),
        "nombre": input("Nombre: "),
        "categoria": input("Categoria (hardware/software/servicio): "),
        "cantidad": input("Cantidad: "),
        "precio": input("Precio: "),
    }


def ejecutar() -> None:
    productos = cargar_productos(RUTA_DATOS)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                mostrar_productos(productos)
            elif opcion == "2":
                if agregar_producto(productos, pedir_datos_producto()):
                    guardar_productos(RUTA_DATOS, productos)
                    print("Producto agregado correctamente.")
                else:
                    print("No se agrego: el codigo ya existe.")
            elif opcion == "3":
                codigo = input("Codigo a actualizar: ").strip()
                cantidad = input("Nueva cantidad: ").strip()
                if actualizar_stock(productos, codigo, cantidad):
                    guardar_productos(RUTA_DATOS, productos)
                    print("Stock actualizado correctamente.")
                else:
                    print("Producto no encontrado.")
            elif opcion == "4":
                codigo = input("Codigo a eliminar: ").strip()
                if eliminar_producto(productos, codigo):
                    guardar_productos(RUTA_DATOS, productos)
                    print("Producto eliminado correctamente.")
                else:
                    print("Producto no encontrado.")
            elif opcion == "5":
                resumen = resumen_inventario(productos)
                print(f"Total productos: {resumen['total_productos']}")
                print(f"Total unidades: {resumen['total_unidades']}")
                print(f"Total valorizado: ${resumen['total_valorizado']:,.0f}")
                print(f"Categorias: {', '.join(resumen['categorias'])}")
            elif opcion == "0":
                print("Gracias por utilizar el sistema.")
                break
            else:
                print("Opcion invalida. Intente nuevamente.")
                continue
        except ValueError as error:
            print(f"Error de validacion: {error}")


if __name__ == "__main__":
    ejecutar()
