from django.shortcuts import render
from .models import Client

def client_profile(request):
    client = Client.objects.first()  # First profile from the database
    return render(request, 'users/profile.html', {'client': client})

def register_page(request):
    return render(request, 'users/register.html')

def user_list(request):
    users = Client.objects.all()
    return render(request, 'users/user_list.html', {'users': users})