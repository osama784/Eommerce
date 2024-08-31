from django.shortcuts import render


def vendor(request, vendor):
    return render(request, 'vendor.html')

def vendor_list(request):
    return render(request, 'vendors_list.html')

