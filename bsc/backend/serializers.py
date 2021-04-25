from rest_framework import serializers

from .models import CarBrand, CarModel, Profile, Advert


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    brand = CarBrandSerializer()

    class Meta:
        model = CarModel
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = Profile
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'password', 'city', 'tel')


class AdvertSerializer(serializers.ModelSerializer):
    current_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Advert
        fields = '__all__'
        read_only_fields = ('advert_date', 'profile')

    def create(self, validated_data):
        user = validated_data.pop('current_user')
        validated_data['profile'] = Profile.objects.get(id = user.id)
        return super().create(validated_data)


class AdvertGetSerializer(serializers.ModelSerializer):
    carmodel = CarModelSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = Advert
        fields = '__all__'
        read_only_fields = ('advert_date', 'profile')
