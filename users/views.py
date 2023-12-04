from django.shortcuts import render, redirect


def login_page(request):
    return redirect('accounts/login')
