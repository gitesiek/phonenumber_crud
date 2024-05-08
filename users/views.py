from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from .models import Users

def login_page(request):
    return redirect('accounts/login')

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Użytkownik dodany pomyślnie.')
            return redirect(user_list)
    else:
        form = UserForm()
    return render(request, 'usersViews/create.html', {'form': form})

def user_delete(request):
    return render(request, 'usersViews/delete.html')
def user_details(request):
    return render(request, 'usersViews/details.html')
def user_edit(request):
    return render(request, 'usersViews/edit.html')
def user_list(request):
    users = Users.objects.all()
    return render(request, 'usersViews/user_list.html', {'users': users})

def group_create(request):
    return render(request, 'rolesViews/create.html')
def group_delete(request):
    return render(request, 'rolesViews/delete.html')
def group_details(request):
    return render(request, 'rolesViews/details.html')
def group_edit(request):
    return render(request, 'rolesViews/edit.html')
def group_list(request):
    return render(request, 'rolesViews/group_list.html')