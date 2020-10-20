from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

class PersonalInfo(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=255,blank=True )
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    phone = models.CharField(max_length=100)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=None,blank=True)

    def __str__(self):
        return self.firstname


class EducationalInfo(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo,  on_delete=models.CASCADE)
    program = models.CharField(max_length=255,blank=True)
    institution = models.CharField(max_length=100,blank=True)
    course = models.BooleanField(default=0,blank=True)
    edate1 = models.CharField(max_length=255,blank=True)
    edate2 = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.program

class ExperienceInfo(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    company = models.CharField(max_length=255,blank=True)
    title = models.CharField(max_length=255,blank=True)
    course = models.CharField(max_length=255,blank=True)
    startingDate = models.CharField(max_length=255,blank=True)
    endingDate = models.CharField(max_length=255,blank=True)
    experienceInfo = models.TextField(max_length=255,blank=True)

    def __str__(self):
        return self.company


class Skills(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255,blank=True)

class Certificate(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    certificate = models.CharField(max_length=255)
    certificateDate = models.CharField(max_length=255)

class Language(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    language = models.CharField(max_length=255,blank=True)


class PersonalDescription(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    Job_title = models.CharField(max_length=255,blank=True)
    about = models.TextField(max_length=255,blank=True)

class Others(models.Model):
    personalinfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,blank=True)
    introduction = models.TextField(max_length=255,blank=True)

