from django.db import models
#from django.contrib.auth.models import User
from authentication.models import User

class Entidad(models.Model):
    """Clase de entidades que suministran servicios eléctricos y de gas"""

    ELECTRICA = 'EL'
    GAS = 'GS'
    TIPOS = [
        (ELECTRICA, 'Electrica'),
        (GAS, 'Gas'),
    ]
    user = models.ManyToManyField(User, related_name=None)
    nombre_entidad = models.CharField(max_length=50)
    tipo_entidad = models.CharField(
            max_length=2,
            choices=TIPOS,
            default=ELECTRICA
        )

    def __str__(self):
        return self.nombre_entidad


class Tarifa(models.Model):
    """Clase de las tarifas de cada entidad"""

    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    fecha_inicio_tarifa = models.DateField(null=False)
    fecha_fin_tarifa = models.DateField(editable=True, blank=True, null=True)
    precio_unitario = models.FloatField(max_length=8, blank=False, null=False)
    codigo = models.CharField(max_length=50)
    consumo_minimo = models.IntegerField(max_length=5)
    consumo_maximo = models.IntegerField(max_length=6)
    cargo_fijo = models.FloatField(max_length=8)
    tipo_tarifa = models.CharField(max_length=50)


class Provincia(models.Model):
    nombre_provincia = models.CharField(max_length=20)


class Partido(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nombre_partido = models.CharField(max_length=20)


class Localidad(models.Model):
    entidad = models.ManyToManyField(Entidad, related_name='entidad')
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    nombre_localidad = models.CharField(max_length=20)
    zona_bioambiental = models.CharField(max_length=20)
