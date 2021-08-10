from django.db import models


class CarModelManager(models.QuerySet):
    def is_brand(self, brand):
        return self.filter(brand=brand)