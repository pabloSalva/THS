from __future__ import unicode_literals

from rest_framework import viewsets, generics, filters, response, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from .utils import conductividad, hay_techo

from .serializers import AmbienteSerializer, InmuebleSerializer, CerramientoSerializer, MaterialSerializer, InmuebleUpdateSerializer
from .models import Etiqueta, Inmueble, Material, Cerramiento, Ambiente
from .filters import InmuebleFilter, AmbienteFilter, CerramientoFilter, MaterialFilter
from api_artefactos.models import Artefacto
from api_artefactos.serializers import ArtefactoSerializer



from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.translation import ugettext as _

class ConflictError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Conflict'


class InmuebleViewSet(viewsets.ModelViewSet):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer
    filterset_class = InmuebleFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['direccion']

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

    @action(methods=['get'], detail=False, url_name='etiqueta', url_path='etiqueta')
    def etiqueta(self, request, *args, **kwargs):        
        inmueble = Inmueble.objects.get(id=int(request.query_params['inmueble']))
        etiqueta = inmueble.etiqueta_set.all().last()

        return JsonResponse({'etiqueta': etiqueta.etiqueta}, status=status.HTTP_200_OK)
    
    @action(methods=['post'], detail=False, url_name='etiqueta-create', url_path='etiqueta-create')
    def etiqueta_create(self, request, *args, **kwargs):
        domicilio = int(request.data['idDomicilio'])
        try:
            inmueble = Inmueble.objects.get(id=domicilio)
        except ObjectDoesNotExist:
            pass
        ambientes = Ambiente.objects.filter(inmueble=domicilio)
        conductividad_total = 0
        calor_cerramientos = 0
        calor_residual_artefactos = 0
        calor_residual_persona = 126*inmueble.cantidad_personas
        if ambientes:
            for ambiente in ambientes:
                cerramientos = Cerramiento.objects.filter(ambiente=ambiente)
                if cerramientos.count() > 4:
                    if hay_techo(cerramientos):
                        for cerramiento in cerramientos:
                            superficie_cerramiento = cerramiento.alto * cerramiento.ancho
                            conductividad_total += conductividad(cerramiento)
                            calor_cerramientos += superficie_cerramiento*conductividad_total
                    else:
                        raise ConflictError(detail=_("Falta agregar Techo a un Ambiente"))  

                else:
                    raise ConflictError(detail=_("La cantidad de cerramientos en uno de los ambientes es menor que 5"))  

                artefactos = Artefacto.objects.filter(ambientes=ambiente.id)
                for artefacto in artefactos:
                    calor_residual_artefactos += artefacto.calor_residual

                
        else:
            raise ConflictError(detail=_("El domicilio no tiene ambientes cargados")) 
        carga_latente = calor_residual_persona + calor_residual_artefactos
        eficiencia = calor_cerramientos/(calor_cerramientos + carga_latente)
        
        if  eficiencia >= 0.9:
            etiqueta_value=0
        elif eficiencia < 0.9 and eficiencia >= 0.8:
            etiqueta_value=1
        elif eficiencia < 0.8 and eficiencia >= 0.7:
            etiqueta_value=1
        elif eficiencia < 0.7 and eficiencia >= 0.6:
            etiqueta_value=1
        elif eficiencia < 0.6 and eficiencia >= 0.5:
            etiqueta_value=1
        elif eficiencia < 0.5 and eficiencia >= 0.25:
            etiqueta_value=1
        else:
            etiqueta_value=6
        Etiqueta.objects.create(
            etiqueta=etiqueta_value,
            inmueble=inmueble
        )
        data = {'etiqueta': etiqueta_value}
        return response.Response(data, status=status.HTTP_201_CREATED)

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    filterset_class = AmbienteFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['volumen', 'descripcion', 'inmueble']

    @action(methods=['put'], detail=False, url_name='artefactos', url_path='artefactos')
    def artefactos(self, request, *args, **kwargs):
        ambiente_request = int(request.data['ambiente'])
        artefactos = request.data['artefactos']

        for artefacto in artefactos:
            try:
                artefacto_carga = Artefacto.objects.get(id=artefacto)
                artefacto_carga.ambientes.add(ambiente_request)
                artefacto_carga.save()
            except ObjectDoesNotExist:
                return None
            
        return response.Response({'status': 'OK'}, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=False, url_name='artefactos-ambiente', url_path='artefactos-ambiente')
    def artefactos_ambiente(self, request, *args, **kwargs):        
        artefactos = Artefacto.objects.filter(ambientes=int(request.query_params['ambiente']))
        artefactos_validated = ArtefactoSerializer(artefactos, many=True)  

        return JsonResponse({'data': artefactos_validated.data}, status=status.HTTP_201_CREATED)
    
    @action(methods=['patch'], detail=False, url_name='artefactos-ambiente-delete', url_path='artefactos-ambiente-delete')
    def artefactos_ambiente_delete(self, request, *args, **kwargs):        
        try:
            artefacto = Artefacto.objects.get(id=request.data['idArtefacto'])
            artefacto.ambientes.remove(int(request.data['idAmbiente']))
            artefacto.save()
        except ObjectDoesNotExist:
            return None
        return response.Response({'status': 'OK'}, status=status.HTTP_201_CREATED)


class CerramientoViewSet(viewsets.ModelViewSet):
    queryset = Cerramiento.objects.all()
    serializer_class = CerramientoSerializer
    filterset_class = CerramientoFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['denominacion', 'ambiente']


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filterset_class = MaterialFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['conductividad', 'nombre']

# class EtiquetaViewSet(viewsets.ModelViewSet):
#     queryset = Etiqueta.objects.all()
#     serializer_class = EtiquetaSerializer
#     filterset_class = EtiquetaFilter
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend]
#     search_fields = ['conductividad', 'nombre']
