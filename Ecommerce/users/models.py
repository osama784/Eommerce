from django.db import models
from django.conf import settings

from . import utils as users_utils

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=users_utils.profile_image_upload, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.IntegerField(null=True, blank=True)

    @property
    def get_country(self):
        address = self.address.split(',')
        return address[0]

    @property
    def get_city(self):
        address = self.address.split(',')
        if len(address) == 1:
            return None
        return address[1]

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ['id']
        