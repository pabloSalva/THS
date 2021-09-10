from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ArtefactoSerializer  # , UserSerlializer
from .models import Artefacto
from .filters import ArtefactoFilter
# from django.contrib.auth.models import User


class ArtefactoViewSet(viewsets.ModelViewSet):
    queryset = Artefacto.objects.all()
    serializer_class = ArtefactoSerializer
    filterset_class = ArtefactoFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre', 'consumo', 'marca']


# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = UserSerlializer
