from django import forms
from .models import Contacts


class ContactsForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa')
    department = forms.CharField(label='Nazwa2')
    office = forms.CharField(label='Nr wew')
    phone = forms.CharField(label='Nr tel')

    class Meta:
        model = Contacts
        fields = ['name', 'department', 'office', 'phone']
