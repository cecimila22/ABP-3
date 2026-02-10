from gestion_de_datos.validaciones import pedir_entero,pedir_texto, pedir_rut
import json
import os

######### PROVEEDORES #########
### Aquí se genera el código del proveedor
archivo_proveedores = 'proveedor.json'

def cargar_proveedores():
    if os.path.exists(archivo_proveedores) and os.path.getsize(archivo_proveedores) > 0:
        with open(archivo_proveedores, 'r', encoding='utf-8') as f:
            return json. load(f)
    return {}

proveedores = cargar_proveedores()

def generar_codigo_proveedor(razon_social,rut,telefono,direccion):
    contador_actual_proveedor = len(proveedores) + 1
    codigo_proveedor = f"Prov{contador_actual_proveedor:03d}" 
 ### Aquí validamos si el codigo de producto existe, para no sobreescribir
    while codigo_proveedor in proveedores:
        contador_actual_proveedor += 1
        codigo_proveedor = f"Prod{contador_actual_proveedor:03d}"

    proveedores[codigo_proveedor] = {
        "codigo_proveedor" : codigo_proveedor,
        "razon_social": razon_social,
        "rut": rut,
        "telefono": telefono,
        "direccion": direccion
    }

    print(f"Proveedor agredado con código: {codigo_proveedor}")
    
### Aquí se ingresa el proveedor (Esto lo hace Compras)
def agregar_proveedor():
    razon_social = pedir_texto("Ingresa el razon_social del proveedor: " )
    rut = pedir_rut("Ingrese RUT del proveedor, con puntos y guión: ")
    telefono = pedir_entero("Ingresa el telefono (+56276534567): ")
    direccion = pedir_direccion()

    generar_codigo_proveedor(razon_social,rut,telefono,direccion)

    #Aqui guardo el dicionario en un archivo .jason para facilitar los reportes
    with open(archivo_proveedores, 'w', encoding='utf-8') as f:
        json.dump(proveedores, f, indent=4, ensure_ascii=False) 

def pedir_direccion():
    return {
        "calle": pedir_texto("Calle / Avenida: "),
        "numero": pedir_texto("Número: "),
        "comuna": pedir_texto("Comuna: "),
        "ciudad": pedir_texto("Ciudad: ")
    }

### Aquí se muestran los proveedores
def mostrar_proveedores():
    datos = cargar_proveedores()
    if not datos:
        print("No hay información de proveedores")
        return

    for cod, info in datos.items():
            print(f"ID: {cod} | {info['razon_social']} {info['rut']} - {info['telefono']} - {info['direccion']}")

# Aqui se eliminan los proveedores
def eliminar_proveedor():
    global proveedores # Usamos el diccionario global

    if not proveedores:
            print("No hay información de proveedores")
            return
                
    codigo = input("Ingrese el código del proveedor a eliminar (ej. Prov001): ")
        
    if codigo in proveedores:
        confirmacion = input(f"¿Eliminar {codigo}? (si/no): ").lower()
        if confirmacion == "si":
            del proveedores[codigo]
            with open(archivo_proveedores, 'w', encoding='utf-8') as f:
                json.dump(proveedores, f, indent=4, ensure_ascii=False)
                print("Proveedor eliminado")
        else:
            print("Eliminación cancelada")
    else:
        print("Código no encontrado")


