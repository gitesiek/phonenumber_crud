from django import forms
from .models import Clinic

class ClinicForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa')
    department = forms.CharField(label='Nazwa2')
    office = forms.CharField(label='Nr wew')
    phone = forms.CharField(label='Nr tel')

    class Meta:
        model = Clinic
        fields = ['name', 'department', 'office', 'phone']