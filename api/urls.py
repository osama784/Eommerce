from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('get-products/', views.get_products, name='get-products'),

    path('get-reviews/<str:handle>/', views.get_reviews, name='get-reviews'),
    path('create-review/<str:handle>/', views.create_review, name='create-review'),

    path('create-cart-item/<int:product_pk>/', views.create_cart_item, name='create-cart-item'),
    path('remove-cart-item/<int:pk>/', views.remove_cart_item, name='remove-cart-item'),
    path('clear-cart/<int:pk>/', views.clear_cart, name='clear-cart'),
    path('update-cart-item-quantity/<int:pk>/', views.update_cart_item_quantity, name="update-cart-item-quantity"),

]