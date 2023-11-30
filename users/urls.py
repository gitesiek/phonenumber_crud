from django.urls import path, include   
from .views import login_page


urlpatterns = [
    path('login', login_page, name='login_page'),
    path("accounts/", include("django.contrib.auth.urls")),
]
