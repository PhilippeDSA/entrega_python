from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, reverse_lazy
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', views.home, name='home'),
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
    path('about/', views.about, name='about'),
    path('pages/', views.pages_list, name='pages_list'),
    path('pages/create/', views.PageCreateView.as_view(), name='pages_create'),
    path('pages/<slug:slug>/', views.pages_detail, name='pages_detail'),
    path('pages/edit/<slug:slug>/',
         views.PageUpdatedView.as_view(), name='pages_update'),
    path('pages/delete/<slug:slug>/',
         views.PageDeleteView.as_view(), name='pages_delete'),
    path('perfil/', views.MiPerfilView.as_view(), name='mi_perfil'),
    path('perfil/editar/<int:pk>/',
         views.EditarPerfilView.as_view(), name='editar_perfil'),
    path('perfil/crear/', views.CrearPerfilView.as_view(), name='crear_perfil'),
    path('perfil/eliminar/<int:pk>/',
         views.EliminarPerfilView.as_view(), name='eliminar_perfil'),
    path('passwor_change/', auth_views.PasswordChangeView.as_view(
        template_name='blog/password_change_form.html', success_url=reverse_lazy('password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='blog/password_change_done.html'), name='password_change_done'),
    path('articulo/<int:pk>/', views.articulo_detail, name='articulo_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
