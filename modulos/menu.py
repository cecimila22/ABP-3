#from gestion_de_datos.validaciones import permisos_menu
from productos import agregar_productos, mostrar_productos, eliminar_producto
from proveedores import agregar_proveedor, mostrar_proveedores, eliminar_proveedor
from vendedores import agregar_vendedor, mostrar_vendedores, eliminar_vendedor
from metas import ingresar_metas_mes_vendedor, mostrar_metas
from ventas import ingresar_venta, mostrar_ventas, eliminar_venta
from inventario import validar_stock, descontar_stock, alertas_stock_bajo

#### Menu principal se usa lambda
menu_principal = [
    [1, "Productos", lambda: ejecutar_menu(menu_productos)],
    [2, "Proveedores", lambda: ejecutar_menu(menu_proveedores)],
    [3, "Vendedores", lambda: ejecutar_menu(menu_vendedores)],
    [4, "Metas", lambda: ejecutar_menu(menu_metas)],
    [5, "Ventas", lambda: ejecutar_menu(menu_ventas)],
    [6, "Inventario", lambda: ejecutar_menu(menu_inventario)],
    [7, "Salir", None]
]

#### Menu productos
menu_productos = [
    [1, "Agregar producto", agregar_productos],
    [2, "Mostrar productos", mostrar_productos],
    [3, "Eliminar producto", eliminar_producto],
    [4, "Volver", None]
]

#### Menu proveedores
menu_proveedores = [
    [1, "Agregar proveedores", agregar_proveedor],
    [2, "Mostrar proveedores", mostrar_proveedores],
    [3, "Eliminar producto", eliminar_proveedor],
    [4, "Volver", None]
]

#### Menu vendedores
menu_vendedores = [
    [1, "Agregar vendedores", agregar_vendedor],
    [2, "Mostrar vendedores", mostrar_vendedores],
    [3, "Eliminar vendedores", eliminar_vendedor],
    [4, "Volver", None]
]

#### Menu metas
menu_metas = [
    [1, "Ingresar o modificar metas", ingresar_metas_mes_vendedor],
    [2, "Mostrar metas", mostrar_metas],
    [3, "Volver", None]
]

#### Menu ventas
menu_ventas = [
    [1, "Agregar ventas", ingresar_venta],
    [2, "Mostrar ventas", mostrar_ventas],
    [3, "Eliminar ventas", eliminar_venta],
    [4, "Volver", None]
]
#### Menu inventario
menu_inventario = [
    [1, "Validar stock", validar_stock],
    [2, "Descontar_stock", descontar_stock],
    [3, "Validar stock bajo:", alertas_stock_bajo],
    [4, "Volver", None]
]

#### Ejecutar menu
def ejecutar_menu(menu):
    while True:
        print()
        for opcion in menu:
            print(f"{opcion[0]}. {opcion[1]}")

        try:
            eleccion = int(input("Seleccione opción: "))
        except ValueError:
            print("Debe ingresar un número del menú")
            continue

        for opcion in menu:
            if opcion[0] == eleccion:
                if opcion[2] is None:
                    return
                opcion[2]()
                break
        else:
            print("Opción inválida")


ejecutar_menu(menu_principal)