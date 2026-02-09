import json
import os
from datetime import date # Aqui obtenemos la fecha de hoy
from validaciones import pedir_texto, pedir_entero, pedir_decimal
from datos_basicos import margen, gerencias, meses


######### VENTAS #########
archivo_ventas = 'venta.json'
archivo_productos = 'producto.json'
archivo_vendedor= 'vendedor.json'
archivo_stock ='stock.json'

ventas = {}
contador_venta = 1

### Aquí se cargan las ventas desde el JSON 
def cargar_ventas():
    if os.path.exists(archivo_ventas) and os.path.getsize(archivo_ventas) > 0:
        with open(archivo_ventas, 'r', encoding='utf-8') as f:
            return json. load(f)
    return {}

ventas = cargar_ventas()

# Se genera un id para identificar esa venta
def generar_id_venta (codigo_vendedor,fecha_de_ingreso_de_venta,mes_de_venta,productos,total_venta):
    global id_venta
    global contador_actual_venta

    contador_actual_venta = len(ventas) + 1
    id_venta = f"Vent{contador_actual_venta:03d}"

    ### Aquí validamos si el id de venta existe, para no sobreescribir
    while id_venta in ventas:
        contador_actual_venta += 1
        id_venta = f"Vent{contador_actual_venta:03d}"

    print("Código de venta generada con código: ", id_venta)

    ventas[id_venta]= { 
        "codigo_vendedor" : codigo_vendedor,
        "fecha_de_ingreso_de_venta": obtener_fecha_actual(),
        "mes_de_venta" : mes_de_venta,
        "codigo_producto": codigo_producto,  
        "cantidad_vendida": cantidad_vendida
    }   

def obtener_fecha_actual():
    return date.today().isoformat()   # YYYY-MM-DD

# Aqui se ingresan las ventas por vendedor, cada vez que se genere una venta. Esto lo hace cada vendedor
def ingresar_venta():
    global cantidad_vendida
    global id_venta
    global codigo_producto

    with open(archivo_vendedor, 'r', encoding='utf-8') as f:
        datos_cargados_vendedor = json. load(f)
    
    while True:
        codigo_vendedor = pedir_texto("Ingrese el código del vendedor: ")
        if codigo_vendedor in datos_cargados_vendedor:
            print("Vendedor validado")
            break
        else:
            print("Vendedor no encontrado, intente de nuevo")
                        
    while True:
        mes_de_venta = pedir_texto("Ingresa el mes en que se realizó la venta: ").capitalize()
        if mes_de_venta in meses:
            break
        else:
            print("Mes ingresado inválido, intente de nuevo")
              
    while True:
        codigo_producto = pedir_texto("Ingrese el código del producto vendido: ")
        if codigo_vendedor in datos_cargados_vendedor:
            break
        else:
            print("Codigo de producto no encontrado, intente de nuevo")
    
    cantidad_vendida = pedir_entero("Ingrese la cantidad de productos vendidos: ")  

    # Aqui calculamos el precio de la venta
    with open(archivo_productos, 'r', encoding='utf-8') as f:
        datos_cargados_producto = json.load(f)
    
    producto_vendido = datos_cargados_producto[codigo_producto]
    precio_unitario = producto_vendido["costo"] + (producto_vendido["costo"] * margen)
    total_venta = precio_unitario * cantidad_vendida

    print("La venta total es de : ", total_venta)

    generar_id_venta (codigo_vendedor,mes_de_venta,codigo_producto,total_venta,cantidad_vendida)

    #Aqui guardo la venta en el dicionario en un archivo .jason para facilitar los reportes
    
    if os.path.exists(archivo_ventas) and os.path.getsize(archivo_ventas) > 0:
        with open(archivo_ventas, 'w', encoding='utf-8') as f:
            json. dump(archivo_ventas, f, indent=4, ensure_ascii=False)
    
    print("Venta ingresada con éxito")    

    #validar_stock(codigo_producto, cantidad_vendida)
    #descontar_stock(codigo_producto, cantidad_vendida)

    #Aqui guardo el dicionario en un archivo .jason para facilitar los reportes
    with open(archivo_ventas, 'w', encoding='utf-8') as f:
            json.dump(ventas, f, indent=4) # indent4 para formato legible [3, 6]

# Aqui se muestran las ventas del vendedor
def mostrar_ventas():
    datos = cargar_ventas()
    if not datos:
        print("No hay ventas registradas")
        return

    for codigo, info in datos.items():
        print(
            f"{codigo} | "
            f"{info['fecha_de_ingreso_de_venta']} | "
            f"{info['mes_de_venta']} | "
            f"{info['codigo_producto']} | "
            f"{info['cantidad_vendida']} | "
        )

# Aqui se eliminan las ventas
def eliminar_venta():
    global ventas 
                
    codigo = input("Ingrese el id_venta a eliminar: ")

    if codigo not in ventas:
        print("Código no encontrado")
        return
    confirmacion = input(f"¿Seguro que desea eliminar la venta {codigo}? (si/no): ").lower()
    if confirmacion == "si":
            del ventas[codigo]
            with open(archivo_productos, 'w', encoding='utf-8') as f:
                json.dump(ventas, f, indent=4, ensure_ascii=False)
                print("Producto eliminado")
    else:
        print("Eliminación cancelada.")






