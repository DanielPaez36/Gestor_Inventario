from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Categoria

def inicio(request):
    return render(request, 'index.html', {})

def categorias(request):
    categorias = Categoria.objects.all()
    context ={
        'categorias': categorias
    }
    return render(request, 'categoria/categorias.html', context)

def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_cat']
        descripcion = request.POST['descripcion_cat']

        Categoria.objects.create(
            nombre_cat=nombre,
            descripcion_cat=descripcion
        )
        messages.success(request, 'Categoria creada correctamente')
        return redirect('categorias')

def  eliminar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    messages.success(request, 'Categoria eliminada correctamente')
    return redirect('categorias')

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    context = {
        'categoria': categoria
    }
    return render(request, 'categoria/editar_categoria.html', context)

def procesar_editar_categoria(request):
    if request.method == 'POST':
        id = request.POST['id']
        nombre = request.POST['nombre_cat']
        descripcion = request.POST['descripcion_cat']

        categoria_editar = Categoria.objects.get(id=id)
        categoria_editar.nombre_cat = nombre
        categoria_editar.descripcion_cat = descripcion
        categoria_editar.save()
        messages.success(request, 'Categoria editada correctamente')
        return redirect('categorias')