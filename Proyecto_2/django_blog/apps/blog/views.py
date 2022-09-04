from django.shortcuts import render
from .models import *

def home(request):
    posts = Post.objects.filter(estado = True)  
    return render(request,'index.html',{'posts':posts})

def generales(request):
    posts = Post.objects.filter(
        estado = True, 
        categoria = Categoria.objects.get(nombre = 'General')
        )
    return render(request,'generales.html',{'posts':posts})

def programacion(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre = 'Programación')
    )
    return render(request,'programacion.html',{'posts':posts})

def tutoriales(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre = 'Tutoriales')
    )
    return render(request,'tutoriales.html',{'posts':posts})

def tecnologia(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre = 'Tecnología')
    )
    return render(request,'tecnologia.html',{'posts':posts})

def videojuegos(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre = 'Videojuegos')
    )
    return render(request,'videojuegos.html',{'posts':posts})