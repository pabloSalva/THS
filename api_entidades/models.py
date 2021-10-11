from django.db import models


class Entidad(models.Model):
    """Clase de entidades que suministran servicios eléctricos y de gas"""

    ELECTRICA = 'EL'
    GAS = 'GS'
    TIPOS = [
        (ELECTRICA, 'Electrica'),
        (GAS, 'Gas'),
    ]
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

    fecha_inicio_tarifa = models.DateField(null=False)
    fecha_fin_tarifa = models.DateField(editable=True, blank=True, null=True)
    categoria = models.CharField(max_length=50)
    sub_categoria = models.CharField(max_length=50)
    consumo_minimo = models.IntegerField()
    consumo_maximo = models.IntegerField(null=True)
    cargo_fijo = models.FloatField(max_length=8)
    precio_unitario = models.FloatField(max_length=8, blank=False, null=False)
    descripcion = models.CharField(max_length=50)

    localidad = models.ForeignKey(
        "Localidad", on_delete=models.PROTECT)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


class Provincia(models.Model):
    nombre_provincia = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_provincia


class Partido(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nombre_partido = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_partido


class Localidad(models.Model):
    entidad = models.ManyToManyField(
        Entidad, null=True, blank=True, related_name='entidad')
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    nombre_localidad = models.CharField(max_length=20)
    zona_bioambiental = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_localidad
