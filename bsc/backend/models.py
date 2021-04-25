from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.


class CarBrand(models.Model):
    name = models.CharField(max_length=255)


class CarModel(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)


class Profile(User):
    city = models.CharField(max_length=128)
    tel = models.CharField(max_length=11)


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

    carmodel = models.ForeignKey(CarModel, on_delete=models.PROTECT)
    advert_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()
    mileage = models.IntegerField()
    prod_year = models.IntegerField()
    owners = models.IntegerField()
    color = models.CharField(choices=Colors.choices, max_length=2)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
