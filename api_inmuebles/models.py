from django.db import models
from django.utils import timezone

from api_entidades.models import Localidad


class Inmueble(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad_personas = models.IntegerField(default=1)
    antiguedad = models.IntegerField()
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Material(models.Model):
    nombre = models.CharField(max_length=255)
    conductividad = models.FloatField(max_length=6)

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
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
    etiqueta = models.IntegerField(choices=Etiqueta, default=A)
    fecha_desde = models.DateField(null=False, default=timezone.now)
    fecha_hasta = models.DateField(null=True, blank=True)
    borrado = models.BooleanField(default=False)

    inmueble = models.ForeignKey(Inmueble, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.etiqueta)


class Ambiente(models.Model):

    descripcion = models.CharField(max_length=255)
    volumen = models.FloatField(max_length=15)
    clasificacion = models.CharField(max_length=255)
    inmueble = models.ForeignKey(
        Inmueble, on_delete=models.PROTECT)

    def __str__(self):
        return self.descripcion


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

    NORTE = 'N'
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
    ancho=models.FloatField(max_length=15, default=0)
    alto = models.FloatField(max_length=15, default=0)
    es_externo = models.BooleanField(default=False)

    tipo = models.CharField(
        max_length=7, choices=TIPOS_CERRAMIENTO, default=PARED)
    orientacion = models.CharField(
        max_length=8, choices=TIPO_ORIENTACION, default=NORTE)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    ambiente = models.ManyToManyField(
        Ambiente, blank=True, null=True, related_name='cerramiento')
    cerramientos = models.ManyToManyField(
        'self', blank=True, null=True, related_name='cerramientos')

    def __str__(self):
        return self.denominacion
