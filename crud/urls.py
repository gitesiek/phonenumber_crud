from django.urls import path, include
from .views import clinic_list, login_page

urlpatterns = [
    path('', clinic_list, name='clinic_list'),
    path('login', login_page, name='clinic_list'),
    path("accounts/", include("django.contrib.auth.urls")),
]
