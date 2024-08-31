from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path('', views.index, name='home'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name="cart"),
    path('shop/', views.shop, name="shop"),
    path('categories/<str:category>/', views.category, name="category"),
    path('wishlist/', views.wishlist, name="wishlist"),
    
]