from django.shortcuts import render, redirect, get_object_or_404
from .models import Clinic
from django.contrib.auth.decorators import login_required
from .forms import ClinicForm
from django.contrib import messages


def clinic_list(request):
    clinics = Clinic.objects.all().order_by('name').values()
    return render(request, 'crud/phoneViews/phone_list.html', {'clinics': clinics})


@login_required
def crud_page(request):
    return render(request, 'crud/crud_page.html')


@login_required
def add_clinic(request):
    if request.method == 'POST':
        form = ClinicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Klinika dodana pomyślnie.')
            return redirect(edit_clinic)
    else:
        form = ClinicForm()
    return render(request, 'crud/phoneViews/create.html', {'form': form})


@login_required
def edit_clinic(request):
    clinics = Clinic.objects.all().order_by('name').values()
    return render(request, 'crud/edit_clinic.html', {'clinics': clinics})


@login_required
def edit(request, clinic_id):
    clinic = get_object_or_404(Clinic, pk=clinic_id)
    if request.method == 'POST':
        form = ClinicForm(request.POST, instance=clinic)
        if form.is_valid():
            form.save()
            messages.success(request, 'Klinika edytowana pomyślnie.')
            return redirect('edit_clinic')
    else:
        form = ClinicForm(instance=clinic)
    return render(request, 'crud/phoneViews/edit.html', {'form': form})


@login_required
def delete_clinic(request, clinic_id):
    clinic = get_object_or_404(Clinic, pk=clinic_id)
    if request.method == 'POST':
        clinic.delete()
        messages.success(request, 'Klinika usunięta pomyślnie.')
        return redirect('edit_clinic')
    return render(request, 'crud/phoneViews/delete.html', {'clinic': clinic})
