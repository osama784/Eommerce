from django.core.management.base import BaseCommand

from vendors.models import Vendor, Rating
from users.models import Profile
import random

class Command(BaseCommand):
    vendors = Vendor.objects.all()
    profiles = Profile.objects.all()

    for i in range(30):
        profile = profiles[i]
        vendor = vendors[i % 7]
        data = {
            'ship_rating': random.randint(1, 5),
            'chat_rating': random.randint(1, 5),
            'products_quality_rating': random.randint(1, 5),
        }

        Rating.objects.create(owner=profile, vendor=vendor, **data)