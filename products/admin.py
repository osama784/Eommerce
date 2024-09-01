from django.contrib import admin
from products.models import Product, Vendor, Order, Review, ProductAttachment


class ProductAttachmentInline(admin.StackedInline):
    model = ProductAttachment
    max_num = 5
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAttachmentInline]
    list_display = ['name', 'price', 'category', 'vendor']
    

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttachment)
admin.site.register(Vendor)
admin.site.register(Order)
admin.site.register(Review)

