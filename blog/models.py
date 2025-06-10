from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(max_length=200)
    contenido = RichTextUploadingField()
    fechas_publicacion = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, related_name='articulos')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, related_name='articulos')

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
