from django.contrib import admin
from products.models import (
    Product, 
    Review, 
    ProductAttachment, 
    Cart, 
    CartItem, 
    Wishlist,
    WishlistItem,
    Invoice, 
    Coupon)


class ProductAttachmentInline(admin.StackedInline):
    model = ProductAttachment
    max_num = 4
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAttachmentInline]
    list_display = ['name', 'price', 'category', 'vendor']
    readonly_fields = ['created', 'updated']
    


class CartItemInline(admin.StackedInline):
    model = CartItem
    readonly_fields = ['subtotal']
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

class WishlitItemInline(admin.StackedInline):
    model = WishlistItem
    extra = 0    

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    inlines = [WishlitItemInline]
    
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    readonly_fields = ['created']


admin.site.register(Review)
admin.site.register(Invoice)

