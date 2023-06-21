from django.db import models

# Create your models here.


class Jurisprudencias(models.Model):
    rol = models.CharField(max_length=50,primary_key=True)
    caratulado = models.CharField(max_length=200)
    tribunal = models.CharField(max_length=30)
    fecha_sentencia = models.CharField(max_length=30)
    tipo_causa = models.CharField(max_length=20)
    competencia = models.CharField(max_length=50)
    materia = models.CharField(max_length=50)
    ministro_redactor = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Jurisprudencia"
        verbose_name_plural = "Jurisprudencias"

    def __str__(self):
        return self.caratulado

class Descriptores(models.Model):
    name = models.CharField(max_length=50)
    Jurisprudencias = models.ManyToManyField(Jurisprudencias)

    class Meta:
        verbose_name = "Descriptor"
        verbose_name_plural = "Descriptores"

    def __str__(self):
        return self.name
    