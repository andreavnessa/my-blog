from django.contrib import admin
from .models import *
# Register your models here.


class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor')
admin.site.register(Publicacion, PublicacionAdmin)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass