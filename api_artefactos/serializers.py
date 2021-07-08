from rest_framework import serializers
from rest_framework.authtoken.models import Token


#from django.contrib.auth.models import User

from .models import Artefacto


class ArtefactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artefacto
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
