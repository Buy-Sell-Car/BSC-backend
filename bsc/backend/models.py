from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import uuid
import os
from phonenumber_field.modelfields import PhoneNumberField

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
    brand = models.ForeignKey(
        CarBrand, on_delete=models.CASCADE, verbose_name='марка автомобиля')

    def __str__(self):
        return "%s %s" % (self.brand, self.name)


class Profile(User):
    city = models.CharField(max_length=128, verbose_name='город')
    tel = PhoneNumberField(verbose_name='телефон')
    favourite = models.ManyToManyField(
        'Advert', verbose_name='закладки', blank=True, related_name='favourites')

    def __str__(self):
        return self.username


class Advert(models.Model):

    class Colors(models.TextChoices):
        BLACK = 'BK', _('Черный')
        SILVER = 'SI', _('Серебристый')
        WHITE = 'WH', _('Белый')
        GREY = 'GY', _('Серый')
        BLUE = 'BL', _('Синий')
        RED = 'RE', _('Красный')
        GREEN = 'GN', _('Зеленый')
        BROWN = 'BR', _('Коричневый')
        BEIGE = 'BE', _('Бежевый')
        YELLOW = 'YE', _('Желтый')
        PURPLE = 'PU', _('Фиолетовый')
        PINK = 'PI', _('Розовый')
        Orange = 'OR', _('Оранжевый')

    class Fuels(models.TextChoices):
        PETROL = 'PR', _('Бензин')
        DIESEL = 'DS', _('Дизель')
        ELECTRICITY = "EL", _('Электричество')

    class Drives(models.TextChoices):
        AWD = 'AW', _('Полный')
        RWD = 'RW', _('Задний')
        FWD = 'FW', _('Передний')

    class Transmissions(models.TextChoices):
        MANUAL = 'MT', _('Механическая')
        AUTO = 'AT', _('Автомат')
        CVT = 'CT', _('Вариатор')
        ROBOTIC = 'RT', _('Робот')

    class Body(models.TextChoices):
        SEDAN = 'SD', _('Седан')
        HATCHBACK = 'HB', _('Хэтчбэк')
        LIFTBACK = 'LB', _('Лифтбэк')
        SUV = 'SV', _('Внедорожник')
        COUPE = 'CP', _('Купе')
        CABRIO = 'CB', _('Кабриолет')
        WAGON = 'WG', _('Универсал')
        MINIVAN = 'MV', _('Минивэн')
        PICKUP = 'PC', _('Пикап')
        LIMOUSINE = 'LM', _('Лимузин')
        VAN = 'VN', _('Фургон')

    carmodel = models.ForeignKey(
        CarModel, on_delete=models.PROTECT, verbose_name='модель автомобиля')
    power = models.IntegerField(verbose_name='мощность двигателя (л.с.)')
    fuel = models.CharField(choices=Fuels.choices,
                            max_length=2, verbose_name='топливо')
    drive = models.CharField(choices=Drives.choices,
                             max_length=2, verbose_name='привод')
    transmission = models.CharField(
        choices=Transmissions.choices, max_length=2, verbose_name='коробка передач')
    carbody = models.CharField(
        choices=Body.choices, max_length=2, verbose_name='кузов')
    advert_date = models.DateField(
        auto_now_add=True, verbose_name='дата публикации')
    description = models.TextField(verbose_name='описание')
    price = models.IntegerField(verbose_name='стоимость (руб)')
    mileage = models.IntegerField(verbose_name='пробег (км)')
    prod_year = models.IntegerField(verbose_name='год выпуска')
    owners = models.IntegerField(verbose_name='количество владельцев по ПТС')
    color = models.CharField(choices=Colors.choices,
                             max_length=2, verbose_name='цвет')
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name='автор объявления')

    def __str__(self):
        return "%s %s %s" % (self.profile.username, self.carmodel, self.advert_date)


class AdvertImage(models.Model):
    advert = models.ForeignKey(
        Advert, on_delete=models.CASCADE, verbose_name='объявление')
    image = models.ImageField(
        upload_to=custom_save_path, verbose_name='изображение')
    default = models.BooleanField(default=False, verbose_name='стандартное')

    def __str__(self):
        return str(self.advert)
