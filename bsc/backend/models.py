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

    class Fuels(models.TextChoices):
        PETROL = 'PR', _('Petrol')
        DIESEL = 'DS', _('Diesel')
        ELECTRICITY = "EL", _('Electricity')

    class Drives(models.TextChoices):
        AWD = 'AW', _('All-wheel-drives')
        RWD = 'RW', _('Rear-whell-drives')
        FWD = 'FW', _('Front-whell-drives')
    
    class Transmissions(models.TextChoices):
        MANUAL = 'MT', _('Manual')
        AUTO = 'AT', _('Auto')
        CVT = 'CT', _('CVT')
        ROBOTIC = 'RT', _('Robotic')

    class Body(models.TextChoices):
        SEDAN = 'SD', _('Sedan')
        HATCHBACK = 'HB', _('Hatchback')
        LIFTBACK = 'LB', _('Liftback')
        SUV = 'SV', _('SUV')
        COUPE = 'CP', _('Coupe')
        CABRIO = 'CB', _('Cabrio')
        WAGON = 'WG', _('Wagon')
        MINIVAN = 'MV', _('Minivan')
        PICKUP = 'PC', _('Pickup')
        LIMOUSINE = 'LM', _('Limousine')
        VAN = 'VN', _('Van')

    carmodel = models.ForeignKey(CarModel, on_delete=models.PROTECT, verbose_name='модель автомобиля')
    power = models.IntegerField(verbose_name='мощность двигателя (л.с.)')
    fuel = models.CharField(choices=Fuels.choices, max_length=2, verbose_name='топливо')
    drive = models.CharField(choices=Drives.choices, max_length=2, verbose_name='привод')
    transmission = models.CharField(choices=Transmissions.choices, max_length=2, verbose_name='коробка передач')
    carbody = models.CharField(choices=Body.choices, max_length=2, verbose_name='кузов')
    advert_date = models.DateField(auto_now_add=True, verbose_name='дата публикации')
    description = models.TextField(verbose_name='описание')
    price = models.IntegerField(verbose_name='стоимость (руб)')
    mileage = models.IntegerField(verbose_name='пробег (км)')
    prod_year = models.IntegerField(verbose_name='год выпуска')
    owners = models.IntegerField(verbose_name='количество владельцев по ПТС')
    color = models.CharField(choices=Colors.choices, max_length=2, verbose_name='цвет')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='автор объявления')

    def __str__(self):
        return "%s %s %s" % (self.profile.username, self.carmodel, self.advert_date)
    

class AdvertImage(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, verbose_name='объявление')
    image = models.ImageField(upload_to=custom_save_path, verbose_name='изображение')
    default = models.BooleanField(default=False, verbose_name='стандартное')

    def __str__(self):
        return str(self.advert)
    