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

    CATEGORIA = (
        (AIRES, 'Aires'),
        (HELADERAS, 'heladeras'),
        (ELECTRONICA, 'Electronica'),
        (ILUMINACION, 'Iluminación'),
        (LAVARROPAS, 'Lavarropas'),
        (COCINA, 'Cocina'),
        (CALEFACCION, 'Calefacción'),
        (BAÑO, 'Baño')
    )

    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7
    I = 8
    J = 9

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
    etiqueta = models.IntegerField(choices=Etiqueta, default=A)
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
