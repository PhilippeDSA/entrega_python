from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(max_length=200)
    contenido = RichTextUploadingField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, related_name='articulos')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, related_name='articulos')
    imagen = models.ImageField(upload_to="articulos/", null=True, blank=True)

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.nombre


class Mensaje(models.Model):
    remitente = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.remitente} para {self.receptor}-{self.fecha.strftime('%Y-%m-%d %H:%M')}"


class Page(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextUploadingField()
    slug = models.SlugField(unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars/', default='avatars/default.png')
    bio = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
