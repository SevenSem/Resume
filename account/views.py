from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.conf import settings

from django.core.mail import send_mail  
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.template import Context

User = settings.AUTH_USER_MODEL
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            ######################### mail system ####################################
            htmly = get_template('pages/email.html')
            d = { 'username': username }
            subject, from_email, to = 'Welcome', 'a4collegeteam@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
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
            return render(request,'pages/index.html')
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