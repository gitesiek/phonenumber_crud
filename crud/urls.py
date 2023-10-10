from django.urls import path, include
from .views import clinic_list, login_page, crud_page

urlpatterns = [
    path('', clinic_list, name='clinic_list'),
    path('login', login_page, name='login_page'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('crud_page', crud_page, name='crud_page')
]
