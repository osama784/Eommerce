from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('purchase-guide/', views.purchase_guide, name='purchase-guide'),
    path('terms-of-service/', views.terms_of_service, name='terms-of-service'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('about-us/', views.about_us, name='about-us'),
    path('dashboard/', views.dashboard, name='dashboard'),
]