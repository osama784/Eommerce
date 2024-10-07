from rest_framework import serializers
from django.urls import reverse
from django.shortcuts import get_object_or_404

from products.models import Product, Review, CartItem, WishlistItem

class ProductSerializer(serializers.ModelSerializer):
    absolute_url = serializers.URLField(source='get_absolute_url')
    download_url = serializers.URLField(source='get_download_url')
    total_reviews = serializers.IntegerField(source='get_total_reviews')
    new_price= serializers.DecimalField(source='get_new_price', max_digits=8, decimal_places=2)
    display_image = serializers.ImageField(source='get_display_image')

    class Meta:
        model = Product
        fields = "__all__"


   
    # def get_total_reviews(self, obj):
    #     return obj.reviews.count()
    
    # def get_new_price(self, obj) -> int:
    #     if obj.discount:
    #         return f'{obj.price * obj.discount / 100:.2f}'
    #     return obj.price
    
    # def get_display_image(self, obj):
    #     if obj.image:
    #         return obj.image.url
        
    #     return '/media/products/default_product.jpg'


"""Review serializers"""
class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['body', 'owner']

    def get_owner(self, obj):
        return obj.owner.user.username


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['body', 'rating']



"""CartItem serializers"""
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']

"""Wishlist serializers"""        
class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = '__all__'