from django.contrib import admin

from .models import Artefacto, Artefacto2, Artefactos, Marca, Modelo


admin.site.register(Artefacto)
admin.site.register(Artefactos)
admin.site.register(Artefacto2)
admin.site.register(Marca)
admin.site.register(Modelo)
