from django.contrib import admin

# Register your models here.

from .models import File, IpsFiles, Traza, MinSizeDocumento



admin.site.site_header = 'Extract Pdf'
admin.site.index_title = 'Administración'
admin.site.site_title = 'HTML title from adminsitration'

class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion','documento','dateTimeUp','proceso', 'usuario']
    list_filter = ('dateTimeUp', 'proceso')
    search_fields = ['descripcion', 'id','usuario']


class IpsFilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'file_id', 'fecha_conexion', 'ip', 'usuario', 'lat', 'lon', 'is_routeable' ]
    list_filter =['fecha_conexion']
    search_fields = ['ip', 'id', 'usuario']



class TrazaAdmin(admin.ModelAdmin):
    list_display = ['id', 'funcion_llamada', 'datos_in', 'datos_out', 'usuario', 'fecha_creacion', 'error' ]
    list_filter =['funcion_llamada', 'fecha_creacion']
    list_editable = ['error']
    search_fields = ['usuario', 'fecha_creacion']




class SeguridadAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tam_min', 'activo']
    list_filter =['tam_min', 'activo']
    list_editable = ['activo']
    search_fields = ['titulo', 'tam_min']


admin.site.register(MinSizeDocumento , SeguridadAdmin)


admin.site.register(File, FileAdmin)

admin.site.register(IpsFiles, IpsFilesAdmin)

admin.site.register(Traza, TrazaAdmin)

admin.site.site_url = 'http://localhost:4200'

