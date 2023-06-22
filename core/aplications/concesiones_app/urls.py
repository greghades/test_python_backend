from django.urls import path
from .views import *
urlpatterns = [
    path('datos-concesiones/',cargar_datos,name="conseciones"),
    path('listar-datos/',listar_datos,name="listar-datos")
]


