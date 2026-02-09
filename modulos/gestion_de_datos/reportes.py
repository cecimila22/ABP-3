from datos_basicos import ventas, vendedores, meses, meses_num
from vendedores import vendedores
from productos import productos
from gestion_de_datos.reportes import ventas_por_producto
from gestion_de_datos.reportes import ventas_por_gerencia
from gestion_de_datos.reportes import gerencia_producto
from gestion_de_datos.reportes import ingresos_por_producto
from gestion_de_datos.reportes import ingresos_producto_mes
from gestion_de_datos.reportes import productos_vendidos_por_vendedor_mes
from gestion_de_datos.reportes import ranking_productos_ingresos
from gestion_de_datos.reportes import producto_mas_vendido_anual
from gestion_de_datos.reportes import cantidad_vendida_por_producto
from gestion_de_datos.reportes import comparativo_mensual_producto
from gestion_de_datos.reportes import crecimiento_mensual_producto
from gestion_de_datos.reportes import productos_sin_ventas

####### HAY QUE MANDAR A IMPRIMIR LOS REPORTES #########

######### Reporte de ventas por productos #########
def ventas_por_producto():
    reporte = {}

    for venta in ventas:
        for producto in venta["productos"]:
            codigo = producto["codigo_producto"]
            subtotal = producto["subtotal"]

            if codigo not in reporte:
                reporte[codigo] = {
                    "cantidad": 0,
                    "ingresos": 0
                }

            reporte[codigo]["cantidad"] += producto["cantidad"]
            reporte[codigo]["ingresos"] += subtotal

    return reporte
    imprimir_reporte_ventas_por_producto(producto)

 
######### Reporte de ventas por gerencia #########
def ventas_por_gerencia():
    reporte = {}

    for venta in ventas:
        cod_vendedor = venta["codigo_vendedor"]
        gerencia = vendedores[cod_vendedor]["gerencia"]
        total = venta["total"]

        reporte[gerencia] = reporte.get(gerencia, 0) + total

    return reporte
    imprimir_reporte_ventas_por_gerencia(reporte)
    
######### Reporte de ventas por gerencia, por producto #########
def gerencia_producto():
    reporte = {}

    for venta in ventas:
        cod_vendedor = venta["codigo_vendedor"]
        gerencia = vendedores[cod_vendedor]["gerencia"]

        for prod in venta["productos"]:
            cod = prod["codigo_producto"]

            if gerencia not in reporte:
                reporte[gerencia] = {}

            if cod not in reporte[gerencia]:
                reporte[gerencia][cod] = {"cantidad": 0, "ingresos": 0}

            reporte[gerencia][cod]["cantidad"] += prod["cantidad"]
            reporte[gerencia][cod]["ingresos"] += prod["subtotal"]

    return reporte    
 
######### INGRESOS POR PRODUCTO Y POR MES #########
def ingresos_producto_mes(codigo_producto, mes):
    total = 0

    for venta in ventas:
        # extraemos el mes desde la fecha (YYYY-MM-DD)
        mes_venta = str(venta["fecha"]).split("-")[1]


        # convertimos número a nombre de mes
        if meses_num.get(mes_venta) != mes:
            continue

        for prod in venta["productos"]:
            if prod["codigo_producto"] == codigo_producto:
                total += prod["subtotal"]

    return total

######### PRODUCTOS VENDIDOS POR VENDEDOR, POR MES #########
def productos_vendidos_por_vendedor_mes(mes):
    reporte_prod_vend_vendedor_mes = {}

    for venta in ventas:
        fecha = str(venta["fecha"])
        mes_venta = meses[int(fecha.split("-")[1]) - 1]

        if mes_venta != mes:
            continue

        cod_vendedor = venta["codigo_vendedor"]

        if cod_vendedor not in reporte_prod_vend_vendedor_mes:
            reporte_prod_vend_vendedor_mes[cod_vendedor] = {}

        for prod in venta["productos"]:
            cod_prod = prod["codigo_producto"]
            cantidad = prod["cantidad"]

            reporte_prod_vend_vendedor_mes[cod_vendedor][cod_prod] = (
                reporte_prod_vend_vendedor_mes[cod_vendedor].get(cod_prod, 0) + cantidad
            )

    return reporte_prod_vend_vendedor_mes



"""######### VENDEDOR TOP POR PRODUCTO Y MES #########
def vendedor_top_por_producto_mes(mes):
    acumulado = {}

    for venta in ventas:
        mes_venta = meses[int(str(venta["fecha"]).split("-")[1]) - 1]
        if mes_venta != mes:
            continue

        for prod in venta["productos"]:
            cod = prod["codigo_producto"]
            vend = venta["codigo_vendedor"]

            acumulado.setdefault(cod, {})
            acumulado[cod][vend] = acumulado[cod].get(vend, 0) + prod["cantidad"]

    return acumulado
"""

######### RANKING DE PRODUCTOS POR INGRESOS #########
def ranking_productos_ingresos():
    ingresos = ingresos_por_producto()
    ranking = sorted(ingresos.items(), key=lambda x: x[1], reverse=True)
    return ranking

#### OJO VALIDAR LAS SIGUIENTES FUNCIONES
######### PRODUCTO MÁS VENDIDO DEL AÑO POR INGRESOS #########
def producto_mas_vendido_anual():
    ingresos = ingresos_por_producto()
    if not ingresos:
        return None
    cod_max = max(ingresos, key=ingresos.get)
    return cod_max, ingresos[cod_max]
    
######### PRODUCTOS MÁS VENDIDO POR CANTIDAD #########
def cantidad_vendida_por_producto():
    cantidades = {}

    for venta in ventas:
        for prod in venta["productos"]:
            cod = prod["codigo_producto"]
            cantidades[cod] = cantidades.get(cod, 0) + prod["cantidad"]

    return cantidades

######### COMPARATIVO DE VENTAS MENSUAL POR PRODUCTO #########
def comparativo_mensual_producto(codigo_producto):
    comparativo = {mes: 0 for mes in meses}

    for venta in ventas:
        # extraer mes desde fecha YYYY-MM-DD
        mes_num = str(venta["fecha"]).split("-")[1]
        mes_nombre = meses_num.get(mes_num)

        if mes_nombre not in comparativo:
            continue

        for prod in venta["productos"]:
            if prod["codigo_producto"] == codigo_producto:
                comparativo[mes_nombre] += prod["subtotal"]

    return comparativo

######### CRECIMIENTO MES A MES (%) – VENTAS POR PRODUCTO #########
def crecimiento_mensual_producto(codigo_producto):
    comparativo = comparativo_mensual_producto(codigo_producto)
    crecimiento = {}

    meses_ordenados = meses

    for i in range(1, len(meses_ordenados)):
        mes_actual = meses_ordenados[i]
        mes_anterior = meses_ordenados[i - 1]

        valor_actual = comparativo[mes_actual]
        valor_anterior = comparativo[mes_anterior]

        if valor_anterior == 0:
            crecimiento[mes_actual] = None
        else:
            crecimiento[mes_actual] = ((valor_actual - valor_anterior) / valor_anterior) * 100

    return crecimiento

######### REPORTE DE PRODUCTOS SIN VENTAS #########
def productos_sin_ventas():
    ingresos = ingresos_por_producto()
    sin_ventas = []

    for cod in productos:
        if ingresos.get(cod, 0) == 0:
            sin_ventas.append(cod)

    return sin_ventas
