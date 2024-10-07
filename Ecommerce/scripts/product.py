from products.models import Product, Review
from users.models import Profile
from django.db.models import Sum, F, Count
from django.db.models.functions import Coalesce

from django.db import connection
from pprint import pprint

def run():
    # types = products.values('type').annotate(type_count=Count("type")).order_by('-type_count')[:4]
    # reivews_count = Product.objects.values('name').annotate(reviews_count=Count('reviews')).order_by('-reviews_count')

    # pprint(reivews_count)
    # for product in reivews_count:
    #     print(product['reviews_count'])    


    products = Product.objects.values('name', 'vendor__name').annotate(reviews_count=Count('reviews'), stars=Sum('reviews__rating')).order_by("-reviews_count")
    print(products)
    # for product in products:
    #     print(product['vendor__name'], product['reviews_count'])

    pprint(connection.queries)