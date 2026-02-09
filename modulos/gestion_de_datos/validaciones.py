
from datos_basicos import meses,gerencias

# Validaciones de opciones del menú principal. La M corresponde al Menu
productosM = 1
proveedoresM =2
vendedoresM = 3
metasM = 4
ventasM = 5
reportesM = 6
inventarioM = 7
salirM = 8

permisos_menu = {
    "comprador": [productosM, proveedoresM,inventarioM, reportesM, salirM],
    "vendedor": [productosM, proveedoresM, inventarioM,vendedoresM, metasM, ventasM,reportesM, salirM],
    "gerente": [productosM, proveedoresM, vendedoresM, metasM, ventasM, inventarioM,reportesM, salirM],
    "usuario": [productosM, inventarioM,ventasM,reportesM, salirM]
}

# Validaciones de opciones del menú acciones. La A corresponde a acción
agregarA = 1
verA = 2
eliminarA = 3
salirA = 4

permisos_acciones = {
    "product": {
        "comprador": [agregarA, verA, eliminarA, salirA],
        "vendedor": [verA, salirA],
        "usuario": [verA, salirA],
        "gerente": [agregarA, verA, eliminarA, salirA]
    },
    
    "vended": {
        "comprador": [verA, salirA],
        "vendedor": [verA, salirA],
        "usuario": [verA, salirA],
        "gerente": [agregarA, verA, eliminarA, salirA]
    },
    "proveed": {
        "comprador": [agregarA, verA, eliminarA, salirA],
        "vendedor": [verA, salirA],
        "usuario": [verA, salirA],
        "gerente": [agregarA, verA, eliminarA, salirA]
    },

     "met": {
        "vendedor": [verA, salirA],
        "usuario": [verA, salirA],
        "gerente": [agregarA, verA, eliminarA, salirA]
    },
    "vent": {
        "vendedor": [agregarA, verA, eliminarA,salirA],
        "usuario": [verA, salirA],
        "gerente": [agregarA, verA, eliminarA, salirA]
    },
     "invent": {
        "comprador": [agregarA, verA, salirA],
        "vendedor": [verA, salirA],
        "usuario": [verA, salirA],
        "gerente": [verA, salirA]
    },
}

# Control de permisos 

def menu_opciones(rol, modulo):
    while True:
        print("\n1. Agregar")
        print("2. Ver")
        print("3. Eliminar")
        print("4. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número")
            continue

        # Obtener permisos del rol para este módulo
        permisos_rol = permisos_acciones.get(modulo, {}).get(rol, [])

        if opcion not in permisos_rol:
            print("No tiene permiso para esta opción")
            continue

        if opcion == agregarA:
            print("Agregar")
        elif opcion == verA:
            print("Ver")
        elif opcion == eliminarA:
            print("Eliminar")
        elif opcion == salirA:
            print("Saliendo...")
            break


def pedir_opcion(mensaje, opciones_validas):
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in opciones_validas:
                return opcion
        except ValueError:
            pass
        print("Opción inválida")

# Funciones de validacion
def pedir_texto(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip()  # Elimino espacios en blanco
        if texto:
            return texto
        print("No puede estar vacío")
        
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
        except ValueError:
            pass
        print("Debe ingresar un número entero válido")

def pedir_decimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                return valor
        except ValueError:
            pass
        print("Debe ingresar un número válido")

# Validacion de rut

def pedir_rut(mensaje):
    while True:
        rut = input(mensaje).strip()

        if validar_formato_rut(rut):
            return normalizar_rut(rut)
        else:
            print("RUT inválido. Use el formato 12.345.678-5")
           
def validar_formato_rut(rut: str) -> bool:
    # Largo mínimo y máximo esperado
    if len(rut) not in (11, 12):
        return False

    # Debe tener puntos y guión en posiciones correctas
    if rut[-2] != "-":
        return False

    cuerpo, dv = rut.split("-")

    # DV debe ser número o K
    if not (dv.isdigit() or dv.lower() == "k"):
        return False

    partes = cuerpo.split(".")

    # Deben ser 3 bloques: XX . XXX . XXX
    if len(partes) != 3:
        return False

    if not (partes[0].isdigit() and len(partes[0]) in (1, 2)):
        return False

    if not (partes[1].isdigit() and len(partes[1]) == 3):
        return False

    if not (partes[2].isdigit() and len(partes[2]) == 3):
        return False

    return True


def normalizar_rut(rut: str) -> str:
    return rut.upper()



# Validaciones para modulos de ventas, metas, productos y proveedores

def pedir_mes(mensaje):
    while True:
        mes = input(mensaje).strip().upper()
        if mes in meses:
            return mes
        print("Mes inválido")

GERENCIAS = ["VENTAS", "FINANZAS", "RRHH", "OPERACIONES"]

def pedir_gerencia(mensaje):
    while True:
        gerencia = input(mensaje).strip().upper()
        if gerencia in GERENCIAS:
            return gerencia
        print("Gerencia inválida")

# Validacion de stock
def validar_stock(producto, cantidad):
    return producto["cantidad"] >= cantidad

def validar_meta(meta):
    return meta >= 0

def puede_eliminar_vendedor(vendedor):
    return not vendedor["ventas"]

def puede_eliminar_producto(producto):
    return producto["cantidad"] == 0









