from django.contrib import admin
from .models import Incidencia, BonoUsuario


class IncidenciasAdmin(admin.ModelAdmin):
    list_display = ['asunto', 'contenido', 'usuario', 'fecha_creacion', 'resuelta']
    list_filter =['usuario', 'fecha_creacion']
    search_fields = ['asunto']
    list_editable = ['resuelta']


class BonoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'bono', 'activado', 'fecha_creacion' ]
    list_filter =['usuario', 'bono', 'fecha_creacion']
    list_editable = ['activado']
    search_fields = ['usuario', 'bono', 'fecha_creacion']


admin.site.register(BonoUsuario, BonoUsuarioAdmin)

admin.site.register(Incidencia, IncidenciasAdmin)
