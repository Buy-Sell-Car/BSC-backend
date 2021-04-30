from django.urls import path, include
from .views import CarBrandAPIView, CarModelAPIView, ProfileAPIView, AdvertAPIView, MyTokenObtainPairView

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'brands', CarBrandAPIView)
router.register(r'models', CarModelAPIView)
router.register(r'profiles', ProfileAPIView)
router.register(r'adverts', AdvertAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
