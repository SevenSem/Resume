from django import forms
from .models import *

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(
            attrs={'required': 'required', 'class': "form-check-input", 'type': "radio"})
                                   )

        fields = ['firstname', 'middlename', 'lastname', 'email', 'dob', 'gender', 'phone', 'country', 'state', 'city','image', 'template']
        widgets = {

            'firstname': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "First Name"}),
            'middlename': forms.TextInput(
                attrs={'class': 'form-control ','placeholder': "Middle Name"}),
            'lastname': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required', 'placeholder': "Last Name"}),
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Email"}),
            'dob': forms.TextInput(
                attrs={'class': 'form-control ','type':"date",'placeholder': " Date of birth "}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Phone"}),
            'country': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Country"}),
            'state': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "State"}),
            'city': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "city"}),
            # 'gender':forms.
        }


class EducationalForm(forms.ModelForm):
    class Meta:
        model = EducationalInfo
        fields = ['program', 'institution', 'course', 'edate1', 'edate2']
        widgets = {

            'program': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Enter program"}),
            'institution': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': "Enter Institution "}),
            'course': forms.TextInput(
                attrs={'class': 'form-control ','placeholder': "Enter Course"}),
            'edate1': forms.TextInput(
                attrs={'class': 'form-control ','type':"date",'placeholder': "Starting Date "}),
            'edate2': forms.TextInput(
                attrs={'class': 'form-control ','type':"date",'placeholder': "Ending Date "}),
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceInfo
        fields = ['company', 'title', 'course', 'startingDate', 'endingDate', 'experienceInfo']

        widgets = {

            'company': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Enter Company"}),
            'title': forms.TextInput(
                attrs={'class': 'form-control ','placeholder': "Enter Job Title "}),
            'course': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': "Enter Course / Project"}),
            'startingDate': forms.TextInput(
                attrs={'class': 'form-control ','type':"date",'placeholder': "Starting Date "}),
            'endingDate': forms.TextInput(
                attrs={'class': 'form-control ','type':"date",'placeholder': "Ending Date "}),
            'experienceInfo': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': "Enter Company"}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill']

        widgets = {

            'skill': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Skills seperated by comma , "})
        }


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['certificate', 'certificateDate']
        widgets = {

            'certificate': forms.TextInput(
                attrs={'class': 'form-control','placeholder': "Certificate Name "}),
            'certificateDate': forms.TextInput(
                attrs={'class': 'form-control ','type':"date",'placeholder': "Certified Date "}),
        }

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['language']

        widgets = {

            'language': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Language"})
        }


class PersonalDescriptionForm(forms.ModelForm):
    class Meta:
        model = PersonalDescription
        fields = ['about','Job_title']

        widgets = {
            'Job_title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Your Main Job Title"}),
            'about': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': "About YourSelf"})

        }


class OthersForm(forms.ModelForm):
    class Meta:
        model = Others
        fields = ['title','introduction']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Title"}),
            'introduction': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': "Description"})
        }