from rest_framework import serializers
from rest_framework.authtoken.models import Token
from api_entidades.serializers import LocalidadSerializer


#from django.contrib.auth.models import User

from .models import Inmueble, Material, Cerramiento, Ambiente


class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = '__all__'


class CerramientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cerramiento
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class InmuebleSerializer(serializers.ModelSerializer):
    localidad = LocalidadSerializer()

    class Meta:
        model = Inmueble
        fields = ['nombre', 'cantidad_personas', 'antiguedad', 'localidad']
