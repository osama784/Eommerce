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

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def get_total_products_reviews(self):
        sum_reviews = self.products.annotate(num_reviews=Count('reviews')).aggregate(sum_reviews=Sum('num_reviews'))
        return sum_reviews['sum_reviews']
    
    def __str__(self):
        return self.name
    


class Rating(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    
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
    
