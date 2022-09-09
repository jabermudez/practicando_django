from dataclasses import fields
from django import forms 
from .models import Autor

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