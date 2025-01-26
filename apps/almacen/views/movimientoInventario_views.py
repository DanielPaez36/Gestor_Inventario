from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import MovimientoInventario, Producto

def listar_movimientos(request):
    movimientos = MovimientoInventario.objects.all()
    context = {
        'movimientos': movimientos,
    }
    return render(request, 'inventario/movimientos.html', context)

def eliminar_movimiento(request, id):
    movimiento = MovimientoInventario.objects.get(id=id)
    movimiento.delete()
    messages.success(request, 'Movimiento eliminado correctamente.')
    return redirect('movimientos')