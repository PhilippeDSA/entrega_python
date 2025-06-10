from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_articulo, name='crear_articulo'),
    path('lista/', views.lista_articulos, name='lista_articulos'),
    path('buscar/', views.buscar_articulo, name='buscar_articulo'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("robots.txt", TemplateView.as_view(
        template_name="robots.txt", content_type="text/plain")),
    path("sitemap.xml", TemplateView.as_view(
        template_name="sitemap.xml", content_type="application/xml")),
    path('mensajes/enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('mensajes/bandeja/', views.bandeja_entrada, name='bandeja_entrada'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
