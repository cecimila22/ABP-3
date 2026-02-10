from gestion_de_datos.datos_basicos import margen, gerencias, meses 
from gestion_de_datos.validaciones import pedir_texto, pedir_rut
from typing import Dict, List
import json
import os

######### VENDEDORES #########
archivo_vendedores = 'vendedor.json'

### Aquí se cargan los vendedores existentes desde el JSON al iniciar para no perder datos
def cargar_vendedores():
    if os.path.exists(archivo_vendedores) and os.path.getsize(archivo_vendedores) > 0:
        with open(archivo_vendedores, 'r', encoding='utf-8') as f:
            return json. load(f)
    return {}

vendedores = cargar_vendedores()

def generar_codigo_vendedor(nombre_completo, run_vendedor, gerencia):
    contador_actual_vendedor = len(vendedores) + 1
    codigo_vendedor = f"Vend{contador_actual_vendedor:03d}"

    ### Aquí validamos si el codigo de vendedor existe, para no sobreescribir
    while codigo_vendedor in vendedores:
        contador_actual_vendedor += 1
        codigo_vendedor = f"Vend{contador_actual_vendedor:03d}"

    vendedores[codigo_vendedor] = {
        "codigo_vendedor" : codigo_vendedor,
        "nombre_completo": nombre_completo,
        "run_vendedor": run_vendedor,
        "gerencia": gerencia,
        "ventas": {}, # ventas por mes
        "metas": {}  # metas por mes
    }
    
    print(f"Vendedor generado: {codigo_vendedor}")

#Aquí se ingresa el vendedor a las gerencias de venta, con su codigo (Esto lo hace el gerente)

def agregar_vendedor():
    nombre_completo = pedir_texto("Ingresa el nombre_completo: " )
    run_vendedor = pedir_rut("Ingrese RUN del vendedor, con puntos y guión: ")
    gerencia = pedir_texto("Ingresa la gerencia a la que pertenece el vendedor: ").strip().upper() # Evita errores de escritura mayusculas y minusculas
    prefijo_gerencia = gerencia[:3]
    ventas_mes : 0
    metas_mes :0
    codigo_vendedor = generar_codigo_vendedor(nombre_completo, run_vendedor, gerencia)
    
    #Aqui guardo vendedor en el dicionario en un archivo .jason para facilitar los reportes
    with open(archivo_vendedores, 'w', encoding='utf-8') as f:
        json.dump(vendedores, f, indent=4, ensure_ascii=False)
    print("Vendedor agregado con éxito")

### Aquí se muestran los vendedores
def mostrar_vendedores():
    datos = cargar_vendedores()
    if not datos:
        print("No hay información de vendedores")
        return

    for cod, info in datos.items():
            print(f"ID: {cod} | {info['nombre_completo']} {info['run_vendedor']} - {info['gerencia']}- {info['ventas']}- {info['metas']}")

# Aqui se eliminan los vendedores
def eliminar_vendedor():
    global vendedores

    if not vendedores:
        print("No hay información de vendedores")
        return
                
    codigo = input("Ingrese el código del vendedor a eliminar (ej. Vend001): ")

    if codigo in vendedores:
        confirmacion = input(f"¿Eliminar {codigo}? (si/no): ").lower()
        if confirmacion == "si":
            del vendedores[codigo]
            with open(archivo_vendedores, 'w', encoding='utf-8') as f:
                json.dump(vendedores, f, indent=4, ensure_ascii=False)
                print("vendedor eliminado")
        else:
            print("Eliminación cancelada")
    else:
        print("Código no encontrado")


