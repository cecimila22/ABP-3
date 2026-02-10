import json
import os
from datetime import date # Aqui obtenemos la fecha de hoy
from gestion_de_datos.validaciones import pedir_texto, pedir_entero, pedir_decimal
from gestion_de_datos.datos_basicos import margen, gerencias, meses
######### METAS #########
# Aqui se ingresan las metas por gerencia por mes por vendedor Esto lo hace el gerente

archivo_metas = 'meta.json'
archivo_vendedor= 'vendedor.json'

meta_vendedor = {}
contador_meta = 1

def cargar_metas():
    if os.path.exists(archivo_metas) and os.path.getsize(archivo_metas) > 0:
        with open(archivo_metas, 'r', encoding='utf-8') as f:
            return json. load(f)
    return {}

metas = cargar_metas()

 
# Aqui se ingresan las metas por vendedor, esto solo lo hace el gerente
def ingresar_metas_mes_vendedor(): 

    with open(archivo_vendedor, 'r', encoding='utf-8') as f:
        datos_cargados_vendedor = json. load(f)

    while True:
        codigo_vendedor = pedir_texto("Ingrese el código del vendedor al que se le cargará la meta(ej: Vend001):")
        if codigo_vendedor in datos_cargados_vendedor:
            print("Vendedor validado")
            break
        else:
            print("Vendedor no encontrado, intente de nuevo")

    while True:
        mes_de_meta = pedir_texto("Ingresa el mes en que se asignará la meta: ").capitalize()
        if mes_de_meta in meses:
            monto_meta = pedir_entero("Ingrese el monto de la meta: $")
            break
        else:
            print("Mes ingresado inválido, intente de nuevo")

    meta_vendedor[codigo_vendedor]= { 
        "mes_de_meta": mes_de_meta,
        "monto_meta": monto_meta    
    }
   

    print("Metas ingresadas / actualizadas correctamente.")
    
    #Aqui guardo el dicionario en un archivo .jason para facilitar los reportes
    with open(archivo_metas, 'w', encoding='utf-8') as f:
        json.dump(meta_vendedor, f, indent=4) # indent4 para formato legible [3, 6]
   
def mostrar_metas():
    datos = cargar_metas()
    if not datos:
        print("No hay metas registradas")
        return

    for codigo, info in datos.items():
        print(
            f"{codigo} | "
            f"{info['mes_de_meta']} | "
            f"{info['monto_meta']} | "
        )


#ingresar_metas_mes_vendedor()
#mostrar_metas()