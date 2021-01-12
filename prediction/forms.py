from django import forms
from .models import UploadCv

class FileFieldForm(forms.Form):

    class Meta:
        model = UploadCv
        fields = ['personalinfo', 'uploadedfile']