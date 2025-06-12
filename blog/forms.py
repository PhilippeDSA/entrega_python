from django import forms
from .models import Autor, Categoria, Articulo, Profile, User
from .models import Mensaje
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'fecha_nacimiento']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4})
        }


class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
