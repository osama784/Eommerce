from django.core.management.base import BaseCommand
from vendors.models import Vendor

import random

class Command(BaseCommand):
    help = "Creating data every time"

    vendors = [
        {"name": 'XFOOD', 'address': 'US/Chicago'},
        {"name": 'Adap Fry', 'address': 'France/Paris'},
        {"name": 'Deep Nutrition Delivery', 'address': 'UK/England'},
        {"name": 'Donut Revolution', 'address': 'Indonesia/Surabaya'},
        {"name": 'Elegant Dinner', 'address': 'Germany/Frankfort'},
        {"name": 'Fantastic Food Fast', 'address': 'Germany/Munich'},
        {"name": 'Healthyappy', 'address': 'US/Los Angeles'},
    ]

    for vendor in vendors:
        phone_number_first = random.randint(100, 999)
        phone_number_second = random.randint(100, 999)
        phone_number_last = random.randint(100, 999)

        phone_number = f'+{phone_number_first}({phone_number_second}){phone_number_last}'
        Vendor.objects.get_or_create(**vendor, phone_number=phone_number)

