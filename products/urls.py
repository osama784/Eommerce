from django.urls import path

from . import views
from . import htmx_views

app_name = "products"

urlpatterns = [
    path('', views.index, name='home'),

    path('products/<str:handle>/', views.product_detail, name='product-detail'),
    path('products/<str:handle>/download/', views.product_download, name="product-download"),
    path('products/<str:handle>/attachments/download/<int:pk>', views.attachment_download, name="attachment-download"),

    path('cart/', views.cart, name="cart"),
    path('shop/', views.shop, name="shop"),

    path('categories/', views.categories_list, name='categories-list'),
    path('categories/<str:category>/', views.category, name="category"),


    path('wishlist/', views.wishlist, name="wishlist"),
    
]

htmx_urlpatterns = [
    path('create-review/<str:handle>', htmx_views.create_review, name='create-review'),
    path('remove-cart-item/<int:pk>', htmx_views.remove_cart_item, name='remove-cart-item'),
    path('clear-cart/<int:pk>', htmx_views.clear_cart, name='clear-cart'),
]

urlpatterns += htmx_urlpatterns