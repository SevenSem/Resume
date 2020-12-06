from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.conf import settings


User = settings.AUTH_USER_MODEL
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistrationForm()
    return render(request, 'pages/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Wrong username and password")
            return redirect('login')
    else:
        return render(request, 'pages/login.html')


def resetPassword(request):
    return render(request, 'pages/resetpassword.html')


def logout(request):
    auth.logout(request)
    return redirect('/')