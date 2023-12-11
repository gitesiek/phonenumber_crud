from django import forms
from .models import FoodPhoto


class FoodPhotoForm(forms.ModelForm):
    class Meta:
        model = FoodPhoto
        fields = ['image', 'type', 'digest']
