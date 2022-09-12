
from django.urls import path
from .views import Inicio,ListadoVideojuegos, ListadoGeneral

urlpatterns = [
    path('', Inicio.as_view(), name = 'index'),
    path('videojuego/', ListadoVideojuegos.as_view(), name = 'videojuegos'),
    path('generales/',ListadoGeneral.as_view(), name = 'generales'),
]