from django.contrib import admin
from products.models import Product, Vendor, Order, Review



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'vendor']
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Vendor)
admin.site.register(Order)
admin.site.register(Review)

