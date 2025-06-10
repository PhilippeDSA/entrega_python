from django import forms
from .models import Autor, Categoria, Articulo
from .models import Mensaje


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'


class BuscarArticuloForm(forms.ModelForm):
    titulo = forms.CharField(
        max_length=200, required=False, label="Buscar por titulo")


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['receptor', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4})
        }
