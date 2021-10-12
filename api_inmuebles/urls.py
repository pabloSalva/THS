from rest_framework import routers

from .views import InmuebleViewSet, AmbienteViewSet, CerramientoViewSet, MaterialViewSet

router = routers.SimpleRouter()

router.register(r'inmuebles', InmuebleViewSet)
router.register(r'ambientes', AmbienteViewSet)
router.register(r'cerramientos', CerramientoViewSet)
router.register(r'materiales', MaterialViewSet)


urlpatterns = router.urls
