# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_filters import rest_framework as filters

from .models import Inmueble, Material, Cerramiento, Ambiente


class InmuebleFilter(filters.FilterSet):
    direccion = filters.CharFilter(
        field_name='direccion', lookup_expr="icontains")
    etiqueta = filters.NumberFilter(
        field_name='etiqueta_set__etiqueta'
    )

    class Meta:
        model = Inmueble
        fields = ['direccion', 'etiqueta']


class MaterialFilter(filters.FilterSet):

    conductividad = filters.NumberFilter(
        field_name='conductividad', lookup_expr='icontains')
    nombre = filters.CharFilter(
        field_name='nombre', lookup_expr="icontains")

    class Meta:
        model = Material
        fields = ['nombre', 'conductividad']


class CerramientoFilter(filters.FilterSet):

    denominacion = filters.CharFilter(
        field_name='denominacion', lookup_expr="icontains")
    ambiente = filters.NumberFilter(field_name='ambiente')
    class Meta:
        model = Cerramiento
        fields = ['denominacion','ambiente']


class AmbienteFilter(filters.FilterSet):

    volumen = filters.NumberFilter(
        field_name='volumen', lookup_expr='icontains')

    descripcion = filters.CharFilter(
        field_name='descripcion', lookup_expr="icontains")
    inmueble = filters.NumberFilter(field_name='inmueble')

    class Meta:
        model = Ambiente
        fields = ['volumen', 'descripcion', 'inmueble']
