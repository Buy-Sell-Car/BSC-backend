from rest_framework import serializers

from .models import CarBrand, CarModel


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    brand = CarBrandSerializer()

    class Meta:
        model = CarModel
        fields = '__all__'
