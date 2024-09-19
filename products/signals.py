from django.db.models.signals import post_save
from .models import Cart, Profile

def product_delete_file():
    pass

def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(owner=instance)

post_save.connect(create_cart, sender=Profile)