from django.contrib import admin
from products.models import Product, Review, ProductAttachment, Cart, CartItem, Invoice, InvoiceItem, Coupon


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

class InvoiceItemInline(admin.StackedInline):
    model = InvoiceItem
    extra = 0

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]
    
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    readonly_fields = ['created']


admin.site.register(Review)

