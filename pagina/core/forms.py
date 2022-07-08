from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion','precio', 'imagen', 'categoria']

class DescuentosForm(ModelForm):
    class Meta:
        model = Descuentos
        fields = ['producto', 'descripcion','descuento', 'promocion']
