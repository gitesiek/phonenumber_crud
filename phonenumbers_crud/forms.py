from django import forms
from .models import Contacts


class ContactsForm(forms.ModelForm):
    jd_organizcyjnej = forms.CharField(label='Nazwa')
    lokalizacja = forms.CharField(label='Nazwa2')
    num_wew = forms.CharField(label='Nr wew')
    num_tel = forms.CharField(label='Nr tel')

    class Meta:
        model = Contacts
        fields = ['jd_organizcyjnej', 'lokalizacja', 'num_wew', 'num_tel']
