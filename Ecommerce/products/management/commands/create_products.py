from django.core.management.base import BaseCommand
from products.models import Product, Vendor, CategoryChoices

import random


class Command(BaseCommand):
    help = "Creating data every time"

    vendors = Vendor.objects.all()

    products = [
        {
            "name": 'Velvet Cakes',
            "category": CategoryChoices.DESSERTS,
        },
        {
            "name": 'Spatchcock BBQ Chicken', 
            "category": CategoryChoices.MEAT_BEEF
        },
        {
            "name": 'Home-made BBQ Grilled Chicken', 
            "category": CategoryChoices.MEAT_BEEF
        },
        {
            "name": 'Double Bief Fried Chicken Bacon', 
            "category": CategoryChoices.BURGERS
        },
        {
            "name": 'Zesty Zucchini Zoodles', 
            "category": CategoryChoices.SALADS_BOWLS
        },
        {
            "name": 'Savory Seaweed Sushi Rolls', 
            "category": CategoryChoices.SUSHI
        },
        {
            "name": 'Mystical Mushroom Medley', 
            "category": CategoryChoices.NUTS_SEEDS
        },
        {
            "name": 'Enchanted Elixir Soup', 
            "category": CategoryChoices.SALADS_BOWLS
        },
        {
            "name": 'Whimsical Waffle Tower', 
            "category": CategoryChoices.DESSERTS
        },
        {
            "name": 'Dragonfire Tacos', 
            "category": CategoryChoices.VEGETABLES
        },
        {
            "name": 'Galactic Grilled Cheese', 
            "category": CategoryChoices.BURGERS
        },
        {
            "name": 'Stardust Smoothie Bowl', 
            "category": CategoryChoices.DESSERTS
        },
        {
            "name": "Fresh Juice",
            "category": CategoryChoices.JUICE
        }
    ]
    previous = False
    for product in products:
        price = random.uniform(20.0, 300.0)
        life = random.randint(1, 100)
        if previous:
            discount = random.randint(1, 99)
            Product.objects.get_or_create(
                **product,
                vendor=random.choice(vendors),
                price=price,
                discount=discount,
                life=life
                    
            )
                       
        else:
            Product.objects.get_or_create(
                **product,
                vendor=random.choice(vendors),
                price=price,      
                life=life              
            )
                

        previous = not previous 
    

    

    
        