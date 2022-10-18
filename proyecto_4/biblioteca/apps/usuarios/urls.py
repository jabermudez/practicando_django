from urllib.parse import urlparse

from  django.urls import path
from django.contrib.auth.decorators import login_required
from apps.usuarios.views import ListadoUsuario, RegistrarUsuario, TemplateView



urlpatterns = [
    path('listado_usuarios/', login_required(ListadoUsuario.as_view()),name='listar_usuarios'),
    path('registrar_usuarios/', login_required(RegistrarUsuario.as_view()),name='registrar_usuarios')

]
#URLS DE VISTAS IMPLICITAS
urlpatterns += [
    path('inicio_usuarios/', login_required(
        TemplateView.as_view(
            template_name = 'usuarios/listar_usuario.html'
        )
     ), name = 'inicio_usuarios'),
]