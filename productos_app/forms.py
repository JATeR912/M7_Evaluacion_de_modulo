from django import forms
from .models import Producto, DetalleProducto

class ProductoForm(forms.ModelForm):
    dimension = forms.CharField(max_length=100, required=False)
    peso = forms.DecimalField(max_digits=10, decimal_places=2, required=False)

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas', 'dimension', 'peso']
