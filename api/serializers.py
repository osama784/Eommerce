from rest_framework import serializers
from django.urls import reverse
from django.shortcuts import get_object_or_404

from products.models import Product, Review

class ProductSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()
    download_url = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    new_price= serializers.SerializerMethodField()
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"


    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.buil_absolute_uri(obj.get_absolute_url)
    
    def get_download_url(self, obj):
        request = self.context.get('request')
        return request.buil_absolute_uri(obj.get_download_url)
    
    def get_total_reviews(self, obj):
        return obj.reviews.count()
    
    def get_new_price(self, obj) -> int:
        if obj.discount:
            return f'{obj.price * obj.discount / 100:.2f}'
        return obj.price
    
    def get_display_image(self, obj):
        if obj.image:
            return obj.image.url
        
        return '/media/products/default_product.jpg'



class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['body', 'owner']

    def get_owner(self, obj):
        return obj.owner.user.username
