from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ContactMessageForm
from .models import ContactMessage
from products.models import Invoice

def about_us(request):
    return render(request, 'about-us.html')

login_required
def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)       
            instance.owner = request.user.profile
            instance.save()
    num_messages = ContactMessage.objects.filter(owner=request.user.profile).count()   
    context = {'num_messages': num_messages}     
    return render(request, 'contact.html', context)

def purchase_guide(request):
    return render(request, 'purchase-guide.html')

def terms_of_service(request):
    return render(request, 'terms-of-service.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

@login_required()
def dashboard(request):
    invoices = Invoice.objects.filter(client=request.user.profile)
    context={'invoices': invoices}
    return render(request, 'dashboard.html', context)
