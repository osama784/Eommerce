from django.contrib import admin
from django.utils.html import format_html

from cloudinary import CloudinaryImage

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
    readonly_fields = ['created', 'updated', 'display_image']

    def display_image(slef, obj, *args, **kwargs):
        if obj.image:
            cloudinary_id = str(obj.image)
            cloudinary_html = CloudinaryImage(cloudinary_id).image(width=500)
            return format_html(cloudinary_html)
        return 'no image for this product'
    
    display_image.short_description = 'Current Image'
    


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

