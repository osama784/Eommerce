from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    image = models.URLField(default='')

    def __str__(self):
        return self.name