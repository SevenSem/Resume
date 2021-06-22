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

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

class UploadCv(models.Model):
    # personalinfo = models.ForeignKey(PersonalInfo,  on_delete=models.CASCADE)
    keywords = models.CharField(max_length=200, null=True)
    cv_user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploadfile = models.FileField(null =True, blank = True, upload_to='files/', validators=[validate_file_extension, validate_file_size])
            