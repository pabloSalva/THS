from django.db import models
from api_entidades.models import Localidad
from api_artefactos.models import Artefacto


class Inmueble(models.Model):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6

    Etiqueta = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
        (D, 'D'),
        (E, 'E'),
        (F, 'F'),
        (G, 'G'),
    )

    nombre = models.CharField(max_length=255)
    cantidad_personas = models.IntegerField(default=1)
    antiguedad = models.IntegerField()
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT)
    estiqueta = models.IntegerField(choices=Etiqueta, default=A)

    def __str__(self):
        return self.nombre

class Material(models.Model):
    nombre = models.CharField(max_length=255)
    conductividad = models.FloatField(max_length=6)

    def __str__(self):
        return self.nombre


class Cerramiento(models.Model):
    VENTANA = 'Ventana'
    TECHO = 'Techo'
    PARED = 'Pared'
    PUERTA = 'Puerta'
    TIPOS_CERRAMIENTO = [
        (VENTANA, 'ventana'),
        (TECHO, 'techo'),
        (PARED, 'pared'),
        (PUERTA, 'puerta')
    ]

    NORTE ='N'
    SUR = 'S'
    ESTE = 'E'
    OESTE = 'O'
    NOROESTE = 'NO'
    SURESTE = 'SE'
    NORESTE = 'NE'
    SUROESTE = 'SO'
    TIPO_ORIENTACION = [
        (NORTE, 'norte'),
        (SUR, 'sur'),
        (ESTE, 'este'),
        (OESTE, 'oeste'),
        (NOROESTE, 'noroeste'),
        (SURESTE, 'sureste'),
        (NORESTE, 'noreste'),
        (SUROESTE, 'sureste'),
    ]

    denominacion = models.CharField(max_length=255)
    superficie = models.FloatField(max_length=15)
    es_externo = models.BooleanField(default=False)

    tipo = models.CharField(max_length=7, choices=TIPOS_CERRAMIENTO, default=PARED)
    orientacion = models.CharField(max_length=8, choices=TIPO_ORIENTACION, default=NORTE)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)

    def __str__(self):
        return self.denominacion

class Ambiente(models.Model):

    descripcion = models.CharField(max_length=255)
    volumen = models.FloatField(max_length=15)
    clasificacion = models.CharField(max_length=255)
    cerramiento = models.ForeignKey(Cerramiento, on_delete=models.PROTECT) 
    artefacto = models.ForeignKey(Artefacto, on_delete=models.PROTECT)