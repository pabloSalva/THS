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
    LINEA_BLANCA = 1
    ELECTRONICA = 2
    ILUMINACION = 3
    CALEFACCION = 4

    CATEGORIA = (
        (AIRES, 'Aires'),
        (LINEA_BLANCA, 'Linea blanca'),
        (ELECTRONICA, 'Electronica'),
        (ILUMINACION, 'Iluminación'),
        (CALEFACCION, 'Calefacción')
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
    descripcion = models.CharField(max_length=50)
    marca = models.CharField(max_length=20, default="")
    modelo = models.CharField(max_length=20, default="")
    tipo = models.CharField(max_length=2,
                            choices=TIPOS,
                            default=ELECTRICO)

    users = models.ManyToManyField(User)
    ambientes = models.ManyToManyField(Ambiente, null=True, blank=True)


def __str__(self):
    return "%s %s" % (self.nombre_artefacto, str(self.consumo))
