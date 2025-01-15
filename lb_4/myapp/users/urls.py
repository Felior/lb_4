from django.urls import path
from .views import client_profile, register_page, user_list

urlpatterns = [
    path('profile/', client_profile, name='client_profile'),
    path('register/', register_page, name='register_page'),
    path('list/', user_list, name='user_list'),
]