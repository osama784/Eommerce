from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import ProductSerializer, ReviewSerializer

from products.models import Product, CategoryChoices

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



@api_view(['GET'])
def get_reviews(request, handle):
    product = get_object_or_404(Product, handle=handle)
    reviews = product.reviews.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

    
