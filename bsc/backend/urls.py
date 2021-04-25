from django.urls import path, include
from .views import CarBrandAPIView, CarModelAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'brands', CarBrandAPIView)
router.register(r'models', CarModelAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
