from productos import productos
import json
import os

######### INVENTARIO #########
stock_minimo = 2
archivo_stock ='stock.json'

# Aquí validamos el stock 
def mostrar_stock():
    if os.path.exists(archivo_stock) and os.path.getsize(archivo_stock) > 0:
        with open(archivo_stock, 'r', encoding='utf-8') as f:
           return json. load(f)
    
    with open(archivo_stock, "r", encoding="utf-8") as archivo:  
        datos = json.load(archivo)

    for cod, info in datos:
        print(f"ID: {cod} | {info['tipo']} {info['marca']} - Stock: {info['cantidad']}")

   
# print (f"El stock disponible del producto ,, "es" , cantidad)

# Aquí descontamos el stock
def descontar_stock(codigo_producto, cantidad_vendida):
    if not productos(codigo_producto, cantidad_vendida):
        return False

    productos[codigo_producto]["cantidad"] -= cantidad_vendida
    return True

# Aquí detectamos stock mínimo
def alertas_stock_bajo():
    print("\nProductos con stock bajo")

    hay_alertas = False

    for codigo, prod in productos.items():
        if prod["cantidad"] <= stock_minimo:
            print(
                f"{codigo} | {prod['marca']} {prod['modelo']} | "
                f"Stock: {prod['cantidad']}"
            )
            hay_alertas = True

    if not hay_alertas:
        print("No hay productos con stock bajo")
