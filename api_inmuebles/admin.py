from django.contrib import admin

from .models import Etiqueta, Inmueble, Cerramiento, Material, Ambiente


admin.site.register(Inmueble)
admin.site.register(Cerramiento)
admin.site.register(Material)
admin.site.register(Ambiente)
admin.site.register(Etiqueta)
