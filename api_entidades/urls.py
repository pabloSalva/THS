from rest_framework import routers

from .views import EntidadViewSet, TarifaViewSet

router = routers.SimpleRouter()

router.register(r'entidades', EntidadViewSet)
router.register(r'tarifas', TarifaViewSet)


urlpatterns = router.urls
