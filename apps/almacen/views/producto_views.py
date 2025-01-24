from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Producto, Categoria

def productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    context = {
        'productos':productos,
        'categorias':categorias,
    }
    return render(request, 'producto/productos.html', context)

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_prod']
        descripcion = request.POST['descripcion_prod']
        precio = request.POST['precio_prod']
        stock = request.POST['stock_prod']
        codigo_barras = request.POST['codigo_barras_prod']
        fk_id_categoria = request.POST['fk_id_categoria']
        categoria_selec = Categoria.objects.get(id=fk_id_categoria)

        if Producto.objects.filter(codigo_barras_prod=codigo_barras).exists() or Producto.objects.filter(nombre_prod=nombre).exists():
            messages.error(request, 'El nombre o el codigo de barras le pertenece a otro producto.')
            return redirect('productos')

        Producto.objects.create(
            nombre_prod=nombre,
            descripcion_prod=descripcion,
            precio_prod=precio,
            stock_prod=stock,
            codigo_barras_prod=codigo_barras,
            fk_id_categoria=categoria_selec
        )
        messages.success(request, 'Producto creado correctamente')
        return redirect('productos')

def eliminar_producto(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.success(request, 'Producto eliminado correctamente')
    return redirect('productos')

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    categorias = Categoria.objects.all()
    context = {
        'producto':producto,
        'categorias':categorias
    }
    return render(request, 'producto/editar_producto.html', context)

def procesar_editar_producto(request):
    if request.method == 'POST':
        id = request.POST['id']
        nombre = request.POST['nombre_prod']
        descripcion = request.POST['descripcion_prod']
        precio = request.POST['precio_prod']
        stock = request.POST['stock_prod']
        codigo_barras = request.POST['codigo_barras_prod']
        fk_id_categoria = request.POST['fk_id_categoria']

        categoria_selec = Categoria.objects.get(id=fk_id_categoria)
        producto_editar = Producto.objects.get(id=id)
        producto_editar.nombre_prod = nombre
        producto_editar.descripcion_prod = descripcion
        producto_editar.precio_prod = precio
        producto_editar.stock_prod = stock
        producto_editar.codigo_barras_prod = codigo_barras
        producto_editar.fk_id_categoria = categoria_selec
        producto_editar.save()
        messages.success(request, 'Producto editado correctamente')
        return redirect('productos')
