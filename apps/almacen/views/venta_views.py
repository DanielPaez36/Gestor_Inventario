from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Venta, Producto, MovimientoInventario

def ventas(request):
    ventas = Venta.objects.all()
    productos = Producto.objects.all()
    context = {
        'ventas':ventas,
        'productos':productos
    }
    return render(request, 'venta/ventas.html', context)

def crear_venta(request):
    if request.method == 'POST':
        fecha = request.POST['fecha_venta']
        cantidad = int(request.POST['cantidad'])
        fk_id_producto = request.POST['productos']
        producto_selec = Producto.objects.get(id=fk_id_producto)

        if producto_selec.stock_prod < cantidad:
            messages.error(request, f"No hay suficiente stock para {producto_selec.nombre_prod}. Disponible: {producto_selec.stock_prod}.")
            return redirect('ventas')

        total = producto_selec.precio_prod * cantidad

        # Crear la venta
        Venta.objects.create(
            fecha_venta=fecha,
            total_venta=total,
            fk_id_producto=producto_selec
        )

        # Reducir el stock del producto
        producto_selec.stock_prod -= cantidad
        producto_selec.save()

        # Registrar movimiento de inventario
        MovimientoInventario.objects.create(
            fk_id_producto=producto_selec,
            tipo_movimiento='S',  # Salida
            cantidad=cantidad
        )

        messages.success(request, 'Venta creada correctamente.')
        return redirect('ventas')
    
def eliminar_venta(request, id):
    venta = Venta.objects.get(id=id)
    venta.delete()
    messages.success(request, 'Venta eliminada correctamente')
    return redirect('ventas')

def editar_venta(request, id):
    venta = Venta.objects.get(id=id)
    productos = Producto.objects.all()

    # Calcular la cantidad (total_venta / precio del producto)
    cantidad = int(venta.total_venta / venta.fk_id_producto.precio_prod)

    context = {
        'venta':venta,
        'productos':productos,
        'cantidad':cantidad
    }
    return render(request, 'venta/editar_venta.html', context)

def procesar_editar_venta(request):
    if request.method == 'POST':
        id = request.POST['id']
        fecha = request.POST['fecha_venta']
        cantidad = int(request.POST['cantidad'])  # Obtener la cantidad del formulario
        fk_id_producto = request.POST['fk_id_producto']
        producto_selec = Producto.objects.get(id=fk_id_producto)
        venta_editar = Venta.objects.get(id=id)

        # Obtener la cantidad previa para calcular el ajuste en stock
        cantidad_previa = int(venta_editar.total_venta / producto_selec.precio_prod)

        # Verificar si hay suficiente stock para ajustar
        diferencia_stock = cantidad - cantidad_previa
        if producto_selec.stock_prod < diferencia_stock:
            messages.error(request, f"No hay suficiente stock para {producto_selec.nombre_prod}. Disponible: {producto_selec.stock_prod}.")
            return redirect('ventas')

        # Recalcular el total (precio del producto * cantidad)
        total = producto_selec.precio_prod * cantidad

        venta_editar.fecha_venta = fecha
        venta_editar.total_venta = total
        venta_editar.fk_id_producto = producto_selec
        venta_editar.save()

        # Ajustar el stock del producto
        producto_selec.stock_prod -= diferencia_stock
        producto_selec.save()

        messages.success(request, 'Venta editada correctamente')
        return redirect('ventas')