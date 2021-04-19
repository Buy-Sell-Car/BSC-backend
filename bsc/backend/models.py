from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CarBrand(models.Model):
    name = models.CharField(max_length=255)


class CarModel(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
