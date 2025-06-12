from django.shortcuts import render, redirect, get_object_or_404
from .forms import AutorForm, CategoriaForm, ArticuloForm, MensajeForm, ProfileForm
from .models import Articulo, Mensaje, Page, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Page, Profile


@login_required
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'blog/crear_articulo.html', {'form': form})


@login_required
def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'blog/lista_articulos.html', {'articulos': articulos})


@login_required
def buscar_articulo(request):
    query = request.GET.get('q')
    resultados = Articulo.objects.filter(
        nombre__icontains=query) if query else []
    return render(request, 'blog/buscar_articulo.html', {'resultados': resultados, 'query': query})


@login_required
def home(request):
    perfil, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'blog/home.html', {'perfil': perfil})


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


@login_required
def bandeja_entrada(request):
    mensajes_recibidos = Mensaje.objects.filter(
        receptor=request.user).order_by('-fecha')
    return render(request, 'blog/bandeja_entrada.html', {'mensajes': mensajes_recibidos})


@login_required
def about(request):
    return render(request, 'blog/about.html')


@login_required
def pages_list(request):
    pages = Page.objects.all()
    return render(request, 'blog/pages_list.html', {'pages': pages})


@login_required
def pages_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'blog/pages_detail.html', {'page': page})


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['titulo', 'contenido', 'slug']
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('pages_list')


class PageUpdatedView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['titulo', 'contenido', 'slug']
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('pages_list')


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'blog/page_confirm_delete.html'
    success_url = reverse_lazy('pages_list')


@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'blog/edit_profile.html', {'form': form})


class MiPerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/mi_perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perfil, created = Profile.objects.get_or_create(user=self.request.user)
        context['perfil'] = perfil
        return context


class EditarPerfilView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'blog/profile_form.html'
    success_url = reverse_lazy('mi_perfil')

    def test_func(self):
        return self.get_object().user == self.request.user


class CrearPerfilView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'blog/profile_form.html'
    success_url = reverse_lazy('mi_perfil')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.__class__.__name__
        return context


class EliminarPerfilView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'blog/profile_confirm_delete.html'
    success_url = reverse_lazy('mi_perfil')

    def test_func(self):
        return self.get_object().user == self.request.user


@login_required
def articulo_detail(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'blog/articulo_detail.html', {'articulo': articulo})
