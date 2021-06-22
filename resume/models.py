from django.db import models
from django.contrib.auth.models import User
from datetime import date


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class Templates(models.Model):
    template = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.template
    
    
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [ '.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_file_size(value):
    filesize= value.size
    if filesize > 5485760:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value
        
class PersonalInfo(models.Model):
    template = models.ForeignKey(Templates, on_delete=models.CASCADE,default=1, blank=True)
    firstname = models.CharField(max_length=100, blank=True)
    middlename = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=255,blank=True, null=True)
    dob = models.CharField(max_length=255,blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128,blank=True, null=True)
    phone = models.CharField(max_length=100,blank=True, null=True)
    country = models.CharField(max_length=255,blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)
    city = models.CharField(max_length=255,blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, validators=[validate_file_extension, validate_file_size])
    
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.firstname


class EducationalInfo(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo,  on_delete=models.CASCADE)
    program = models.CharField(max_length=255, blank=True)
    institution = models.CharField(max_length=100, blank=True)
    course = models.CharField(max_length=100, blank=True)
    edate1 = models.CharField(max_length=255, blank=True)
    edate2 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.program


class ExperienceInfo(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    company = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    course = models.CharField(max_length=255, blank=True)
    startingDate = models.CharField(max_length=255, blank=True)
    endingDate = models.CharField(max_length=255, blank=True)
    experienceInfo = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.company

    def date(self):
        pass 


class Skills(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255, blank=True)


class Certificate(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    certificate = models.CharField(max_length=255, blank=True)
    certificateDate = models.CharField(max_length=255, blank=True)


class Language(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    language = models.CharField(max_length=255, blank=True)


class PersonalDescription(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    Job_title = models.CharField(max_length=255, blank=True)
    about = models.TextField(max_length=255, blank=True)


class Others(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    introduction = models.TextField(max_length=255, blank=True)


class Messagebox(models.Model):
    created_date = models.DateField(default=date.today)
    full_Name = models.CharField(default='', max_length=100)
    email = models.CharField(default='', max_length=30, blank=True)
    subject = models.CharField(default='', max_length=50, blank=True)
    message = models.CharField(default='', max_length=400, blank=True)

    def __str__(self):
        return self.full_Name

    class Meta:
        ordering = ['-created_date' ]

