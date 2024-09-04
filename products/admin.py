from django.contrib import admin
from products.models import Product, Order, Review, ProductAttachment


class ProductAttachmentInline(admin.StackedInline):
    model = ProductAttachment
    max_num = 5
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAttachmentInline]
    list_display = ['name', 'price', 'category', 'vendor']
    readonly_fields = ['created', 'updated']
    

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttachment)
admin.site.register(Order)
admin.site.register(Review)

