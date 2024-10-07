from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class ProfileForm(forms.Form):
    image = forms.ImageField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()


class UserForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(max_length=50)   

    def save(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = User.objects.create(
            username=username,
            email=email,
            password=password,
            first_name=username
        )

        return user
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)        
    password = forms.CharField(max_length=50)        

    def save(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if not user:
            return None
        return user
    
    
