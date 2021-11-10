# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_filters import rest_framework as filters

from .models import Artefacto


class ArtefactoFilter(filters.FilterSet):
    consumo = filters.NumberFilter(
        field_name='consumo', lookup_expr='icontains')
    etiqueta = filters.NumberFilter(
        field_name='etiqueta', lookup_expr='icontains')
    categoria = filters.NumberFilter(
        field_name='categoria', lookup_expr='icontains')

    nombre = filters.CharFilter(
        field_name='nombre', lookup_expr="icontains")
    marca = filters.CharFilter(
        field_name='marca', lookup_expr="icontains")

    class Meta:
        model = Artefacto
        fields = ['consumo', 'etiqueta', 'categoria',
                  'nombre', 'marca']
