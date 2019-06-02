from django.contrib import admin
from .models import Incidencia, BonoUsuario, MarketingCampaign


class IncidenciasAdmin(admin.ModelAdmin):
    list_display = ['asunto', 'contenido', 'usuario', 'fecha_creacion', 'resuelta']
    list_filter =['usuario', 'fecha_creacion']
    search_fields = ['asunto']
    list_editable = ['resuelta']


class MarketingCampaignAdmin(admin.ModelAdmin):
    list_display = ['id', 'asunto', 'fecha_creacion', 'fecha_publicacion', 'lanzada']
    list_filter =['asunto', 'fecha_creacion', 'fecha_publicacion', 'lanzada']
    search_fields = ['asunto']


class BonoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'bono', 'activado', 'fecha_creacion' ]
    list_filter =['usuario', 'bono', 'fecha_creacion']
    list_editable = ['activado']
    search_fields = ['usuario', 'bono', 'fecha_creacion', 'peticiones_consumidas']


admin.site.register(MarketingCampaign, MarketingCampaignAdmin)

admin.site.register(BonoUsuario, BonoUsuarioAdmin)

admin.site.register(Incidencia, IncidenciasAdmin)
