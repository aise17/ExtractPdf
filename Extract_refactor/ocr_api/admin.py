from django.contrib import admin

# Register your models here.
from .models import File, Explicacion, AnuncioInferior, AnuncioLateral, AnuncioSuperior, IpsFiles, Incidencia, \
    QuienSomos


class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion','documento','dateTimeUp','proceso', 'usuario']
    list_filter = ('dateTimeUp', 'proceso')
    search_fields = ['descripcion', 'id']

class ExplicacionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_creacion', 'fecha_publicacion', 'publicado' ]
    list_filter =['publicado', 'fecha_creacion', 'fecha_publicacion']
    list_editable = ['publicado']
    search_fields = ['titulo']


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

class IpsFilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'file_id', 'fecha_conexion', 'ip', 'usuario', 'lat', 'lon', 'is_routeable' ]
    list_filter =['fecha_conexion']
    search_fields = ['ip', 'id']


class IncidenciasAdmin(admin.ModelAdmin):
    list_display = ['asunto', 'contenido', 'usuario', 'fecha_creacion', 'resuelta']
    list_filter =['usuario', 'fecha_creacion']
    search_fields = ['asunto']
    list_editable = ['resuelta']


class QuienSomosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_creacion', 'fecha_publicacion', 'publicado' ]
    list_filter =['publicado', 'fecha_creacion', 'fecha_publicacion']
    list_editable = ['publicado']
    search_fields = ['titulo']


admin.site.site_header = 'Extract Pdf'
admin.site.index_title = 'Administración'
admin.site.site_title = 'HTML title from adminsitration'

admin.site.register(File, FileAdmin)
admin.site.register(Explicacion, ExplicacionAdmin)
admin.site.register(AnuncioLateral, AnuncioLateralAdmin)
admin.site.register(AnuncioSuperior, AnuncioSuperiorAdmin)
admin.site.register(AnuncioInferior, AnuncioInferiorAdmin)
admin.site.register(IpsFiles, IpsFilesAdmin)
admin.site.register(Incidencia, IncidenciasAdmin)
admin.site.register(QuienSomos, QuienSomosAdmin)

