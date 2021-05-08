from django.shortcuts import render, redirect
from account.forms import RegistrationForm,UserUpdateForm, ProfileUpdateForm
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required
def profile(request):
    return render(request, 'pages/profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'pages/updateprofile.html', context)

    