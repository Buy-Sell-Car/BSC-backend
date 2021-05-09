from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CarBrand, CarModel, Profile, Advert, AdvertImage


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    brand = CarBrandSerializer()

    class Meta:
        model = CarModel
        fields = '__all__'


class AdvertImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertImage
        fields = '__all__'
        read_only_fields = ('advert', )


class AdvertSerializer(serializers.ModelSerializer):
    current_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    advertimage_set = AdvertImageSerializer(many=True, read_only=True)

    class Meta:
        model = Advert
        fields = '__all__'
        read_only_fields = ('advert_date', 'profile')

    def create(self, validated_data):
        user = validated_data.pop('current_user')
        validated_data['profile'] = Profile.objects.get(id=user.id)
        advert = super().create(validated_data)

        images_data = self.context['request'].FILES
        for img in images_data.getlist('file'):
            AdvertImage.objects.create(advert=advert, image=img)
        return advert


class ProfileForAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'city', 'tel')


class AdvertGetSerializer(serializers.ModelSerializer):
    carmodel = CarModelSerializer()
    profile = ProfileForAdvertSerializer()
    advertimage_set = AdvertImageSerializer(many=True)
    fuel = serializers.CharField(source='get_fuel_display')
    drive = serializers.CharField(source='get_drive_display')
    transmission = serializers.CharField(source='get_transmission_display')
    carbody = serializers.CharField(source='get_carbody_display')
    color = serializers.CharField(source='get_color_display')
    favourite = serializers.IntegerField(
        source='favourites.count', read_only=True)

    class Meta:
        model = Advert
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    favourite = AdvertGetSerializer(many=True, read_only=True)
    advert_set = AdvertGetSerializer(many=True, read_only=True)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = Profile
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'password', 'city', 'tel', 'favourite', 'advert_set')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        # and everything else you want to send in the response
        return data
