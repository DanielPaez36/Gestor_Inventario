from django.shortcuts import render
from ..models import Detalle_Venta, Venta

def detalles(request, id):
    venta = Venta.objects.get(id=id)
    detalles = Detalle_Venta.objects.filter(fk_id_venta=venta)
    cantidad = int(venta.total_venta / venta.fk_id_producto.precio_prod)
    
    context = {
        'venta': venta,
        'detalles': detalles,
        'cantidad': cantidad
    }
    return render(request, 'detalle/detalles.html', context)