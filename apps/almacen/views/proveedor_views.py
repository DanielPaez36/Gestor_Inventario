from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Proveedor

def proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {
        'proveedores':proveedores
    }
    return render(request, 'proveedor/proveedores.html', context)

def crear_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_prov']
        direccion = request.POST['direccion_prov']
        telefono = request.POST['telefono_prov']
        email = request.POST['email_prov']

        if Proveedor.objects.filter(nombre_prov=nombre).exists():
            messages.error(request, 'Ya existe un proveedor con ese nombre.')
            return redirect('proveedores')

        Proveedor.objects.create(
            nombre_prov = nombre,
            direccion_prov = direccion,
            telefono_prov = telefono,
            email_prov = email
        )
        messages.success(request, 'Proveedor añadido correctamente')
        return redirect('proveedores')

def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    messages.success(request, 'Proveedor eliminado correctamente')
    return redirect('proveedores')

def editar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    context = {
        'proveedor':proveedor
    }
    return render(request, 'proveedor/editar_proveedores.html', context)

def procesar_editar_proveedor(request):
    if request.method == 'POST':
        id = request.POST['id']
        nombre = request.POST['nombre_prov']
        direccion = request.POST['direccion_prov']
        telefono = request.POST['telefono_prov']
        email = request.POST['email_prov']
        
        proveedor_editar = Proveedor.objects.get(id=id)
        proveedor_editar.nombre_prov = nombre
        proveedor_editar.direccion_prov = direccion
        proveedor_editar.telefono_prov = telefono
        proveedor_editar.email_prov = email
        proveedor_editar.save()
        messages.success(request, 'Proveedor editado correctamente')
        return redirect('proveedores')