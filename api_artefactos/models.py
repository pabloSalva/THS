from django.db import models

#from django.contrib.auth.models import User
from authentication.models import User
from api_inmuebles.models import Ambiente


class Artefacto(models.Model):
    ELECTRICO = 'EL'
    GAS = 'GS'
    TIPOS = [
        (ELECTRICO, 'Electrico'),
        (GAS, 'Gas'),
    ]
    AIRES = 0
    HELADERAS = 1
    ELECTRONICA = 2
    ILUMINACION = 3
    COCINA = 4
    LAVARROPAS = 5
    CALEFACCION = 6
    BAÑO = 7
    AGUA = 8

    CATEGORIA = (
        (AIRES, 'Aires'),
        (HELADERAS, 'heladeras'),
        (ELECTRONICA, 'Electronica'),
        (ILUMINACION, 'Iluminación'),
        (LAVARROPAS, 'Lavarropas'),
        (COCINA, 'Cocina'),
        (CALEFACCION, 'Calefacción'),
        (BAÑO, 'Baño'),
        (AGUA, 'Agua')
    )

    A = 'A+++'
    B = 'A++'
    C = 'A+'
    D = 'A'
    E = 'B'
    F = 'C'
    G = 'D'
    H = 'E'
    I = 'F'
    J = 'G'

    Etiqueta = (
        (A, 'A+++'),
        (B, 'A++'),
        (C, 'A+'),
        (D, 'A'),
        (E, 'B'),
        (F, 'C'),
        (G, 'D'),
        (H, 'E'),
        (I, 'F'),
        (J, 'G'),
    )
    etiqueta = models.CharField(choices=Etiqueta, max_length=4, default=A)
    nombre = models.CharField(max_length=50)
    consumo = models.IntegerField(default=0)
    calor_residual = models.FloatField(default=0.0)
    categoria = models.IntegerField(choices=CATEGORIA, default=AIRES)
    descripcion = models.CharField(max_length=500)
    marca = models.CharField(max_length=20, default="")
    modelo = models.CharField(max_length=20, default="")
    tipo = models.CharField(max_length=2,
                            choices=TIPOS,
                            default=ELECTRICO)

    users = models.ManyToManyField(User)
    ambientes = models.ManyToManyField(Ambiente, null=True, blank=True)

    def __str__(self):
        return self.nombre
