### Sistema de Gestión de Productos ###

# 1. Descripción general del sistema
El Sistema de Gestión de Productos es una aplicación desarrollada en Python cuyo objetivo es permitir el registro, modificación, consulta y eliminación de datos relacionados con productos, proveedores y validaciones del inventario, a través de un menú interactivo por consola.
El sistema está diseñado para cubrir necesidades básicas de gestión comercial, incluyendo el control de stock, análisis de ventas, generación de rankings y validaciones de datos para asegurar la consistencia de la información ingresada por el usuario.
El proyecto utiliza una arquitectura modular, separando la lógica de negocio de las funciones de validación, lo que facilita la mantenibilidad, escalabilidad y legibilidad del código.

# 2. Funcionalidades Implementadas
## 2.1 Gestión de Productos

*agregar_productos*: Registra nuevos productos en el sistema, almacenando su información básica como nombre, precio y stock.
*mostrar_productos*: Muestra el listado completo de productos registrados.
*eliminar_producto*: Elimina un producto del sistema, siempre que cumpla con las validaciones establecidas.
*validar_stock*: Verifica que el stock disponible sea suficiente antes de realizar una venta.
*alertas_stock_bajo*: Genera alertas cuando el stock de un producto se encuentra por debajo del mínimo permitido.
*productos_sin_ventas*: Identifica productos que no registran ventas durante un período determinado.
*cantidad_vendida_por_producto*: Calcula la cantidad total de unidades vendidas por cada producto.
*producto_mas_vendido_anual*: Determina el producto con mayor cantidad de ventas a lo largo del año.
*ventas_por_producto*: Muestra las ventas asociadas a cada producto.
*ingresos_producto_mes*: Calcula los ingresos generados por un producto en un mes específico.
*comparativo_mensual_producto*: Compara las ventas mensuales de un producto entre distintos períodos.
*crecimiento_mensual_producto*: Analiza el crecimiento o disminución de ventas mensuales de un producto.
*ranking_productos_ingresos*: Genera un ranking de productos según los ingresos obtenidos.
*gerencia_producto*: Permite asignar o gestionar productos según la gerencia correspondiente.


## 2.2 Gestión de Proveedores

*agregar_proveedor*: Registra nuevos proveedores en el sistema.
*mostrar_proveedor*: Muestra el listado de proveedores registrados.
*eliminar_proveedor*: Elimina un proveedor del sistema.


## 2.3 Gestión de Vendedores

*agregar_vendedor*: Registra nuevos vendedores en el sistema.
*mostrar_vendedor*: Muestra el listado de vendedores registrados.
*eliminar_vendedor*: Elimina un vendedor, validando que no tenga dependencias asociadas.
*ingresar_o_modificar_metas_mes_vendedor*: Permite ingresar o modificar las metas mensuales de cada vendedor.
*mostrar_metas_vendedor*: Muestra las metas asignadas a los vendedores.
*productos_vendidos_por_vendedor_mes*: Muestra los productos vendidos por cada vendedor en un mes específico.


## 2.4 Gestión de Ventas

*ingresar_venta*: Registra una venta asociada a un vendedor y a un producto.
*mostrar_ventas_vendedor*: Muestra las ventas realizadas por un vendedor.
*eliminar_venta*: Elimina una venta previamente registrada.
*ventas_por_gerencia*: Muestra las ventas agrupadas según la gerencia correspondiente.
*ingresos_producto_mes*: Calcula los ingresos generados por un producto en un período determinado.


# 3. Funciones de Validación

*Validación de texto*: Evita el ingreso de campos vacíos o con valores inválidos.
*Validación de números enteros*: Verifica que los valores ingresados sean enteros válidos.
*Validación de números decimales*: Controla el ingreso correcto de valores numéricos decimales.
*Validación de RUT*: Verifica que el RUT ingresado tenga un formato válido.
*Validación de stock*: Controla la disponibilidad de stock antes de registrar una venta.
*Validación de metas*: Verifica que las metas mensuales ingresadas sean coherentes.
*Validación de eliminación*: Impide eliminar productos o vendedores que tengan ventas asociadas.


# 4 . Estructuras de datos utilizadas

El sistema utiliza principalmente:
- Listas: para almacenar productos, proveedores, vendedores y ventas.
- Diccionarios: para representar entidades con múltiples atributos (por ejemplo, producto, vendedor).
- Funciones modulares: para reutilizar lógica y evitar duplicación de código.

Link a github: https://github.com/cecimila22/ABP-3