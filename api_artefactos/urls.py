from rest_framework import routers

from .views import ArtefactoViewSet

router = routers.SimpleRouter()

router.register(r'artefactos', ArtefactoViewSet)


urlpatterns = router.urls
