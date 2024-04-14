from django.urls import path, include   
from .views import (
    login_page,
    user_create, user_delete, user_details, user_edit, user_list,
    group_create, group_delete, group_details, group_edit, group_list,
)


urlpatterns = [
    path('login', login_page, name='login_page'),
    path("accounts/", include("django.contrib.auth.urls")),

    path('user_list', user_list, name='user_list_page'),
    path('user/create', user_create, name='user_create'), #to trzeba dodac do wszystkich niżej, z taką nazwą jak chcesz miec w html
    path('user/delete', user_delete),
    path('user/details', user_details),
    path('user/edit', user_edit),

    path('group_list', group_list, name='group_list_page'),
    path('group/create', group_create),
    path('group/delete', group_delete),
    path('group/details', group_details),
    path('group/edit', group_edit),
]
