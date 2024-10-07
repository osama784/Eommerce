from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('get-products/', views.get_products, name='get-products'),

    path('get-reviews/<str:handle>/', views.get_reviews, name='get-reviews'),
    path('create-review/<str:handle>/', views.create_review, name='create-review'),

    path('create-or-remove-cart-item/<int:product_pk>/', views.create_or_remove_cart_item, name='create-or-remove-cart-item'),
    path('clear-cart/<int:pk>/', views.clear_cart, name='clear-cart'),
    path('update-cart-item-quantity/<int:pk>/', views.update_cart_item_quantity, name="update-cart-item-quantity"),

    path('create-or-remove-wishlist-item/<int:product_pk>/', views.create_or_remove_wishlist_item, name="create-or-remove-wishlist-item"),
    path('clear-wishlist/<int:pk>/', views.clear_Wishlist, name='clear-wishlist'),

    path('coupon-change/', views.coupon_change, name="coupon-change"),
    path('coupon-apply/', views.coupon_apply, name="coupon-apply"),

    path('create-invoice/', views.create_invoice, name='create-invoice')

]