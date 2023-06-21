from django.urls import path
from .views import *
urlpatterns = [
    path('agregar-datos/',Obtener_datos,name="agregar-datos"),
    path('busqueda/',Busqueda,name="busqueda"),
    path('listar/',Listar,name="listar"),
]
