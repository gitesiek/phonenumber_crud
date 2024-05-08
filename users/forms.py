from django import forms
from .models import Users


class UserForm(forms.ModelForm):
    name = forms.CharField(label='Imie')
    surname = forms.CharField(label='Nazwisko')
    email = forms.CharField(label='Email')
    department = forms.CharField(label='Jednostka')
    active = forms.BooleanField(label='Aktywny')

    class Meta:
        model = Users
        fields = ['name', 'surname', 'email', 'department', 'active']
