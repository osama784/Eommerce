from django.core.management.base import BaseCommand
from products.models import Product, Vendor

import random


class Command(BaseCommand):
    help = "Creating data every time"

    vendors = Vendor.objects.all()

    products = [
        {
            "name": 'Velvet Cakes',
            "category": Product.CategoryChoices.DESSERTS,
        },
        {
            "name": 'Spatchcock BBQ Chicken', 
            "category": Product.CategoryChoices.MEAT_BEEF
        },
        {
            "name": 'Home-made BBQ Grilled Chicken', 
            "category": Product.CategoryChoices.MEAT_BEEF
        },
        {
            "name": 'Double Bief Fried Chicken Bacon', 
            "category": Product.CategoryChoices.BURGERS
        },
        {
            "name": 'Zesty Zucchini Zoodles', 
            "category": Product.CategoryChoices.SALADS_BOWLS
        },
        {
            "name": 'Savory Seaweed Sushi Rolls', 
            "category": Product.CategoryChoices.SUSHI
        },
        {
            "name": 'Mystical Mushroom Medley', 
            "category": Product.CategoryChoices.NUTS_SEEDS
        },
        {
            "name": 'Enchanted Elixir Soup', 
            "category": Product.CategoryChoices.SALADS_BOWLS
        },
        {
            "name": 'Whimsical Waffle Tower', 
            "category": Product.CategoryChoices.DESSERTS
        },
        {
            "name": 'Dragonfire Tacos', 
            "category": Product.CategoryChoices.VEGETABLES
        },
        {
            "name": 'Galactic Grilled Cheese', 
            "category": Product.CategoryChoices.BURGERS
        },
        {
            "name": 'Stardust Smoothie Bowl', 
            "category": Product.CategoryChoices.DESSERTS
        },
        {
            "name": "Fresh Juice",
            "category": Product.CategoryChoices.JUICE
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
    

    

    
        