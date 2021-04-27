from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import uuid
import os

# Create your models here.

def custom_save_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/', filename)


class CarBrand(models.Model):
    name = models.CharField(max_length=255, verbose_name='марка автомобиля')

    def __str__(self):
        return self.name
    

class CarModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='модель автомобиля')
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name='марка автомобиля')
    
    def __str__(self):
        return "%s %s" % (self.brand, self.name)
    


class Profile(User):
    city = models.CharField(max_length=128, verbose_name='город')
    tel = models.CharField(max_length=11, verbose_name='телефон')

    def __str__(self):
        return self.username
    


class Advert(models.Model):

    class Colors(models.TextChoices):
        BLACK = 'BK', _('Black')
        SILVER = 'SI', _('Silver')
        WHITE = 'WH', _('White')
        GREY = 'GY', _('Grey')
        BLUE = 'BL', _('Blue')
        RED = 'RE', _('Red')
        GREEN = 'GN', _('Green')
        BROWN = 'BR', _('Brown')
        BEIGE = 'BE', _('Beige')
        YELLOW = 'YE', _('Yellow')
        PURPLE = 'PU', _('Purple')
        PINK = 'PI', _('Pink')
        Orange = 'OR', _('Orange')

    carmodel = models.ForeignKey(CarModel, on_delete=models.PROTECT, verbose_name='модель автомобиля')
    advert_date = models.DateField(auto_now_add=True, verbose_name='дата публикации')
    description = models.TextField(verbose_name='описание')
    price = models.IntegerField(verbose_name='стоимость')
    mileage = models.IntegerField(verbose_name='пробег')
    prod_year = models.IntegerField(verbose_name='дата производства')
    owners = models.IntegerField(verbose_name='количество владельцев по ПТС')
    color = models.CharField(choices=Colors.choices, max_length=2, verbose_name='цвет')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='автор объявления')

    def __str__(self):
        return "%s %s " % (self.carmodel, self.description)
    

class AdvertImage(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, verbose_name='объявление')
    image = models.ImageField(upload_to=custom_save_path, verbose_name='изображение')
    default = models.BooleanField(default=False, verbose_name='стандартное')

    def __str__(self):
        return str(self.advert)
    