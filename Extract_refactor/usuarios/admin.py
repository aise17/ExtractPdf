from django.contrib import admin
from.models import Incidencia

# Register your models here.

class IncidenciasAdmin(admin.ModelAdmin):
    list_display = ['asunto', 'contenido', 'usuario', 'fecha_creacion', 'resuelta']
    list_filter =['usuario', 'fecha_creacion']
    search_fields = ['asunto']
    list_editable = ['resuelta']

admin.site.register(Incidencia, IncidenciasAdmin)
