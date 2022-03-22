from django.db import models

#from django.contrib.auth.models import User
from authentication.models import User
from api_inmuebles.models import Ambiente


class Marca(models.Model):
    marca = models.CharField(max_length=20)

    def __str__(self):
        return self.marca

class Modelo(models.Model):
    modelo = models.CharField(max_length=30)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT )

    def __str__(self):
        return self.marca.marca + " " + self.modelo

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
    etiqueta = models.IntegerField(choices=Etiqueta, max_length=4, default=A)
    nombre = models.CharField(max_length=50)
    consumo = models.IntegerField(default=0)
    calor_residual = models.FloatField(default=0.0)
    categoria = models.IntegerField(choices=CATEGORIA, default=AIRES)
    descripcion = models.CharField(max_length=500)
    marca_modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)
    tipo = models.CharField(max_length=2,
                            choices=TIPOS,
                            default=ELECTRICO)

    users = models.ManyToManyField(User)
    ambientes = models.ManyToManyField(Ambiente, null=True, blank=True)

    def __str__(self):
        return self.nombre




class Artefacto2(models.Model):
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
    etiqueta = models.IntegerField(choices=Etiqueta, max_length=4, default=A)
    nombre = models.CharField(max_length=50)
    consumo = models.IntegerField(default=0)
    calor_residual = models.FloatField(default=0.0)
    categoria = models.IntegerField(choices=CATEGORIA, default=AIRES)
    descripcion = models.CharField(max_length=500)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=2,
                            choices=TIPOS,
                            default=ELECTRICO)

    users = models.ManyToManyField(User)
    ambientes = models.ManyToManyField(Ambiente, null=True, blank=True)

    def __str__(self):
        return self.nombre



class Artefactos(models.Model):
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

    # MARCA_MODELO = [
    # ('BGH', (
    #         ('bb55', 'bb55'),
    #         ('bb56', 'bb56'),
    #     )
    # ),
    # ('DREAN', (
    #         ('fuzy22', 'Fuzy22'),
    #         ('blue9.0', 'blue9.0'),
    #     )
    # ),
    # ]

    MARCA = [
        ('BGH','BGH'),('DREAN','DREAN')
    ]

    class ModelosChoices():
        MODELOS = [
            ('bb55', 'bb55'),
            ('bb56', 'bb56'),
            ('fuzy22', 'Fuzy22'),
            ('blue9.0', 'blue9.0'),
        ]

        MARCA_MODELO = {
            'BGH':[
            ('bb55', 'bb55'),
            ('bb56', 'bb56'),
            ],
            'DREAN':[('fuzy22', 'Fuzy22'),
            ('blue9.0', 'blue9.0'),]
        }
        @classmethod
        def obtener_modelos_clases(cls, marca):
            return cls.MARCA_MODELO.get(marca, cls.MODELOS)
    etiqueta = models.IntegerField(choices=Etiqueta, max_length=4, default=A)
    nombre = models.CharField(max_length=50)
    consumo = models.IntegerField(default=0)
    calor_residual = models.FloatField(default=0.0)
    categoria = models.IntegerField(choices=CATEGORIA, default=AIRES)
    descripcion = models.CharField(max_length=500)
    marca = models.CharField(choices=MARCA, max_length=50, null=True)
    modelo = models.CharField(choices=ModelosChoices.obtener_modelos_clases(marca), max_length=50,null=True)
    tipo = models.CharField(max_length=2,
                            choices=TIPOS,
                            default=ELECTRICO)

    users = models.ManyToManyField(User)
    ambientes = models.ManyToManyField(Ambiente, null=True, blank=True)

    def __str__(self):
        return self.nombre
