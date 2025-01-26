from django.urls import path
from apps.almacen.views import categoria_views, producto_views, proveedor_views, venta_views, detalles_views, compra_views, movimientoInventario_views

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

    #Proveedores
    path('proveedores/', proveedor_views.proveedores, name='proveedores'),
    path('crear_proveedor/', proveedor_views.crear_proveedor, name='crear_proveedor'),
    path('eliminar_proveedor/<int:id>/', proveedor_views.eliminar_proveedor, name='eliminar_proveedor'),
    path('editar_proveedor/<int:id>/', proveedor_views.editar_proveedor, name='editar_proveedor'),
    path('procesar_editar_proveedor/', proveedor_views.procesar_editar_proveedor, name='procesar_editar_proveedor'),

    #Ventas
    path('ventas/', venta_views.ventas, name='ventas'),
    path('crear_venta/', venta_views.crear_venta, name='crear_venta'),
    path('eliminar_venta/<int:id>/', venta_views.eliminar_venta, name='eliminar_venta'),
    path('editar_venta/<int:id>/', venta_views.editar_venta, name='editar_venta'),
    path('procesar_editar_venta/', venta_views.procesar_editar_venta, name='procesar_editar_venta'),

    #Detalles
    path('detalles/<int:id>/', detalles_views.detalles, name='detalles'),

    #Compras
    path('compras/', compra_views.compras, name='compras'),
    path('crear_compra/', compra_views.crear_compra, name='crear_compra'),
    path('eliminar_compra/<int:id>/', compra_views.eliminar_compra, name='eliminar_compra'),
    path('detalles_compra/<int:id>/', compra_views.detalles_compra, name='detalles_compra'),

    #Movimientos
    path('movimientos/', movimientoInventario_views.listar_movimientos, name='movimientos'),
    path('crear_movimiento/', movimientoInventario_views.crear_movimiento, name='crear_movimiento'),
    path('editar_movimiento/<int:id>/', movimientoInventario_views.editar_movimiento, name='editar_movimiento'),
    path('procesar_editar_movimiento/', movimientoInventario_views.procesar_editar_movimiento, name='procesar_editar_movimiento'),
    path('eliminar_movimiento/<int:id>/', movimientoInventario_views.eliminar_movimiento, name='eliminar_movimiento'),
]