import pandas as pd
from django.http import HttpResponse
from ..models import Categoria, Proveedor, Producto, Venta, Detalle_Venta, Compra, Detalle_Compra, MovimientoInventario

def exportar_movimientos_excel(request):
    # Crear un diccionario para almacenar los DataFrames de cada modelo
    dataframes = {}

    # Categoría
    categorias = Categoria.objects.all().values()
    dataframes['Categorias'] = pd.DataFrame(categorias)

    # Proveedor
    proveedores = Proveedor.objects.all().values()
    dataframes['Proveedores'] = pd.DataFrame(proveedores)

    # Producto
    productos = Producto.objects.all().values()
    dataframes['Productos'] = pd.DataFrame(productos)

    # Venta
    ventas = Venta.objects.all().values()
    dataframes['Ventas'] = pd.DataFrame(ventas)

    # Detalle Venta
    detalles_venta = Detalle_Venta.objects.all().values()
    dataframes['Detalle_Ventas'] = pd.DataFrame(detalles_venta)

    # Compra
    compras = Compra.objects.all().values()
    dataframes['Compras'] = pd.DataFrame(compras)

    # Detalle Compra
    detalles_compra = Detalle_Compra.objects.all().values()
    dataframes['Detalle_Compras'] = pd.DataFrame(detalles_compra)

    # Movimiento Inventario
    movimientos = MovimientoInventario.objects.all().values()
    dataframes['Movimientos_Inventario'] = pd.DataFrame(movimientos)

    # Crear un archivo Excel con varias hojas
    with pd.ExcelWriter('archivo_general.xlsx', engine='xlsxwriter') as writer:
        for sheet_name, df in dataframes.items():
            if not df.empty:
                df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Leer el archivo generado
    with open('archivo_general.xlsx', 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="archivo_general.xlsx"'
        return response