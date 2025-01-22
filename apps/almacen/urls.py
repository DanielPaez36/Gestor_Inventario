from django.urls import path
from apps.almacen.views import categoria_views, producto_views

urlpatterns = [

    #Inicio
    path('', categoria_views.inicio, name='inicio'),

    #Categorias
    path('categorias/', categoria_views.categorias, name='categorias'),
    path('crear_categoria/', categoria_views.crear_categoria, name='crear_categoria'),
    path('eliminar_categoria/<int:id>/', categoria_views.eliminar_categoria, name='eliminar_categoria'),
    path('editar_categoria/<int:id>/', categoria_views.editar_categoria, name='editar_categoria'),
    path('procesar_editar_categoria/', categoria_views.procesar_editar_categoria, name='procesar_editar_categoria'),

    #Productos
    path('productos/', producto_views.productos, name='productos'),
    path('crear_producto/', producto_views.crear_producto, name='crear_producto'),
    path('eliminar_producto/<int:id>/', producto_views.eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:id>/', producto_views.editar_producto, name='editar_producto'),
    path('procesar_editar_producto/', producto_views.procesar_editar_producto, name='procesar_editar_producto'),
]