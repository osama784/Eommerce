from django.urls import path


from . import views


app_name = "vendors"

urlpatterns = [
    path('', views.vendor_list, name="vendor-list"),
    path('<str:handle>/', views.vendor, name='vendor'),

    path('<str:handle>/rating', views.vendor_rating, name='vendor-rating')
]