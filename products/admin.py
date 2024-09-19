from django.contrib import admin
from products.models import Product, Review, ProductAttachment, Cart, CartItem, Invoice, InvoiceItem, Coupon


class ProductAttachmentInline(admin.StackedInline):
    model = ProductAttachment
    max_num = 5
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAttachmentInline]
    list_display = ['name', 'price', 'category', 'vendor']
    readonly_fields = ['created', 'updated']
    


class CartItemInline(admin.StackedInline):
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

class InvoiceItemInline(admin.StackedInline):
    model = InvoiceItem

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]
    


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttachment)
admin.site.register(Review)
admin.site.register(Cart, CartAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Coupon)

