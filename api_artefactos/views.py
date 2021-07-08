from rest_framework import viewsets, generics

from .serializers import ArtefactoSerializer#, UserSerlializer
from .models import Artefacto
# from django.contrib.auth.models import User


class ArtefactoViewSet(viewsets.ModelViewSet):
    queryset = Artefacto.objects.all()
    serializer_class = ArtefactoSerializer


# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = UserSerlializer
