import random
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

def consulta(id):
    return Post.objects.get(id = id)

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

        

        contexto = {
            'principal':principal,
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4)

        }
        return render(request, 'index.html',contexto)

