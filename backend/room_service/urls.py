from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ApartmentFeatureViewSet, ApartmentImageViewSet, LocationViewSet, ApartmentViewSet, ApartmentTypeViewSet


router = DefaultRouter()

router.register(r'locations', LocationViewSet)
router.register(r'apartment-type', ApartmentTypeViewSet)
router.register(r'apartments', ApartmentViewSet)
router.register(r'apartment-image', ApartmentImageViewSet)
router.register(r'apartment-feature', ApartmentFeatureViewSet)

urlpatterns = [
    path('', include(router.urls))
]
