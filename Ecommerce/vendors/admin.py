from django.contrib import admin

from .models import Vendor, Rating

class VendorAdmin(admin.ModelAdmin):
    list_display = [ 'name']
    readonly_fields = ['created', 'updated']


# class RatingAdmin(admin.ModelAdmin):
#     readonly_fields = ['created']

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Rating)
