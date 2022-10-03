from urllib import request
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm, LibroForm
from .models import Autor, Libro
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, View
from django.urls import reverse_lazy


'''
   1. dispatch(): valida la petición y elige que método HTTP se utilizo para la solicitud
   2. http_method_not_allowed(): retorna un error cuando se utiliza un método HTTP no soportado o definido 
   3. options()

class Inicio(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')
'''

class Inicio(TemplateView): 
    template_name = 'index.html'

class ListarAutor(ListView):
    model = Autor
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado=True)

class ActualizarAutor(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'    
    success_url = reverse_lazy('libro:listar_autor')

class CrearAutor(CreateView):
    model = Autor 
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

'''  eliminación Lógica

class EliminarAutor(DeleteView):
    model = Autor 
    success_url = reverse_lazy('libro:listar_autor')
'''

class EliminarAutor(DeleteView):
    model = Autor 
    
    def post(self, request,pk,*args, **kwargs):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')



#Eliminación completa de la base de datos de un registro
"""
/creación formulario inputs html
def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html',{'autor_form':autor_form})

/Eliminación con validación
def eliminarAutor(request,id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        autor.delete()
        return redirect('libro:listar_autor')
    return render(request, 'libro/eliminar_autor.html', {'autor':autor})

/Eliminación sin validación
def eliminarAutor(request,id):
    autor = Autor.objects.get(id = id)
    autor.delete()
    return redirect('libro:listar_autor')
    


"""
#Eliminación lógica o desactivación de la base de datos de un registro

def eliminarAutor(request,id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')
    return render(request, 'libro/autor/eliminar_autor.html', {'autor':autor})



class ListadoLibros(View):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/listar_libro.html' # queryset = Libro.objects.all() object_list

    def get_queryset(self):
        return self.model.objects.filter(estado=True)
    
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['libros'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto 
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro:listado_libros')
'''
class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:listado_libros')
'''
class ActualizarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/libro.html'
    success_url = reverse_lazy('libro:listado_libros')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['libros'] = Libro.objects.filter(estado = True)
        return context

class EliminarLibro(DeleteView):
    model = Libro

    def post(self, request, pk, *args, **kwargs):
        object = Libro.objects.get(id = pk)
        object.estado = False 
        object.save()
        return redirect('libro:listado_libros')