from django import forms
from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control form-control-user','placeholder':'Enter Password' }))
    password2 = forms.CharField(widget=forms.PasswordInput(
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

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user