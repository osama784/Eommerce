from django.db.models.signals import post_save, pre_save

from .models import Cart, Wishlist
from users.models import Profile

def create_cart_wislist(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(owner=instance)
    if created:
        Wishlist.objects.create(owner=instance)


post_save.connect(create_cart_wislist, sender=Profile)
