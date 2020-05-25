from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from ..views import restapi as views

__all__ = [
    'urlpatterns'
]

router = DefaultRouter()
router.register(r'game', views.GameViewSet)
router.register(r'faction', views.FactionViewSet)
router.register(r'army', views.ArmyViewSet)
router.register(r'unit', views.UnitViewSet)
router.register(r'unittype', views.UnitTypeViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
