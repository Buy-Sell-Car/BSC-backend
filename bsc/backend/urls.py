from django.urls import path, include
from .views import CarBrandAPIView, CarModelAPIView, ProfileAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'brands', CarBrandAPIView)
router.register(r'models', CarModelAPIView)
router.register(r'profile', ProfileAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
