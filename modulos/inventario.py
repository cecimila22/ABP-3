from productos import productos

######### INVENTARIO #########
stock_minimo = 3

# Aquí validamos el stock 
def validar_stock(codigo_producto, cantidad_vendida):
    if codigo_producto not in productos:
        print("Producto no existe.")
        return False

    if cantidad_vendida <= 0:
        print("La cantidad debe ser mayor a cero.")
        return False

    stock_disponible = productos[codigo_producto]["cantidad"]

    if cantidad_vendida > stock_disponible:
        print("Stock insuficiente.")
        return False

    return True    

# Aquí descontamos el stock
def descontar_stock(codigo_producto, cantidad_vendida):
    if not validar_stock(codigo_producto, cantidad_vendida):
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
        print("No hay productos con stock bajo.")


