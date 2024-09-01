from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path('', views.index, name='home'),

    path('products/<str:handle>/', views.product_detail, name='product-detail'),
    path('products/<str:handle>/download/<int:pk>/', views.product_download, name="product-download"),

    path('cart/', views.cart, name="cart"),
    path('shop/', views.shop, name="shop"),
    path('categories/<str:category>/', views.category, name="category"),
    path('wishlist/', views.wishlist, name="wishlist"),
    
]