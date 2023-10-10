from django.shortcuts import render, redirect
from .models import Clinic

def clinic_list(request):
    clinics = Clinic.objects.all()
    return render(request, 'home.html', {'clinics': clinics})

def login_page(request):
    return redirect('accounts/login')
