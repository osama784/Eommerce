from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User

from products.models import Product, Vendor, Review, Order
from users.models import Profile

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

    vendors = Vendor.objects.all()

    products = [
        {
            "name": 'Velvet Cakes',
            "color": "brown",
            "type": Product.TypeChoices.DESSERTS
        },
        {
            "name": 'Spatchcock BBQ Chicken', 
            "color": "red",
            "type": Product.TypeChoices.MEAT_BEEF
        },
        {
            "name": 'Home-made BBQ Grilled Chicken', 
            "color": "red",
            "type": Product.TypeChoices.MEAT_BEEF
        },
        {
            "name": 'Double Bief Fried Chicken Bacon', 
            "color": "amber",
            "type": Product.TypeChoices.BURGERS
        },
        {
            "name": 'Zesty Zucchini Zoodles', 
            "color": "green",
            "type": Product.TypeChoices.SALADS_BOWLS
        },
        {
            "name": 'Savory Seaweed Sushi Rolls', 
            "color": "green",
            "type": Product.TypeChoices.SUSHI
        },
        {
            "name": 'Mystical Mushroom Medley', 
            "color": "brown",
            "type": Product.TypeChoices.NUTS_SEEDS
        },
        {
            "name": 'Enchanted Elixir Soup', 
            "color": "wheat",
            "type": Product.TypeChoices.SALADS_BOWLS
        },
        {
            "name": 'Whimsical Waffle Tower', 
            "color": "brown",
            "type": Product.TypeChoices.DESSERTS
        },
        {
            "name": 'Dragonfire Tacos', 
            "color": "mixed",
            "type": Product.TypeChoices.VEGETABLES
        },
        {
            "name": 'Galactic Grilled Cheese', 
            "color": "amber",
            "type": Product.TypeChoices.BURGERS
        },
        {
            "name": 'Stardust Smoothie Bowl', 
            "color": "pink",
            "type": Product.TypeChoices.DESSERTS
        },
        {
            "name": "Fresh Juice",
            "color": "mixed",
            "type": Product.TypeChoices.JUICE
        }
    ]

    for product in products:
        price = random.uniform(20.0, 700.0)
        discount = random.randint(1, 99)
        Product.objects.get_or_create(
            **product,
            vendor=random.choice(vendors),
            price=price,
            discount=discount
                
        )
    
    products = Product.objects.all()

    reviews = [
        "The food here is absolutely amazing. I can't get enough of their signature dishes.",
        "Honestly, I expected more. The flavors were bland, and the service was slow.",
        "I clicked, but the taste didn't load. Disappointing.",
        "What a nice food, please make more of it!",
        "Awful product, the testing didn't match my needs."
    ]

    users = [
        {'username': 'ahmad'},
        {'username': 'zavier'},
        {'username': 'shafiq'},
        {'username': 'hadi'},
        {'username': 'salam'},
        {'username': 'omar'},
        {'username': 'amina'},
        {'username': 'sara'},
        {'username': 'tariq'},
        {'username': 'ibrahim'},
        {'username': 'rana'},
        {'username': 'khaled'},
        {'username': 'samira'},
        {'username': 'leila'},
        {'username': 'karim'},
        {'username': 'mansour'},
        {'username': 'rashid'},
        {'username': 'yusuf'},
        {'username': 'hamza'},
        {'username': 'amir'},
        {'username': 'layla'},
        {'username': 'hana'},
        {'username': 'tamer'},
        {'username': 'najwa'},
        {'username': 'jamil'},
        {'username': 'farida'},
        {'username': 'lina'},
        {'username': 'adil'},
        {'username': 'samih'},
        {'username': 'aziz'},
        {'username': 'hakim'},
    ]

    for user in users:
        new_user = User.objects.create(
            **user,
        )
        new_user.set_password('test')
        new_user.save()
        Profile.objects.create(user=new_user)

    profiles = Profile.objects.all()  

    for i in range(27):
        body = random.choice(reviews)
        product = random.choice(products)
        rating = random.randint(1, 5)
        Review.objects.get_or_create(
            body=body,
            product=product,
            rating=rating,
            owner=profiles[i]
        )

    
        