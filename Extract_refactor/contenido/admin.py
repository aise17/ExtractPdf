from django.contrib import admin

from .models import AnuncioInferior, AnuncioLateral, AnuncioSuperior, Explicacion, QuienSomos, Bono, Faqs


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

class ExplicacionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_creacion', 'fecha_publicacion', 'publicado' ]
    list_filter =['publicado', 'fecha_creacion', 'fecha_publicacion']
    list_editable = ['publicado']
    search_fields = ['titulo']


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

class FaqsAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_creacion', 'fecha_publicacion', 'publicado' ]
    list_filter =['publicado', 'fecha_creacion', 'fecha_publicacion']
    list_editable = ['publicado']
    search_fields = ['titulo']





admin.site.register(AnuncioLateral, AnuncioLateralAdmin)
admin.site.register(AnuncioSuperior, AnuncioSuperiorAdmin)
admin.site.register(AnuncioInferior, AnuncioInferiorAdmin)

admin.site.register(Explicacion, ExplicacionAdmin)
admin.site.register(Faqs, FaqsAdmin)
admin.site.register(QuienSomos, QuienSomosAdmin)
admin.site.register(Bono, BonoAdmin)



