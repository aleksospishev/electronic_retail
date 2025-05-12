from rest_framework.routers import DefaultRouter

from .views import RetailNodeViewSet

router = DefaultRouter()
router.register(r"nodes", RetailNodeViewSet, basename="retailnode")

urlpatterns = router.urls
