from django.contrib import admin

from .models import Vendor, Rating

class VendorAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'image']
    readonly_fields = ['created', 'updated']


class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ['created']

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Rating)
