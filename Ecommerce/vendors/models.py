from django.db import models
from django.db.models import Count, Sum
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

from cloudinary.models import CloudinaryField
from math import ceil

from . import utils as vendors_utils

from users.models import Profile

class Vendor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    image = CloudinaryField(
        'image',
        public_id_prefix=vendors_utils.get_vendor_prefix_id,
        display_name=vendors_utils.get_vendor_display_name,
        blank=True,
        null=True)
    handle = models.CharField(max_length=200, null=True, blank=True)
    opened = models.DateField(null=True, blank=True)
    social_facebook = models.URLField(blank=True, null=True)
    social_twitter = models.URLField(blank=True, null=True)
    social_Instegram = models.URLField(blank=True, null=True)
    social_youtube = models.URLField(blank=True, null=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def get_stars_number(self):
        sum_ratings_columns = self.ratings.aggregate(
            sum_ship_rating=Sum('ship_rating'),
            sum_chat_rating=Sum('chat_rating'),
            sum_products_quality_rating=Sum('products_quality_rating')
        )
        sum_ratings = sum_ratings_columns['sum_ship_rating'] + sum_ratings_columns['sum_chat_rating'] + sum_ratings_columns['sum_products_quality_rating']
        return ceil(sum_ratings / (self.ratings.count() * 3))
    
    @property
    def get_ship_rating_percentage(self):
        sum_ship_rating = self.ratings.aggregate(sum_ship_rating=Sum('ship_rating'))['sum_ship_rating']
        return ceil(sum_ship_rating * 100 / (5 * self.ratings.count()))
    
    @property
    def get_chat_rating_percentage(self):
        sum_chat_rating = self.ratings.aggregate(sum_chat_rating=Sum('chat_rating'))['sum_chat_rating']
        return ceil(sum_chat_rating * 100 / (5 * self.ratings.count()))
    
    @property
    def get_products_quality_rating_percentage(self):
        products_quality_rating = self.ratings.aggregate(sum_products_quality_rating=Sum('products_quality_rating'))['sum_products_quality_rating']
        return ceil(products_quality_rating * 100 / (5 * self.ratings.count()))
    

    def get_absolute_url(self):
        return reverse('vendors:vendor', kwargs={'handle': self.handle})
    
    

    def __str__(self):
        return self.name or 'Vendor'
    
    def save(self, *args, **kwargs) -> None:
        if self.name:
            self.handle = slugify(self.name)
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
    

    