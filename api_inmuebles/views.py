from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import AmbienteSerializer, InmuebleSerializer, CerramientoSerializer, MaterialSerializer, InmuebleUpdateSerializer
from .models import Inmueble, Material, Cerramiento, Ambiente
from .filters import InmuebleFilter, AmbienteFilter, CerramientoFilter, MaterialFilter


class InmuebleViewSet(viewsets.ModelViewSet):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer
    filterset_class = InmuebleFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre', 'consumo', 'marca']

    serializers = {
        'default': InmuebleSerializer,
        'update': InmuebleUpdateSerializer,
        'create': InmuebleUpdateSerializer,

    }

    def get_serializer_class(self):
        """
        Devuelve un serializador en función del verbo HTTP.
        Si no está definido, devuelve el serializador
        por defecto.
        """

        return self.serializers.get(
            self.action, self.serializers["default"])


class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    filterset_class = AmbienteFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['volumen', 'descripcion']


class CerramientoViewSet(viewsets.ModelViewSet):
    queryset = Cerramiento.objects.all()
    serializer_class = CerramientoSerializer
    filterset_class = CerramientoFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['denominacion']


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filterset_class = MaterialFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['conductividad', 'nombre']
