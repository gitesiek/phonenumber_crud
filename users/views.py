from django.shortcuts import render, redirect


def login_page(request):
    return redirect('accounts/login')

def user_create(request):
    return render(request, 'usersViews/create.html')
def user_delete(request):
    return render(request, 'usersViews/delete.html')
def user_details(request):
    return render(request, 'usersViews/details.html')
def user_edit(request):
    return render(request, 'usersViews/edit.html')
def user_list(request):
    return render(request, 'usersViews/user_list.html')

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