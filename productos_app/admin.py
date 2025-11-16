from django.contrib import admin
from .models import Producto, DetalleProducto, Categoria, Etiqueta

admin.site.register(Producto)
admin.site.register(DetalleProducto)
admin.site.register(Categoria)
admin.site.register(Etiqueta)