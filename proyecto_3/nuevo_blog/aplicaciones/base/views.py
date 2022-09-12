import random
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Post, Categoria, RedesSociales, Web

def consulta(id):
    try:
        return Post.objects.get(id = id)
    except:
        return None

def obtenerRedes():
    return RedesSociales.objects.filter(estado = True).latest('fecha_creacion')

def obtenerWeb():
    return Web.objects.filter(estado = True).latest('fecha_creacion')

class Inicio(ListView):

    def get(self,request,*args,**kwargs):
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat=True))
        print(posts)
        principal = random.choice(posts)
        posts.remove(principal)
        principal = consulta(principal)

        post1 = random.choice(posts)
        posts.remove(post1)

        post2 = random.choice(posts)
        posts.remove(post2)

        post3 = random.choice(posts)
        posts.remove(post3)

        post4 = random.choice(posts)
        posts.remove(post4)

        try:
            post_videojuegos = Post.objects.filter(
                                estado = True,
                                publicado = True,
                                categoria = Categoria.objects.get(nombre = 'Videojuegos')
                                ).latest('fecha_publicacion')
        except:
            post_videojuegos = None
        
        try:
            post_general = Post.objects.filter(
                estado = True,
                publicado = True,
                categoria = Categoria.objects.get(nombre = 'General')
                ).latest('fecha_publicacion')
        except:
            post_general = None
        

        contexto = {
            'principal':principal,
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4),
            'post_general':post_general,
            'post_videojuegos':post_videojuegos,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),

        }
        return render(request, 'index.html',contexto)

class ListadoVideojuegos(ListView):

    def get(self,request,*args,**kwargs):
        posts_videojuegos = Post.objects.filter(
                            estado = True,
                            publicado = True,
                            categoria = Categoria.objects.get(nombre = 'Videojuegos')
                            )
        try:
            categoria = Categoria.objects.get(nombre = 'Videojuegos')
        except:
            categoria = None

        paginator = Paginator(posts_videojuegos,3)
        pagina = request.GET.get('page')
        posts = paginator.get_page(pagina)

        contexto = {
            'posts': posts,
            'sociales': obtenerRedes(),
            'web':obtenerRedes(),
            'categoria':categoria,
        }
        return render(request, 'categoria.html',contexto)

class ListadoGeneral(ListView):
    def get(self,request, *args, **kwargs):
        posts_generales = Post.objects.filter(
                            estado = True,
                            publicado = True,
                            categoria = Categoria.objects.get(nombre = 'General')
                            )
        try:
            categoria = Categoria.objects.get(nombre = 'General')
        except:
            categoria = None
        
        paginator = Paginator(posts_generales, 3)
        pagina = request.GET.get('page')
        posts =paginator.get_page(pagina)

        contexto = {
            'posts':posts,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'categoria':categoria,
        }
        return render(request, 'categoria.html',contexto)