from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db import connection

from pprint import pprint
import mimetypes

from .models import Product, ProductAttachment, Order, Review, Vendor


def index(request):
    products = Product.objects.select_related('vendor').prefetch_related('reviews')
    print(products.first().image)
    context = {'products': products}
    return render(request, 'index.html', context=context)


def product_detail(request, handle):
    product = get_object_or_404(Product, handle=handle)
    products = Product.objects.all()
    context = {'product': product, 'products': products}
    return render(request, 'product.html', context=context)


def attachment_download(request, handle, pk):
    attachment = get_object_or_404(ProductAttachment, product__handle=handle, pk=pk)
    image = attachment.image.open(mode='rb')
    filename = attachment.image.name

    response = FileResponse(image)
    response['Content-Type'] = 'application/octet-stream'
    response["Content-Disposition"] = f'attachment;filename={filename}'
    return response

def product_download(request, handle):
    product = get_object_or_404(Product, handle=handle)
    image = product.image    
    filename = image.name

    response = FileResponse(image)
    response['Content-Type'] = 'application/octet-stream'
    response["Content-Disposition"] = f'attachment;filename={filename}'
    return response


@login_required
def cart(request):
    orders = Order.objects.filter(owner=request.user.profile).select_related('product', 'owner')
    context = {'orders': orders}
    return render(request, 'cart.html', context=context)


def shop(request):
    return render(request, 'shop.html')

def category(request, category):
    return render(request, 'category.html')

def wishlist(request):
    return render(request, 'wishlist.html')


