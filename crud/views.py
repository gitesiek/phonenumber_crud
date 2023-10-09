from django.shortcuts import render
from .models import Clinic

def clinic_list(request):
    clinics = Clinic.objects.all()
    return render(request, 'home.html', {'clinics': clinics})
