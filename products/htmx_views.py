from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_http_methods

from .models import Product, CartItem, Cart
from .forms import ReviewForm



@login_required
@require_http_methods(['POST'])
def create_review(request, handle):
    product = get_object_or_404(Product, handle=handle)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.owner = request.user.profile
        review.save()
        return render(request, 'htmx_partials/successfull-review.html')
    return render(request, 'htmx_partials/bad-review.html')


@login_required
@require_http_methods(['DELETE'])
def remove_cart_item(request, pk):
    item = get_object_or_404(CartItem, pk=pk)
    if item.cart.owner != request.user.profile:
        return HttpResponseForbidden()
    item.delete()

    items = CartItem.objects.filter(owner=request.user.profile)

    if not items.exists():
        return render(request, 'htmx_partials/cart-cleared.html')

    context= {'items': items}

    return render(request, 'partials/cart-table.html', context=context)


@login_required
@require_http_methods(['DELETE'])
def clear_cart(request, pk):
    cart = get_object_or_404(Cart, pk=pk)

    if cart.owner != request.user.profile:
        return HttpResponseForbidden()
    
    items = cart.items
    items.delete()

    return render(request, 'htmx_partials/cart-cleared.html')

    

    