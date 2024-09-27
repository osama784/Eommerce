from django.core.management.base import BaseCommand
from products.models import Coupon

import random, string


class Command(BaseCommand):
    help = "Creating data every time"

    def handle(self, *args, **options):
        characters = string.ascii_letters + string.digits

        for i in range(30):
            coupon = ''.join(random.choice(characters) for _ in range(8))
            Coupon.objects.create(name=coupon)