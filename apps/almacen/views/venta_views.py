from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Venta, Producto, Detalle_Venta

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
        cantidad = int(request.POST['cantidad'])  # Obtener la cantidad del formulario
        fk_id_producto = request.POST['productos']
        producto_selec = Producto.objects.get(id=fk_id_producto)

        # Calcular el total (precio del producto * cantidad)
        total = producto_selec.precio_prod * cantidad

        # Crear la venta
        Venta.objects.create(
            fecha_venta=fecha,
            total_venta=total,
            fk_id_producto=producto_selec
        )

        messages.success(request, 'Venta creada correctamente')
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
        # Obtener los datos enviados desde el formulario
        id = request.POST['id']
        fecha = request.POST['fecha_venta']
        cantidad = int(request.POST['cantidad'])  # Obtener la cantidad del formulario
        fk_id_producto = request.POST['fk_id_producto']

        # Obtener el producto y la venta que se va a editar
        producto_selec = Producto.objects.get(id=fk_id_producto)
        venta_editar = Venta.objects.get(id=id)

        # Recalcular el total (precio del producto * cantidad)
        total = producto_selec.precio_prod * cantidad

        # Actualizar los valores de la venta
        venta_editar.fecha_venta = fecha
        venta_editar.total_venta = total
        venta_editar.fk_id_producto = producto_selec
        venta_editar.save()

        # Mensaje de éxito
        messages.success(request, 'Venta editada correctamente')
        return redirect('ventas')