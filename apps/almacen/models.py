from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre_cat = models.CharField(max_length=100, unique=True)
    descripcion_cat = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_cat
    
class Proveedor(models.Model):
    nombre_prov = models.CharField(max_length=100)
    direccion_prov = models.TextField(blank=True, null=True)
    telefono_prov = models.CharField(max_length=15, blank=True, null=True)
    email_prov = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre_prov

class Producto(models.Model):
    nombre_prod = models.CharField(max_length=100)
    descripcion_prod = models.TextField(blank=True, null=True)
    precio_prod = models.DecimalField(max_digits=10, decimal_places=2)
    stock_prod = models.PositiveIntegerField(default=0)
    codigo_barras_prod = models.CharField(max_length=100, unique=True, blank=True, null=True)
    fk_id_categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fk_id_proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)  # Nueva relación

    def __str__(self):
        return self.nombre_prod

class Venta(models.Model):
    fecha_venta = models.DateField(default=timezone.now)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fk_id_producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"venta {self.id} - {self.fecha_venta}"

class Detalle_Venta(models.Model):
    fk_id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name="Detalles")
    fk_id_producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario
    
class Compra(models.Model):
    fk_id_proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    fecha_compra = models.DateField(default=timezone.now)
    total_compra = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"compra {self.id} - {self.fecha_compra}"

class Detalle_Compra(models.Model):
    fk_id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="Detalles")
    fk_id_producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

class MovimientoInventario(models.Model):
    fk_id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=50, choices=(('E', 'Entrada'), ('S', 'Salida')))
    cantidad = models.PositiveIntegerField()
    fecha_movimiento = models.DateField(auto_now_add=True)
    descripcion_movimiento = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_movimiento} - {self.fecha_movimiento}"
