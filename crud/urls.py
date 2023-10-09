from django.urls import path
from .views import clinic_list

urlpatterns = [
    path('', clinic_list, name='clinic_list'),
]