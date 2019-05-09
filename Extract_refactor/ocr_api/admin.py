from django.contrib import admin

# Register your models here.
from .models import File, Explicacion, IpsFiles, Incidencia, \
    QuienSomos, Bono, BonoUsuario, Traza


class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion','documento','dateTimeUp','proceso', 'usuario']
    list_filter = ('dateTimeUp', 'proceso')
    search_fields = ['descripcion', 'id']

class ExplicacionAdmin(admin.ModelAdmin):
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


class BonoAdmin(admin.ModelAdmin):
    list_display = ['id', 'peticiones', 'descripcion', 'precio', 'activado', 'fecha_creacion' ]
    list_filter =['activado', 'fecha_creacion']
    list_editable = ['activado']
    search_fields = ['id']

class BonoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'bono', 'activado', 'fecha_creacion' ]
    list_filter =['usuario', 'bono', 'fecha_creacion']
    list_editable = ['activado']
    search_fields = ['usuario', 'bono', 'fecha_creacion']

class TrazaAdmin(admin.ModelAdmin):
    list_display = ['id', 'funcion_llamada', 'datos_in', 'datos_out', 'usuario', 'fecha_creacion', 'error' ]
    list_filter =['funcion_llamada', 'fecha_creacion']
    list_editable = ['error']
    search_fields = ['usuario', 'fecha_creacion']


admin.site.site_header = 'Extract Pdf'
admin.site.index_title = 'Administración'
admin.site.site_title = 'HTML title from adminsitration'

admin.site.register(File, FileAdmin)
admin.site.register(Explicacion, ExplicacionAdmin)

admin.site.register(IpsFiles, IpsFilesAdmin)
admin.site.register(Incidencia, IncidenciasAdmin)
admin.site.register(QuienSomos, QuienSomosAdmin)

admin.site.register(Bono, BonoAdmin)
admin.site.register(BonoUsuario, BonoUsuarioAdmin)
admin.site.register(Traza, TrazaAdmin)

admin.site.site_url = 'http://localhost:4200'

