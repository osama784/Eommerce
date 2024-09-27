from django import forms

from .models import Review, CartItem

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'rating']

class CartItemUpdateForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']
        