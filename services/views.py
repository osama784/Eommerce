from django.shortcuts import render


def about_us(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')

def purchase_guide(request):
    return render(request, 'purchase-guide.html')

def terms_of_service(request):
    return render(request, 'terms-of-service.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def dashboard(request):
    return render(request, 'dashboard.html')
