from rest_framework import serializers

from .models import Entidad, Tarifa, Provincia, Partido, Localidad


class TarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarifa
        fields = '__all__'


class EntidadSerializer(serializers.ModelSerializer):

    tarifa = serializers.SerializerMethodField()

    def get_tarifa(self, obj):
        return list(obj.tarifa_set.all().values())

    class Meta:
        model = Entidad
        fields = ['id', 'nombre_entidad', 'tipo_entidad', 'tarifas', 'tarifa']


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'


class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = '__all__'


class LocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields = '__all__'
