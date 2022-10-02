from cProfile import label
from dataclasses import fields
from tkinter import Widget
from django import forms 
from .models import Autor,Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model =Autor
        fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']
        labels = {
            'nombre': 'Nombre del Autor',
            'apellidos': 'Apellidos del Autor',
            'nacionalidad': 'Nacionalidad del autor',
            'descripcion': 'Pequeña descripción'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el nombre del autor',
                    'id':'nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese los apellidos del autor',
                    'id':'apellidos'
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese una nacionalidad para el autor',
                    'id':'nacionalidad'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese una descripción para el autor',
                    'id':'descripcion'
                }
            )   

        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'autor_id','fecha_publicacion')
        label = {
            'titulo': 'Título del Libro',
            'autor_id': 'Autor(es) del libro',
            'fecha_publicacion': 'Fecha de Publicación del Libro' 
        }
        widgets = {
            'titulo': forms.TextInput(
               attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese título del libro'
                }
            ),
            'autor_id': forms.SelectMultiple(
                attrs= {
                    'class':'form-control'
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget()
        }