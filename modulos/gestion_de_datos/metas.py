from datos_basicos import margen, meses, gerencias  #Validar que voy a usar de aqui
from validaciones import pedir_texto, pedir_decimal
from vendedores import vendedor

######### METAS #########
# Aqui se ingresan las metas por gerencia por mes por vendedor Esto lo hace el gerente

def ingresar_metas_mes_vendedor(): 
    codigo = pedir_texto("Ingrese el código del vendedor (ej: vend001): ")
    
    if codigo not in vendedor:
        print("Vendedor no encontrado.")
        return

    for mes in meses:
        meta = pedir_decimal(f"Meta para {mes}: ")
        vendedor[codigo]["metas"][mes] = meta

    print("Metas ingresadas / actualizadas correctamente.")
    
    #Aqui guardo el dicionario en un archivo .jason para facilitar los reportes
    with open('producto.json', 'w', encoding='utf-8') as f:
        json.dump(productos, f, indent=4) # indent4 para formato legible [3, 6]
   
def mostrar_metas_vendedor():
    for cod_vend, datos in vendedor.items():
        print(f"\nVendedor: {cod_vend} - {datos['nombre_completo']}")

        if not datos["metas"]:
            print("  Sin metas registradas")
            continue

        for mes in meses:
            if mes in datos["metas"]:
                print(f"  Meta de {mes}: $ {datos['metas'][mes]:,.0f}")


ingresar_metas_mes_vendedor()