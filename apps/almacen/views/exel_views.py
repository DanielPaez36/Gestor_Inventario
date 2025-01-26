import pandas as pd
from django.http import HttpResponse
from ..models import MovimientoInventario

def exportar_movimientos_excel(request):
    # Obtener los movimientos desde la base de datos
    movimientos = MovimientoInventario.objects.select_related('fk_id_producto').all()

    # Crear un DataFrame con los datos
    data = [
        {
            'Producto': movimiento.fk_id_producto.nombre_prod,
            'Tipo de Movimiento': movimiento.get_tipo_movimiento_display(),
            'Cantidad': movimiento.cantidad,
            'Fecha': movimiento.fecha_movimiento,
        }
        for movimiento in movimientos
    ]
    df = pd.DataFrame(data)

    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="movimientos_inventario.xlsx"'

    # Exportar el DataFrame a Excel
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Movimientos')

    return response