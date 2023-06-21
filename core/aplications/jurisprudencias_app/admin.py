from django.contrib import admin
from .models import *
# Register your models here.

class JurisprudenciasAdmin(admin.ModelAdmin):
    list_display = ("rol", "caratulado", "tribunal", "fecha_sentencia", "ministro_redactor", "tipo_causa")


admin.site.register(Jurisprudencias,JurisprudenciasAdmin)
admin.site.register(Descriptores)