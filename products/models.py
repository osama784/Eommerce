from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.exceptions import ValidationError

from . import utils as products_utils
from users.models import Profile
from vendors.models import Vendor



class Product(models.Model):
    class CategoryChoices(models.TextChoices):
        ORGANIC = 'OR', 'organic'
        VEGETABLES = 'VG', 'vegetables'
        Plant_Based_Proteins = 'PP', 'plant-based protiens'
        SEAFOOD = 'SF', 'seafood'
        HERBS_SPICES = 'HS', 'herbs & spices'
        NUTS_SEEDS = 'NS', 'nuts & seeds'
        JUICE = 'JC', 'juice'
        SALADS_BOWLS = 'SB', 'salads & bowls'
        DESSERTS = 'DS', 'desserts'
        MEAT_BEEF = 'MB', 'meats & beefs'
        BURGERS = 'BG', 'burgers'
        SUSHI = 'SH', 'sushis'


    name= models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.IntegerField(blank=True, null=True)
    vendor= models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.IntegerField(default=1)
    category = models.CharField(max_length=2, choices=CategoryChoices.choices)
    handle = models.CharField(max_length=200, blank=True, null=True)
    life = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to=products_utils.product_image_download, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def get_total_reviews(self):
        return self.reviews.count()
    
    @property
    def get_new_price(self) -> int:
        if self.discount:
            return f'{self.price * self.discount / 100:.2f}'
        return self.price
    
    @property
    def get_display_image(self):
        if self.image:
            return self.image.url
        
        return '/media/products/default_product.jpg'
    
    def get_absolute_url(self):
        return reverse(f"products:product-detail", kwargs={'handle': self.handle})
    
    def get_download_url(self):
        return reverse("products:product-download", kwargs={'handle': self.handle})
    
    @property
    def get_attachments(self):
        attachments = ProductAttachment.objects.filter(product=self)
        return attachments or None

    def __str__(self):
        return f'{self.stock} x {self.name}'
    
    def save(self, *args, **kwargs) -> None:
        if self.name:
            self.handle = self.name.lower().replace(" ", "-")
        return super().save(*args, **kwargs)
    
    
    class Meta:
        ordering = ['stock']
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name="unique_name"
            ),
            models.CheckConstraint(
                check=Q(discount__gte=1, discount__lte=99),
                name="check_discount"
            )
        ]
      

class ProductAttachment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attachments')
    image = models.ImageField(upload_to=products_utils.product_attachment_download)        

    def get_download_url(self):
        return reverse('products:attachment-download', kwargs={'handle': self.product.handle, 'pk': self.pk})
    
class Review(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    body = models.TextField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    created = models.DateField(default=timezone.now)

    @property
    def like(self):
        pass

    def __str__(self):
        if not self.owner:
            return 'meow'
        if len(self.body) > 50:
            return f'{self.owner.user.username} : {self.body[:50]}...'        
        return f'{self.owner.user.username} : {self.body[:50]}'

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=['owner', 'product'],
                name="review_once"
            )
        ]


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    entries = models.BigIntegerField(default=0)


    def __str__(self):
        return f'{self.owner.user.username} : {self.quantity} x {self.product.name}'
 

class Like_DisLike(models.Model):
    class TypeChoices(models.TextChoices):
        LIKE = 'LK', 'like'
        DISLIKE = 'DK', 'dislike'
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TypeChoices.choices)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        constraints = [
            models.UniqueConstraint('owner', name="like_dislike_once")
        ]
 

class Invoice(models.Model):
    class StatusChoices(models.IntegerChoices):
        PROCESSING = 1
        DELIVERED  = 2
        SHIPPED = 3
        CANCELED = 4

    name = models.CharField(default='INVOICE', max_length=50)
    total = models.IntegerField()
    paid_status = models.BooleanField(default=False)
    status = models.IntegerField(choices=StatusChoices.choices)
    products = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
