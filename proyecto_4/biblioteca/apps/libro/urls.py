from django.urls import path
from .views import ListarAutor, eliminarAutor, ActualizarAutor, CrearAutor

urlpatterns = [
   path('crear_autor/', CrearAutor.as_view(), name='crear_autor'),
   path('listar_autor/', ListarAutor.as_view(), name='listar_autor'),
   path('editar_autor/<int:pk>', ActualizarAutor.as_view(), name = 'editar_autor'),
   path('eliminar_autor/<int:id>', eliminarAutor, name = 'eliminar_autor')
]