from django.core.management.base import BaseCommand
from products.models import Product, Vendor, Review
from users.models import Profile

import random


class Command(BaseCommand):
    help = "Creating data every time"

    products = Product.objects.all()

    reviews = [
        "The food here is absolutely amazing. I can't get enough of their signature dishes.",
        "Honestly, I expected more. The flavors were bland, and the service was slow.",
        "I clicked, but the taste didn't load. Disappointing.",
        "What a nice food, please make more of it!",
        "Awful product, the testing didn't match my needs."
    ]

    

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