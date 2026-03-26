from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

MEMBER_EMAILS = [
    'syifaakrt@gmail.com' #kalo mau test, masukin email kalian disini
]

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'main.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')
