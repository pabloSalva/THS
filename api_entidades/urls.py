from rest_framework import routers

from .views import EntidadViewSet, TarifaViewSet, LocalidadViewSet

router = routers.SimpleRouter()

router.register(r'entidades', EntidadViewSet)
router.register(r'tarifas', TarifaViewSet)
router.register(r'localidades', LocalidadViewSet)


urlpatterns = router.urls
