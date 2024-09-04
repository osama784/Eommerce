from django.forms import ModelForm

from .models import Rating


class RatingForm(ModelForm):

    class Meta:
        model = Rating
        fields = ['ship_rating', 'chat_rating', 'products_quality_rating']