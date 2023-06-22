from django.db import models

# Create your models here.
class Concesiones(models.Model):
    numero_concesion = models.CharField(max_length=80, primary_key=True)
    numero = models.IntegerField()
    tipo_concesion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=150)
    lugar = models.CharField(max_length=150)
    rs_ds = models.CharField(max_length=15)
    tipo_tramite = models.CharField(max_length=200)
    concesionario = models.CharField(max_length=150)
    tipo_vigencia = models.CharField(max_length=150)