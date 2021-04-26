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
    name = models.CharField(max_length=255, verbose_name='Марка автомобиля')


class CarModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Модель автомобиля')
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name='Марка автомобиля')


class Profile(User):
    city = models.CharField(max_length=128, verbose_name='Город')
    tel = models.CharField(max_length=11, verbose_name='Телефон')


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

    carmodel = models.ForeignKey(CarModel, on_delete=models.PROTECT, verbose_name='Модель автомобиля')
    advert_date = models.DateField(auto_now_add=True, verbose_name='Дата  публикации')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Стоимость')
    mileage = models.IntegerField(verbose_name='Пробег')
    prod_year = models.IntegerField(verbose_name='Дата производства')
    owners = models.IntegerField(verbose_name='Количество владельцев по ПТС')
    color = models.CharField(choices=Colors.choices, max_length=2, verbose_name='Цвет')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Автор объявления')


class AdvertImage(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=custom_save_path)
    default = models.BooleanField(default=False)