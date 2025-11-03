from django.db import models
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre

class detalle_producto(models.Model):
    producto = models.OneToOneField(
        Producto,
        on_delete=models.CASCADE,
        related_name='detalle'       
    )
    dimension = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Detalle de {self.producto.nombre}"