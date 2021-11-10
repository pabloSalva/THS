from rest_framework import viewsets, response
from rest_framework.decorators import action

from .serializers import (
    EntidadSerializer,
    TarifaSerializer,
    ProvinciaSerializer,
    PartidoSerializer,
    LocalidadSerializer
)
from .models import Entidad, Tarifa, Provincia, Partido, Localidad


class EntidadViewSet(viewsets.ModelViewSet):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer


class TarifaViewSet(viewsets.ModelViewSet):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer

    @action(methods=['get'], detail=True, url_path='entidad')
    def get_entidad(self, request, *args, **kwargs):

        filtered_data_qs = self.filter_queryset(self.get_queryset())
        print(filtered_data_qs)
        # filtered_data = RolExportSerializer(filtered_data_qs, many=True).data
        # for f in filtered_data:
        #     if f['estado'] == "True":
        #         f['estado'] = "Activo"
        #     else:
        #         f['estado'] = "Inactivo"

        # headers = filtrar_export(request.GET.keys(), RolExportSerializer())

        # list_filters = filtrar_filtros_usados(
        #     request.GET.keys(), RolExportSerializer())

        # output = export_excel(user=request.user.username, headers=headers,
        #                       data=filtered_data, list_filters=list_filters)

        # output.seek(0)

        return response.Response(status=200)


class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer


class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer


class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
