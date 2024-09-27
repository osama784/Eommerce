from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .serializers import (
    ProductSerializer,
    ReviewSerializer,
    ReviewCreateSerializer,
    CartItemSerializer,
    CartItemUpdateSerializer)

from products.models import Product, CategoryChoices, CartItem, Cart


""" custom permission """
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.cart.owner == request.user.profile


""" Product views """
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


""" Review views """
@api_view(['GET'])
def get_reviews(request, handle):
    product = get_object_or_404(Product, handle=handle)
    reviews = product.reviews.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, handle):
    product = get_object_or_404(Product, handle=handle)
    owner = request.user.profile
    serializer = ReviewCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    review = serializer.save(product=product, owner=owner)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


""" (Cart, CartItem) views """

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_cart_item(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    cart = Cart.objects.get(owner=1)
    cartItem = CartItem.objects.create(
        cart=cart,
        product=product,
        quantity=1
    ) 
    serializer = CartItemSerializer(cartItem, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated & IsOwner])
def remove_cart_item(request, pk):    
    cartItem = get_object_or_404(CartItem, pk=pk)

    if not IsOwner().has_object_permission(request, None, obj=cartItem):
        raise PermissionDenied()
    
    cartItem.delete()

    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated & IsOwner])
def clear_cart(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    if cart.owner != request.user.profile:
        raise PermissionDenied()
    
    cart.items.all().delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated & IsOwner])
def update_cart_item_quantity(request, pk):
    print(request.data)
    cartItem = get_object_or_404(CartItem, pk=pk)
    if not IsOwner().has_object_permission(request, None, obj=cartItem):
        raise PermissionDenied()
    
    serializer = CartItemUpdateSerializer(instance=cartItem, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    serializer = CartItemSerializer(serializer.instance, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
    


