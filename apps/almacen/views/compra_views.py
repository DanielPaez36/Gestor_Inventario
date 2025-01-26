from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Compra, Detalle_Compra, Proveedor, Producto, MovimientoInventario

def compras(request):
    compras = Compra.objects.all()
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()  # Todos los productos
    context = {
        'compras': compras,
        'proveedores': proveedores,
        'productos': productos,
    }
    return render(request, 'compra/compras.html', context)

def crear_compra(request):
    if request.method == 'POST':
        fk_id_proveedor = request.POST['fk_id_proveedor']
        fecha_compra = request.POST['fecha_compra']
        productos_ids = request.POST.getlist('productos[]')
        cantidades = request.POST.getlist('cantidades[]')
        precios_unitarios = request.POST.getlist('precios_unitarios[]')

        proveedor = Proveedor.objects.get(id=fk_id_proveedor)
        total_compra = sum(float(cantidades[i]) * float(precios_unitarios[i]) for i in range(len(productos_ids)))

        compra = Compra.objects.create(
            fk_id_proveedor=proveedor,
            fecha_compra=fecha_compra,
            total_compra=total_compra
        )

        for i in range(len(productos_ids)):
            producto = Producto.objects.get(id=productos_ids[i])
            cantidad = int(cantidades[i])
            
            # Crear detalle de la compra
            Detalle_Compra.objects.create(
                fk_id_compra=compra,
                fk_id_producto=producto,
                cantidad=cantidad,
                precio_unitario=precios_unitarios[i]
            )

            # Actualizar stock del producto
            producto.stock_prod += cantidad
            producto.save()

            # Registrar movimiento de inventario
            MovimientoInventario.objects.create(
                fk_id_producto=producto,
                tipo_movimiento='E',  # Entrada
                cantidad=cantidad
            )

        messages.success(request, 'Compra creada correctamente.')
        return redirect('compras')

    
def eliminar_compra(request, id):
    compra = Compra.objects.get(id=id)
    compra.delete()
    messages.success(request, 'Compra eliminada correctamente.')
    return redirect('compras')

def detalles_compra(request, id):
    compra = Compra.objects.get(id=id)
    detalles = Detalle_Compra.objects.filter(fk_id_compra=compra)
    context = {
        'compra': compra,
        'detalles': detalles,
    }
    return render(request, 'compra/detalles_compra.html', context)