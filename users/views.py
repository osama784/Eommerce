from django.shortcuts import render



def login_user(request):
    if request.method == 'POST':
        pass
    return render(request, 'login.html')

def register_user(request):
    return render(request, 'sign-up.html')