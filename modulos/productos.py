from gestion_de_datos.validaciones import pedir_texto, pedir_decimal, pedir_entero
import json
import os


######### PRODUCTOS #########
archivo_productos = 'producto.json'
archivo_stock ='stock.json'

### Aquí se cargan los productos existentes desde el JSON al iniciar para no perder datos
def cargar_productos():
    if os.path.exists(archivo_productos) and os.path.getsize(archivo_productos) > 0:
        with open(archivo_productos, 'r', encoding='utf-8') as f:
           return json. load(f)
    return {}

productos = cargar_productos()

def generar_codigo_producto(proveedor, tipo, marca, modelo, costo, cantidad, ubicacion):
    global codigo_producto

    contador_actual_producto = len(productos) + 1
    codigo_producto = f"Prod{contador_actual_producto:03d}"

    ### Aquí validamos si el codigo de producto existe, para no sobreescribir
    while codigo_producto in productos:
        contador_actual_producto += 1
        codigo_producto = f"Prod{contador_actual_producto:03d}"
    
        print("Código de producto generado: ", codigo_producto)

    productos[codigo_producto] = {
        "codigo_producto" : codigo_producto,
        "proveedor": proveedor,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "costo": costo,
        "cantidad": cantidad,
        "ubicacion": ubicacion
    }    

### Aquí se ingresa el producto (Esto lo hace Compras)
def agregar_productos():
    proveedor = pedir_texto("Ingresa la Razón social del proveedor: ")
    tipo = pedir_texto("Ingresa el tipo de producto: ")
    marca = pedir_texto("Ingresa la marca: ")
    modelo = pedir_texto("Ingresa el modelo: ")
    costo = pedir_decimal("Ingresa el costo: $")
    cantidad = pedir_entero("Ingresa la cantidad: ")
    ubicacion = pedir_texto("Ingresa la ubicación en donde sera almacenado: ")

    generar_codigo_producto(proveedor, tipo, marca, modelo, costo, cantidad, ubicacion)

    #Aqui guardo producto en el dicionario en un archivo .jason para facilitar los reportes
    with open(archivo_productos, 'w', encoding='utf-8') as f:
        json.dump(productos, f, indent=4, ensure_ascii=False)
    print("Producto agregado con éxito")    

    cargar_stock()
  
    #Aqui guardo el ingreso de los productos en stock en un archivo .jason para facilitar los reportes
    with open(archivo_stock, 'w', encoding='utf-8') as f:
        json.dump(productos, f, indent=4, ensure_ascii=False)
    print("Producto agregado a stock con éxito")      

def cargar_stock():
    if os.path.exists(archivo_stock) and os.path.getsize(archivo_stock) > 0:
        with open(archivo_stock, 'r', encoding='utf-8') as f:
            return json. load(f)
    return {}

    

stock = cargar_stock

   
### Aquí se muestran los productos ingresados
def mostrar_productos():
    datos = cargar_productos()
    if not datos:
        print("No hay información de productos")
        return

    for cod, info in datos.items():
            print(f"ID: {cod} | {info['tipo']} {info['marca']} - Stock: {info['cantidad']}")

# Aqui se eliminan los productos
def eliminar_producto():
    global productos # Usamos el diccionario global

    if not productos:
            print("No hay información de productos")
            return
                
    codigo = input("Ingrese el código del producto a eliminar (ej. Prod001): ")
        
    if codigo in productos:
        confirmacion = input(f"¿Eliminar {codigo}? (si/no): ").lower()
        if confirmacion == "si":
            del productos[codigo]
            with open(archivo_productos, 'w', encoding='utf-8') as f:
                json.dump(productos, f, indent=4, ensure_ascii=False)
                print("Producto eliminado")
        else:
            print("Eliminación cancelada")
    else:
        print("Código no encontrado")


