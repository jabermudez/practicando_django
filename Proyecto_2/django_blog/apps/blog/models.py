from argparse import BooleanOptionalAction
from tabnanny import verbose
from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoría', max_length=100, null=False,blank=False)
    estado = models.BooleanField('Categoría Activada/Categoría no Activada', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.nombre 

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres de Autor', max_length=255, null=False, blank=False)
    apellidos = models.CharField('Apellidos del Autor', max_length=255, null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null = True, blank = True)
    correo = models.EmailField('Correo Eletrónico', blank=False, null = False)
    estado = models.BooleanField('Autor Activo/No Activo', default=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)