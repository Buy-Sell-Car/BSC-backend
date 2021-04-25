from django.urls import path, include
from .views import CarBrandAPIView, CarModelAPIView, ProfileAPIView, AdvertAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'brands', CarBrandAPIView)
router.register(r'models', CarModelAPIView)
router.register(r'profiles', ProfileAPIView)
router.register(r'adverts', AdvertAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
