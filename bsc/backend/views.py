from django.shortcuts import render

# Create your views here.

from .models import CarBrand, CarModel, Profile

from rest_framework import viewsets
from .serializers import CarBrandSerializer, CarModelSerializer, ProfileSerializer


class CarBrandAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarModelAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class ProfileAPIView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
