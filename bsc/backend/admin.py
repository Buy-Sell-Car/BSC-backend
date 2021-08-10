from django.contrib import admin
from .models import CarBrand, CarModel, Advert, Profile, AdvertImage

# Register your models here.

admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(Advert)
admin.site.register(Profile)
admin.site.register(AdvertImage)