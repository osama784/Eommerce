from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


from .models import Vendor
from .forms import RatingForm

def vendor(request, handle):
    return render(request, 'vendor.html')

def vendor_list(request):
    return render(request, 'vendors_list.html')


@require_POST
@login_required
def vendor_rating(request, handle):
    vendor = get_object_or_404(Vendor, handle=handle)
    
    data = {}
    for key in request.POST:
        if key == 'csrfmiddlewaretoken':
            continue
        data[key] = int(request.POST[key])
    
    form = RatingForm(data)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.owner = request.user.profile
        obj.vendor = vendor
        obj.save()
    
        return redirect('products:home')
    # print(form.)
    raise ValidationError('something went wrong.')

