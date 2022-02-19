from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ArtefactoSerializer, ArtefactosSerializer  # , UserSerlializer
from .models import Artefacto, Artefactos
from .filters import ArtefactoFilter, ArtefactosFilter
# from django.contrib.auth.models import User


class ArtefactoViewSet(viewsets.ModelViewSet):
    queryset = Artefacto.objects.all()
    serializer_class = ArtefactoSerializer
    filterset_class = ArtefactoFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre', 'consumo', 'marca_modelo__modelo','marca_modelo__marca__marca']

class ArtefactosViewSet(viewsets.ModelViewSet):
    queryset = Artefactos.objects.all()
    serializer_class = ArtefactosSerializer
    filterset_class = ArtefactosFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre', 'consumo', 'modelo']


# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = UserSerlializer
