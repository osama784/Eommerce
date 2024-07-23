from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coupon = models.CharField(max_length=20, null=True, blank=True)
    image = models.URLField(default='', blank=True, null=True)

    def __str__(self):
        return self.user.username