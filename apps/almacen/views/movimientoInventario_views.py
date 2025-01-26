from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import MovimientoInventario, Producto

def listar_movimientos(request):
    movimientos = MovimientoInventario.objects.all()
    productos = Producto.objects.all()
    context = {
        'movimientos': movimientos,
        'productos': productos,
    }
    return render(request, 'inventario/movimientos.html', context)

def crear_movimiento(request):
    if request.method == 'POST':
        fk_id_producto = request.POST['fk_id_producto']
        tipo_movimiento = request.POST['tipo_movimiento']
        cantidad = request.POST['cantidad']
        descripcion_movimiento = request.POST['descripcion_movimiento']

        producto = Producto.objects.get(id=fk_id_producto)

        # Validar stock en caso de salida
        if tipo_movimiento == 'S' and producto.stock_prod < int(cantidad):
            messages.error(request, 'No hay suficiente stock para realizar esta salida.')
            return redirect('movimientos')

        # Crear el movimiento
        MovimientoInventario.objects.create(
            fk_id_producto=producto,
            tipo_movimiento=tipo_movimiento,
            cantidad=cantidad,
            descripcion_movimiento=descripcion_movimiento
        )

        '''
        # Actualizar el stock del producto
        if tipo_movimiento == 'E':
            producto.stock_prod += int(cantidad)
        else:
            producto.stock_prod -= int(cantidad)
        producto.save()
        '''

        messages.success(request, 'Movimiento creado correctamente.')
        return redirect('movimientos')

def eliminar_movimiento(request, id):
    movimiento = MovimientoInventario.objects.get(id=id)

    '''
    # Revertir el movimiento
    if movimiento.tipo_movimiento == 'E':
        movimiento.fk_id_producto.stock_prod -= movimiento.cantidad
    else:
        movimiento.fk_id_producto.stock_prod += movimiento.cantidad
    movimiento.fk_id_producto.save()
    '''

    movimiento.delete()
    messages.success(request, 'Movimiento eliminado correctamente.')
    return redirect('movimientos')
    


def editar_movimiento(request, id):
    movimiento = MovimientoInventario.objects.get(id=id)
    productos = Producto.objects.all()
    context = {
        'movimiento': movimiento,
        'productos': productos,
    }
    return render(request, 'inventario/editar_movimiento.html', context)

def procesar_editar_movimiento(request):
    if request.method == 'POST':
        movimiento_id = request.POST['id']
        fk_id_producto = request.POST['fk_id_producto']
        tipo_movimiento = request.POST['tipo_movimiento']
        cantidad = request.POST['cantidad']
        descripcion_movimiento = request.POST['descripcion_movimiento']

        movimiento = MovimientoInventario.objects.get(id=movimiento_id)
        producto = Producto.objects.get(id=fk_id_producto)

        # Revertir el movimiento anterior
        if movimiento.tipo_movimiento == 'E':
            movimiento.fk_id_producto.stock_prod -= movimiento.cantidad
        else:
            movimiento.fk_id_producto.stock_prod += movimiento.cantidad

        # Validar stock en caso de salida
        if tipo_movimiento == 'S' and producto.stock_prod < int(cantidad):
            messages.error(request, 'No hay suficiente stock para realizar esta salida.')
            return redirect('movimientos')

        # Actualizar el movimiento
        movimiento.fk_id_producto = producto
        movimiento.tipo_movimiento = tipo_movimiento
        movimiento.cantidad = cantidad
        movimiento.descripcion_movimiento = descripcion_movimiento
        movimiento.save()

        # Aplicar el nuevo movimiento
        if tipo_movimiento == 'E':
            producto.stock_prod += int(cantidad)
        else:
            producto.stock_prod -= int(cantidad)
        producto.save()

        messages.success(request, 'Movimiento actualizado correctamente.')
        return redirect('movimientos')