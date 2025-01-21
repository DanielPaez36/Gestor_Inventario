from django.urls import path
from apps.almacen.views import categoria_views

urlpatterns = [

    #Inicio
    path('', categoria_views.inicio, name='inicio'),

    #Categorias
    path('categorias/', categoria_views.categorias, name='categorias'),
    path('crear_categoria/', categoria_views.crear_categoria, name='crear_categoria'),
    path('eliminar_categoria/<int:id>/', categoria_views.eliminar_categoria, name='eliminar_categoria'),
    path('editar_categoria/<int:id>/', categoria_views.editar_categoria, name='editar_categoria'),
    path('procesar_editar_categoria/', categoria_views.procesar_editar_categoria, name='procesar_editar_categoria'),
]