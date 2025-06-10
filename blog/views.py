from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, ArticuloForm, MensajeForm
from .models import Articulo, Mensaje
from django.contrib.auth.decorators import login_required


def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'blog/crear_articulo.html', {'form': form})


def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'blog/lista_articulos.html', {'articulos': articulos})


def buscar_articulo(request):
    query = request.GET.get('q')
    resultados = Articulo.objects.filter(
        nombre__icontains=query) if query else []
    return render(request, 'blog/buscar_articulo.html', {'resultados': resultados, 'query': query})


def home(request):
    return render(request, 'blog/home.html')


@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('bandeja_entrada')
    else:
        form = MensajeForm()
        return render(request, 'blog/enviar_mensaje.html', {'form': form})


def bandeja_entrada(request):
    mensajes_recibidos = Mensaje.objects.filter(
        receptor=request.user).order_by('-fecha')
    return render(request, 'blog/bandeja_entrada.html', {'mensajes ': mensajes_recibidos})
