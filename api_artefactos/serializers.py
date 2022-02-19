from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist


#from django.contrib.auth.models import User

from .models import Artefacto, Artefactos, Marca, Modelo

class ModeloSerializer(serializers.ModelSerializer):
    
    marca = serializers.SerializerMethodField() 
    class Meta:
        model = Modelo
        fields = [
            'id',
            'modelo',
            'marca'
        ]
    def get_marca(self, obj):
        try:
            marca = Marca.objects.get(id=obj.marca.id)
        except ObjectDoesNotExist:
            return None
        return marca.marca

class ArtefactoSerializer(serializers.ModelSerializer):
    marca_modelo = ModeloSerializer()
    modelo = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Artefacto
        fields = [
            'id',
            'etiqueta',
            'nombre',
            'consumo',
            'calor_residual',
            'categoria',
            'descripcion',
            'modelo',
            'marca_modelo',
            'tipo',
            'users',
            'ambientes'
        ]
    def get_modelo(self, obj):
        try:
            modelo = Modelo.objects.get(id=obj.marca_modelo_id)
        except ObjectDoesNotExist:
            return None
        return modelo.modelo
class ArtefactosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artefactos
        fields = '__all__'


# class UserSerlializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User(
#             email=validated_data['email'],
#             username=validated_data['username']
#             )
#         user.set_password(validated_data['password'])
#         user.save()
#         Token.objects.create(user=user)
#         return user
