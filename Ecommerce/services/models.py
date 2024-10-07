from django.db import models

from users.models import Profile

class ContactMessage(models.Model):
    owner = models.ForeignKey(Profile, models.CASCADE)
    first_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(max_length=200)