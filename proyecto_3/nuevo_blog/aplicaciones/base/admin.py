from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Autor

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Post

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Contacto

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Web

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = RedesSociales

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'estado','fecha_creacion')
    search_fields = ['nombre']
    resource_class = CategoriaResource



# Register your models here.

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor)
admin.site.register(Post)
admin.site.register(Web)
admin.site.register(RedesSociales)
admin.site.register(Contacto)
admin.site.register(Suscriptor)
