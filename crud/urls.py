from django.urls import path, include
from .views import clinic_list, login_page, crud_page, add_clinic, edit_clinic, edit, delete_clinic

urlpatterns = [
    path('', clinic_list, name='clinic_list'),
    path('login', login_page, name='login_page'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('crud_page', crud_page, name='crud_page'),
    path('add_clinic/', add_clinic, name='add_clinic'),
    path('edit_clinic/', edit_clinic, name='edit_clinic'),
    path('edit/<int:clinic_id>/', edit, name='edit'),
    path('delete_clinic/<int:clinic_id>/', delete_clinic, name='delete'),
]
