from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.exceptions import PermissionDenied, NotFound
from django.shortcuts import get_object_or_404
from django.http import Http404


from .serializers import (
    ProductSerializer,
    ReviewSerializer,
    ReviewCreateSerializer,
    CartItemSerializer,
    CartItemUpdateSerializer,
    WishlistItemSerializer)

from products.models import (
    Product,
    CategoryChoices, 
    CartItem, 
    Cart, 
    Coupon, 
    Wishlist, 
    WishlistItem, 
    Invoice)


""" custom permissions """
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj, attr):
        if hasattr(obj, attr):
            owner = getattr(obj, attr)
            return owner == request.user.profile
        raise Exception('no attribute with the given name.')


""" 
Product views:
    - get the products (GET, get_products)
"""
@api_view(['GET'])
def get_products(request):
    categories = request.GET.getlist('categories') or None
    vendors = request.GET.getlist('vendors') or None
    price = request.GET.get('price') or None

    products = Product.objects.all()

    if categories:
        try:
            categories = [CategoryChoices(category) for category in categories]
            products = products.filter(category__in=categories)
        except:
            print("not valid category")    
    if vendors:
        try:
            products = products.filter(vendor__in=vendors)
        except:
            pass    
    if price:
        products = products.filter(price__lte=price)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


""" 
Review views:
    - get the reviews (GET, get_reviews)
    - create a review (POST, create_review)
"""
@api_view(['GET'])
def get_reviews(request, handle):
    product = get_object_or_404(Product, handle=handle)
    reviews = product.reviews.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, handle):
    print(request.POST)
    product = get_object_or_404(Product, handle=handle)
    owner = request.user.profile
    serializer = ReviewCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    review = serializer.save(product=product, owner=owner)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


""" 
(Cart, CartItem, Wishlist) views:
    - create cart item (POST, create_cart_item)
    - remove cart item (DELETE, remove_cart_item)
    - clear the cart (DELETE, clear_cart)
    - update a cart item quantity (PATCH, update_cart_item_quantity)
"""

@api_view(['POST'])
@permission_classes([IsAuthenticated & IsOwner])
def create_or_remove_cart_item(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    cart = Cart.objects.get(owner=request.user.profile)
    cartItem, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
    ) 
    
    if not created:
        if not IsOwner().has_object_permission(request, None, obj=cart, attr='owner'):
            raise PermissionDenied()
        cartItem.delete()
        return Response(status=status.HTTP_200_OK)
    serializer = CartItemSerializer(cartItem, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated & IsOwner])
def create_or_remove_wishlist_item(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    wishlist = Wishlist.objects.get(owner=request.user.profile)
    wishlistItem, created = WishlistItem.objects.get_or_create(
        wishlist=wishlist,
        product=product
    )

    if not created:
        if not IsOwner().has_object_permission(request, None, obj=wishlist, attr='owner'):
            raise PermissionDenied()
        wishlistItem.delete()
        return Response(status=status.HTTP_200_OK)    
    
    serializer = WishlistItemSerializer(wishlistItem, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated & IsOwner])
def clear_cart(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    if not IsOwner().has_object_permission(request, None, obj=cart, attr='owner'):
        raise PermissionDenied()
    
    cart.items.all().delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated & IsOwner])
def clear_Wishlist(request, pk):
    wishlist = get_object_or_404(Wishlist, pk=pk)
    if not IsOwner().has_object_permission(request, None, obj=wishlist, attr='owner'):
        raise PermissionDenied()
    
    wishlist.items.all().delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated & IsOwner])
def update_cart_item_quantity(request, pk):
    cartItem = get_object_or_404(CartItem, pk=pk)
    if not IsOwner().has_object_permission(request, None, obj=cartItem.cart, attr='owner'):
        raise PermissionDenied()
    
    serializer = CartItemUpdateSerializer(instance=cartItem, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    serializer = CartItemSerializer(serializer.instance, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
    

""" 
Coupon views:   
    - when coupon changes (GET, coupon_change)
    - when coupon applied (POST, coupon_apply) 

"""

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def coupon_change(request):
    coupon_value = request.GET.get('coupon')
    
    try: 
        coupon = get_object_or_404(Coupon, name=coupon_value)
    except Http404:
        detail = {
            'detail': 'invalid coupon!'
        }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)  
      
    if not coupon.check_validity:
        detail = {
            'detail': 'coupon has expired.'
        }
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)
    
    detail = {
        'detail': f'{coupon_value} is a valid coupon.'
    }
    return Response(detail, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def coupon_apply(request):
    cart = get_object_or_404(Cart, owner=request.user.profile)
    coupon_value = request.data.get('coupon')
    coupon = get_object_or_404(Coupon, name=coupon_value)
    cart.coupon = coupon
    cart.save()
    data = {
        'coupon': {
            'name': coupon_value,
            'discount': coupon.discount
        }
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_invoice(request):
    cart = request.user.profile.cart
    instance = Invoice.objects.create(
        client = request.user.profile,
        coupon = cart.coupon,
        total = cart.total,
        number_of_items = cart.items.all().count()
    )
    instance.name = f'INVOICE_NO_{instance.pk}'
    instance.save()
    cart.items.all().delete()
    return Response(status=status.HTTP_201_CREATED)
