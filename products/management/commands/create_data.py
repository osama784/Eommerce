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
            "type": Product.CategoryChoices.DESSERTS,
        },
        {
            "name": 'Spatchcock BBQ Chicken', 
            "type": Product.CategoryChoices.MEAT_BEEF
        },
        {
            "name": 'Home-made BBQ Grilled Chicken', 
            "type": Product.CategoryChoices.MEAT_BEEF
        },
        {
            "name": 'Double Bief Fried Chicken Bacon', 
            "type": Product.CategoryChoices.BURGERS
        },
        {
            "name": 'Zesty Zucchini Zoodles', 
            "type": Product.CategoryChoices.SALADS_BOWLS
        },
        {
            "name": 'Savory Seaweed Sushi Rolls', 
            "type": Product.CategoryChoices.SUSHI
        },
        {
            "name": 'Mystical Mushroom Medley', 
            "type": Product.CategoryChoices.NUTS_SEEDS
        },
        {
            "name": 'Enchanted Elixir Soup', 
            "type": Product.CategoryChoices.SALADS_BOWLS
        },
        {
            "name": 'Whimsical Waffle Tower', 
            "type": Product.CategoryChoices.DESSERTS
        },
        {
            "name": 'Dragonfire Tacos', 
            "type": Product.CategoryChoices.VEGETABLES
        },
        {
            "name": 'Galactic Grilled Cheese', 
            "type": Product.CategoryChoices.BURGERS
        },
        {
            "name": 'Stardust Smoothie Bowl', 
            "type": Product.CategoryChoices.DESSERTS
        },
        {
            "name": "Fresh Juice",
            "type": Product.CategoryChoices.JUICE
        }
    ]

    for product in products:
        price = random.uniform(20.0, 700.0)
        discount = random.randint(1, 99)
        # image_path = f'products/{products['name'].lower().replace()}'
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

    
        