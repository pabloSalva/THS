# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_filters import rest_framework as filters

from .models import Artefacto, Artefactos


class ArtefactoFilter(filters.FilterSet):
    consumo = filters.NumberFilter(
        field_name='consumo')
    etiqueta = filters.NumberFilter(
        field_name='etiqueta')
    categoria = filters.NumberFilter(
        field_name='categoria')

    nombre = filters.CharFilter(
        field_name='nombre', lookup_expr="icontains")
    marca_modelo= filters.CharFilter(
        field_name='marca_modelo__modelo', lookup_expr="icontains")

    marca = filters.CharFilter(field_name='marca_modelo__marca__marca', lookup_expr='icontains')
    # modelo = filters.CharFilter(
    #     field_name='marca_modelo__modelo', lookup_expr="icontains")

    class Meta:
        model = Artefacto
        fields = ['consumo', 'etiqueta', 'categoria',
                  'nombre', 'marca_modelo__modelo','marca_modelo__marca__marca']

class ArtefactosFilter(filters.FilterSet):
    consumo = filters.NumberFilter(
        field_name='consumo')

    nombre = filters.CharFilter(
        field_name='nombre')
    marca_modelo = filters.CharFilter(
        field_name='marca_modelo')

    class Meta:
        model = Artefactos
        fields = ['consumo', 'nombre', 'marca_modelo']
