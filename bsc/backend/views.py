from django.shortcuts import render

# Create your views here.

from .models import CarBrand, CarModel, Profile, Advert

from rest_framework import viewsets
from .serializers import (
    CarBrandSerializer, CarModelSerializer, ProfileSerializer, 
    AdvertSerializer, AdvertGetSerializer)
from rest_framework import permissions
from .permissions import IsCurrentUserOrReadOnly, IsOwnerOrReadOnly


class CarBrandAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarModelAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class ProfileAPIView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOrReadOnly]


class AdvertAPIView(viewsets.ModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return AdvertGetSerializer
        return AdvertSerializer
