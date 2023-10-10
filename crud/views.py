from django.shortcuts import render, redirect
from .models import Clinic
from django.contrib.auth.decorators import login_required


def clinic_list(request):
    clinics = Clinic.objects.all()
    return render(request, 'home.html', {'clinics': clinics})

def login_page(request):
    return redirect('accounts/login')

@login_required
def crud_page(request):
    return render(request, 'home.html')