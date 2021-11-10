from django.contrib import admin

from .models import Entidad, Tarifa, Localidad, Partido, Provincia


admin.site.register(Entidad)
admin.site.register(Tarifa)
admin.site.register(Localidad)
admin.site.register(Partido)
admin.site.register(Provincia)
