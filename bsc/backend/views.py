from django.shortcuts import render

# Create your views here.

from .models import CarBrand, CarModel

from rest_framework import viewsets
from .serializers import CarBrandSerializer, CarModelSerializer


class CarBrandAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarModelAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
