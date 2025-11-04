from django.db import models
from categorias.models import Categoria
from etiquetas.models import Etiqueta

# --- MODELO DETALLE DEL PRODUCTO ---
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    # Relación Muchos a Uno con Categoría
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE, 
        related_name='productos'
    )

    # Relación Muchos a Muchos con Etiqueta
    etiquetas = models.ManyToManyField(
        Etiqueta,
        related_name='productos',
        blank=True
    )

    def __str__(self):
        return self.nombre


# --- MODELO DETALLE DEL PRODUCTO ---
class DetalleProducto(models.Model):
    producto = models.OneToOneField(
        Producto,
        on_delete=models.CASCADE,
        related_name='detalle'
    )
    dimension = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de {self.producto.nombre}"