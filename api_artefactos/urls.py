from rest_framework import routers

from .views import ArtefactoViewSet, ArtefactosViewSet

router = routers.SimpleRouter()

router.register(r'artefactos', ArtefactoViewSet)
router.register(r'artefacto', ArtefactosViewSet)


urlpatterns = router.urls
