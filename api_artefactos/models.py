from django.db import models

#from django.contrib.auth.models import User
from authentication.models import User

class Artefacto(models.Model):
    users = models.ManyToManyField(User, related_name=None)
    nombre_artefacto = models.CharField(max_length=50)
    consumo = models.IntegerField(default=0)
    eficiencia = models.CharField(max_length=4)
    categoria = models.CharField(max_length=20, default="Aires")
    descripcion = models.CharField(max_length=50)
    marca = models.CharField(max_length=20, default="S/N")
    modelo = models.CharField(max_length=20, default="S/N")
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s" % (self.nombre_artefacto, str(self.consumo))
