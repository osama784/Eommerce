from django.shortcuts import render
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db import connection

from pprint import pprint

from products.models import Product, Order, Review, Vendor



def index(request):
    products = Product.objects.select_related('vendor').prefetch_related('reviews').annotate(reviews_count=Count('reviews'))

    context = {'products': products}
    return render(request, 'index.html', context=context)


def product(request):
    return render(request, 'product.html')

@login_required
def cart(request):
    orders = Order.objects.filter(owner=request.user.profile).select_related('product', 'owner')
    context = {'orders': orders}
    return render(request, 'cart.html', context=context)


def shop(request):
    return render(request, 'shop.html')

def vendor(request):
    return render(request, 'vendor.html')

def about_us(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')

def purchase_guide(request):
    return render(request, 'purchase-guide.html')

def terms_of_service(request):
    return render(request, 'terms-of-service.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def user_info(request):
    return render(request, 'account.html')