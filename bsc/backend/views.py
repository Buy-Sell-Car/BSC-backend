from django.shortcuts import render, get_object_or_404
from rest_framework import status

# Create your views here.

from .models import CarBrand, CarModel, Profile, Advert

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    CarBrandSerializer, CarModelSerializer, ProfileSerializer,
    AdvertSerializer, AdvertGetSerializer, CustomTokenObtainPairSerializer)
from rest_framework import permissions
from .permissions import IsCurrentUserOrReadOnly, IsOwnerOrReadOnly


class CarBrandAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarModelAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

    def get_queryset(self):
        list_models = self.queryset
        query = self.request.query_params.get('brand')
        if (query):
            list_models = list_models.is_brand(query)

        return list_models


class ProfileAPIView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsCurrentUserOrReadOnly]


class AdvertAPIView(viewsets.ModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return AdvertGetSerializer
        return AdvertSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class PostView(APIView):

    def put(self, request, userpk, advertpk):
        post = get_object_or_404(Advert, pk=advertpk)
        if request.user.is_authenticated:
            profile = Profile.objects.get(id=request.user.id)
            if profile not in post.favourites.all():
                post.favourites.add(profile)
                return Response({'detail': 'User added to post'}, status=status.HTTP_200_OK)
            return Response({'detail': 'Already in favourite'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unathorized'}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, userpk, advertpk):
        post = get_object_or_404(Advert, pk=advertpk)
        if request.user.is_authenticated:
            profile = Profile.objects.get(id=request.user.id)
            if profile in post.favourites.all():
                post.favourites.remove(profile)
                return Response({'detail': 'User removed from post'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'detail': self.bad_request_message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unathorized'}, status=status.HTTP_401_UNAUTHORIZED)
