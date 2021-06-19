from django import forms
from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import transaction
from .models import Applicant, Profile
# User = settings.AUTH_USER_MODEL
User = get_user_model()

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(
        attrs={'class':'form-control form-control-user','placeholder':'Enter Password' }))
    password2 = forms.CharField(label='ConfirmPassword',widget=forms.PasswordInput(
        attrs={'class':'form-control form-control-user','placeholder':'Retype Password '}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={'class':'form-control form-control-user','placeholder':'Enter Username','required':True}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control form-control-user','placeholder':'Enter First Name','required':True}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control form-control-user','placeholder':'Enter Last Name','required':True}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter Email','required':True}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email
    
    def clean_password2(self):
        data = self.cleaned_data
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('The passwords you entered are not the same')
        return password1
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save() 
        profile = Profile.objects.create(user=user)
        applicant = Applicant.objects.create(user=user)
        return user

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.save()
    #     profile = Profile.objects.create(user=user)
    #     return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

        widgets = {
                'username': forms.TextInput(
                    attrs={'class': 'form-control'}),
                'email': forms.TextInput(
                    attrs={'class': 'form-control'}),
                'first_name': forms.TextInput(
                    attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(
                    attrs={'class': 'form-control '}),
            }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
