from django.contrib import admin
from .models import *
# Register your models here.

class ConcesionesAdmin(admin.ModelAdmin):
    ordering = ['numero']
    list_display = ("numero", "numero_concesion", "comuna", "lugar", "tipo_tramite", "concesionario","tipo_vigencia")


admin.site.register(Concesiones,ConcesionesAdmin)