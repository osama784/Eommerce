from django.db import models
from django.db.models import Count, Sum
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

from . import utils as vendors_utils

from users.models import Profile

class Vendor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to=vendors_utils.vendor_download ,blank=True, null=True)
    handle = models.CharField(max_length=200, null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def get_total_products_reviews(self):
        sum_reviews = self.products.annotate(num_reviews=Count('reviews')).aggregate(sum_reviews=Sum('num_reviews'))
        return sum_reviews['sum_reviews']
    
    @property
    def get_ship_rating_percentage(self):
        sum_ship_rating = self.ratings.aggregate(sum_ship_rating=Sum('ship_rating'))['sum_ship_rating']
        return int(sum_ship_rating * 100 / (5 * self.ratings.count()))
    
    @property
    def get_chat_rating_percentage(self):
        sum_chat_rating = self.ratings.aggregate(sum_chat_rating=Sum('chat_rating'))['sum_chat_rating']
        return int(sum_chat_rating * 100 / (5 * self.ratings.count()))
    
    @property
    def get_products_quality_rating_percentage(self):
        products_quality_rating = self.ratings.aggregate(sum_products_quality_rating=Sum('products_quality_rating'))['sum_products_quality_rating']
        return int(products_quality_rating * 100 / (5 * self.ratings.count()))
    
    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs) -> None:
        if self.name:
            self.handle = self.name.lower().replace(" ", "-")
        return super().save(*args, **kwargs)
    


class Rating(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='vendor_ratings')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='ratings')
    
    ship_rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    chat_rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    products_quality_rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])

    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner.user.username }: {self.vendor.name}'
    

    