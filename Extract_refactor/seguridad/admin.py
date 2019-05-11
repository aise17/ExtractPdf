from django.contrib import admin

# Register your models here.
from .models import MinSizeDocumento


class SeguridadAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tam_min', 'activo']
    list_filter =['tam_min', 'activo']
    list_editable = ['activo']
    search_fields = ['titulo', 'tam_min']


admin.site.register(MinSizeDocumento , SeguridadAdmin)
