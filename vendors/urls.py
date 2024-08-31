from django.urls import path


from . import views


app_name = "vendors"

urlpatterns = [
    path('<str:vendor>/', views.vendor, name='vendor'),
    path('', views.vendor_list, name="vendor-list"),
]