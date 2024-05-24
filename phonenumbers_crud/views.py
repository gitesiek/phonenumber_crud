from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacts
from django.contrib.auth.decorators import login_required
from .forms import ContactsForm
from django.contrib import messages


def clinic_list(request):
    clinics = Contacts.objects.all().order_by('jd_organizcyjnej').values()
    return render(request, 'crud/phoneViews/phone_list.html', {'clinics': clinics})


@login_required
def crud_page(request):
    return render(request, 'crud/crud_page.html')


@login_required
def add_clinic(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Klinika dodana pomyślnie.')
            return redirect(edit_clinic)
    else:
        form = ContactsForm()
    return render(request, 'crud/phoneViews/create.html', {'form': form})


@login_required
def edit_clinic(request):
    clinics = Contacts.objects.all().order_by('jd_organizcyjnej').values()
    return render(request, 'crud/edit_clinic.html', {'clinics': clinics})


@login_required
def edit(request, clinic_id):
    clinic = get_object_or_404(Contacts, pk=clinic_id)
    if request.method == 'POST':
        form = ContactsForm(request.POST, instance=clinic)
        if form.is_valid():
            form.save()
            messages.success(request, 'Klinika edytowana pomyślnie.')
            return redirect('edit_clinic')
    else:
        form = ContactsForm(instance=clinic)
    return render(request, 'crud/phoneViews/edit.html', {'form': form})


@login_required
def delete_clinic(request, clinic_id):
    clinic = get_object_or_404(Contacts, pk=clinic_id)
    if request.method == 'POST':
        clinic.delete()
        messages.success(request, 'Klinika usunięta pomyślnie.')
        return redirect('edit_clinic')
    return render(request, 'crud/phoneViews/delete.html', {'clinic': clinic})

