"""
from datos_basicos import margen

from inventario import validar_stock, descontar_stock
from vendedores import vendedor
from productos import productos
from typing import Dict, List
"""
import json
import os
from datetime import date # Aqui obtenemos la fecha de hoy
from validaciones import pedir_texto, pedir_entero, pedir_decimal
from datos_basicos import margen, gerencias, meses


######### VENTAS #########
# Aqui se generan identificador (id) de las ventas
archivo_ventas = 'venta.json'
archivo_productos = 'producto.json'

### Aquí se cargan las ventas desde el JSON 
def cargar_ventas():
    if os.path.exists(archivo_ventas) and os.path.getsize(archivo_ventas) > 0:
        with open(archivo_ventas, 'r', encoding='utf-8') as f:
            return json. load(f)
    return {}

ventas = cargar_ventas()

def generar_codigo_venta (codigo_vendedor,id_venta,fecha_de_ingreso_de_venta,mes_de_venta,productos,total_venta):
    contador_actual_venta = len(ventas) + 1
    codigo_venta = f"Vent{contador_actual_venta:03d}"

    ### Aquí validamos si el codigo de venta existe, para no sobreescribir
    with open(archivo_productos, 'r', encoding='utf-8') as f:
            return json. load(f)
    
    while codigo_venta in ventas:
        contador_actual_venta += 1
        codigo_venta = f"Vent{contador_actual_venta:03d}"

    ventas[codigo_venta, codigo_producto, cantidad_vendida]= { 
        "codigo_vendedor" : codigo_vendedor,
        "id_venta": generar_codigo_venta(),
        "fecha_de_ingreso_de_venta": obtener_fecha_actual(),
        "mes_de_venta" : mes_de_venta,
        "codigo_producto": codigo_producto,  
        "cantidad_vendida": cantidad_vendida,
    }

    print("Venta generada: {codigo_venta}")

def obtener_fecha_actual():
    return date.today().isoformat()   # YYYY-MM-DD

# Aqui se ingresan las ventas por vendedor, cada vez que se genere una venta. Esto lo hace cada vendedor

def ingresar_venta():
    "codigo_vendedor" = codigo_vendedor,
    "id_venta"= generar_codigo_venta(),
    "fecha_de_ingreso_de_venta"= obtener_fecha_actual(),
    "mes_de_venta" = mes,
    "codigo_producto" = codigo_producto,  
    "cantidad_vendida" = cantidad_vendida
    
    with open('vendedor.json', 'r', encoding='utf-8') as f:
        datos_cargados = json.load(f)
    
    codigo_vendedor = pedir_texto("Ingrese el código del vendedor: ")
    if codigo_vendedor not in datos_cargados:
        print("Vendedor no encontrado.")
        return

    mes = pedir_texto("Ingresa el mes en que se realizó la venta: ").capitalize()
    if mes not in meses:
        print("Mes ingresado inválido.")
        return
    
    global codigo_producto
    global cantidad_vendida

    while True:
        codigo_producto = pedir_texto("Ingrese el código del producto vendido: ")
        cantidad_vendida = pedir_entero("Ingrese la cantidad de productos vendidos: ")

    # Validacion de stock
    with open('stock.json', 'r', encoding='utf-8') as f:
            datos_cargados = json.load(f)

    with open('producto.json', 'r', encoding='utf-8') as f:
            datos_cargados = json.load(f)        

        if not validar_stock(codigo_producto, cantidad_vendida):
            continue

    producto = productos[codigo_producto]

        precio_unitario = producto["costo"] + (producto["costo"]* margen)
        subtotal = precio_unitario * cantidad_vendida

        productos_venta = venta{"productos"}
        productos_venta.append({
            "codigo_producto": codigo_producto,
            "marca": producto["marca"],
            "modelo": producto["modelo"],
            "precio_unitario": precio_unitario,
            "cantidad": cantidad_vendida,
            "subtotal": subtotal
        })        
        venta["total_venta"] += subtotal

        descontar_stock(codigo_producto, cantidad_vendida)

        otro_producto = pedir_texto("¿Agregar otro producto? (s/n): ").lower()
        if otro_producto != "s":
            break

      #Aqui guardo el dicionario en un archivo .jason para facilitar los reportes
        with open('venta.json', 'w', encoding='utf-8') as f:
            json.dump(productos, f, indent=4) # indent4 para formato legible [3, 6]


# Aqui se muestran las ventas del vendedor
def mostrar_ventas_vendedor():
    if not os.path.exists('venta.json') or os.path.getsize('venta.json') == 0:
        print("No hay información de ventas.")
        return
    with open('venta.json', 'r') as f:
        datos_cargados = json.load(f)
        if not datos_cargados:
            print("No hay información de ventas para mostrar.")
        else:
            print(datos_cargados)


# Aqui se eliminan las ventas
def eliminar_venta():
    with open('venta.json', 'r', encoding='utf-8') as f:
        datos_cargados = json.load(f)
    codigo = generar_id_venta("Ingrese el código de la venta a eliminar: ")
    if codigo not in datos_cargados:
        print("Venta no encontrada.")
        return

    confirmacion = input(f"¿Está seguro de que desea eliminar esta venta {codigo}? (si/no): ").lower()
    if confirmacion == "si":
        del datos_cargados[codigo]

        # Aqui actualizamos el archivo .json
        with open('venta.json', 'w', encoding='utf-8') as f:
            json.dump(datos_cargados, f, indent=4)
        print("Venta eliminado correctamente.")
    else:
            print("Eliminación cancelada.")

    codigo_vendedor = pedir_texto("Código vendedor: ")

    if codigo_vendedor not in vendedor:
        print("Vendedor no existe")
        return

    ventas_vendedor = vendedor[codigo_vendedor]["ventas"]

    if not ventas_vendedor:
        print("No tiene ventas")
        return

    for mes, lista in ventas_vendedor.items():
        for venta in lista:
            print(f"{venta['id_venta']} | {mes} | {venta['fecha']} | {venta['total_venta']}")

    id_eliminar = pedir_texto("ID venta a eliminar: ")

    for mes, lista in ventas_vendedor.items():
        for venta in lista:
            if venta["id_venta"] == id_eliminar:
                for prod in venta["productos"]:
                    productos[prod["codigo_producto"]]["cantidad"] += prod["cantidad"]

                lista.remove(venta)
                print("Venta eliminada correctamente")
                return

    print("Venta no encontrada")

"""
ingresar_venta()
#mostrar_ventas_vendedor()
#eliminar_venta()