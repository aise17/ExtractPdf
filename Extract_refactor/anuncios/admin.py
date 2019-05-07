from django.contrib import admin

from .models import AnuncioInferior, AnuncioLateral, AnuncioSuperior

# Register your models here.

class AnuncioSuperiorAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_creacion', 'fecha_publicacion', 'publicado' ]
    list_filter =['publicado', 'fecha_creacion', 'fecha_publicacion']
    list_editable = ['publicado']
    search_fields = ['titulo']

class AnuncioLateralAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_creacion', 'fecha_publicacion', 'publicado' ]
    list_filter =['publicado', 'fecha_creacion', 'fecha_publicacion']
    list_editable = ['publicado']
    search_fields = ['titulo']

class AnuncioInferiorAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_creacion', 'fecha_publicacion', 'publicado' ]
    list_filter =['publicado', 'fecha_creacion', 'fecha_publicacion']
    list_editable = ['publicado']
    search_fields = ['titulo']


admin.site.register(AnuncioLateral, AnuncioLateralAdmin)
admin.site.register(AnuncioSuperior, AnuncioSuperiorAdmin)
admin.site.register(AnuncioInferior, AnuncioInferiorAdmin)