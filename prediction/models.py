from django.db import models
from resume.models import PersonalInfo
from django.core.exceptions import ValidationError
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
def validate_file_size(value):
    filesize= value.size
    if filesize > 5485760:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value

class UploadCv(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo,  on_delete=models.CASCADE)
    cv_user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploadfile = models.FileField(null =True, blank = True, upload_to='files/', validators=[validate_file_size])
            