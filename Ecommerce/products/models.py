from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q, Sum
from django.db.models.functions import Lower

from datetime import datetime, timedelta

from .middleware import get_current_request
from . import utils as products_utils
from users.models import Profile
from vendors.models import Vendor


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



class Product(models.Model):
    name= models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.IntegerField(blank=True, null=True)
    vendor= models.ForeignKey(Vendor, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)
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
    def get_stars_percentage(self):
        count_all = self.get_total_reviews
        count_five = self.reviews.filter(rating=5).count()
        count_four = self.reviews.filter(rating=4).count()
        count_three = self.reviews.filter(rating=3).count()
        count_two = self.reviews.filter(rating=2).count()
        count_one = self.reviews.filter(rating=1).count()
        return {
            'five': products_utils.custom_round(count_five * 5 / count_all),
            'four': products_utils.custom_round(count_four * 5 / count_all),
            'three': products_utils.custom_round(count_three * 5 / count_all),
            'two': products_utils.custom_round(count_two * 5 / count_all),
            'one': products_utils.custom_round(count_one * 5 / count_all),
        }

    
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
    
    @property
    def added_to_cart(self):
        request = get_current_request()
        if request.user.is_anonymous:
            return False
        try:
            CartItem.objects.get(product__pk=self.pk, cart__owner=request.user.profile)
            return True
        except:
            return False
        
    @property
    def added_to_wishlist(self):
        request = get_current_request()
        if request.user.is_anonymous:
            return False
        try:
            WishlistItem.objects.get(product__pk=self.pk, wishlist__owner=request.user.profile)
            return True
        except:
            return False
    
    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={'handle': self.handle})
    
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
    created = models.DateField(auto_now_add=True)

    @property
    def like(self):
        pass

    def __str__(self):
        if not self.owner:
            return 'Anonymos'
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




class Cart(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    @property
    def shipping(self):
        return 0

    @property
    def subtotal(self):
        sum_items = self.items.aggregate(sum_items=Sum('subtotal'))['sum_items']
        return sum_items or 0

    @property
    def total(self):
        if self.coupon:
            return f'{(self.shipping + self.subtotal) * self.coupon.discount / 100:.2f}'
        return self.shipping + self.subtotal

    def __str__(self):
        return f"{self.owner.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.subtotal = float(self.quantity * self.product.price)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    class Meta:

        constraints = [
                models.UniqueConstraint(fields=['product', 'cart'], name='unique_product_cart')
            ]


class Invoice(models.Model):
    PROCESSING = 'Processing'
    SHIPPING = 'Shipping'
    DELIVERED = 'Delivered'
    delivery_choices = [
        (PROCESSING, 'Processing'),
        (SHIPPING, 'Shipping'),
        (DELIVERED, 'Delivered')
    ]

    name = models.CharField(max_length=30, null=True, blank=True)
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='invoices')
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    number_of_items = models.PositiveSmallIntegerField(null=True, blank=True)
    paid_status = models.BooleanField(default=True)
    delivery_status = models.CharField(max_length=20, choices=delivery_choices, default=PROCESSING)
    
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.client}"    

class Coupon(models.Model):
    name = models.CharField(max_length=10)
    life = models.PositiveIntegerField(default=10)
    discount = models.PositiveIntegerField(default=20, validators=[
        MinValueValidator(1), MaxValueValidator(99)
    ])

    created = models.DateField(auto_now_add=True)

    @property
    def check_validity(self):
        # Convert to string and then to date object
        datetime_obj = timezone.now() - timedelta(days=self.life)
        date_str = datetime_obj.strftime('%Y-%m-%d')
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        return self.created >=  date_obj

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner.user.username}"        

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'wishlist'], name='unique_product_wishlist')
        ]