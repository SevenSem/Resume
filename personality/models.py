from django.db import models
from django.contrib.auth.models import User


class PersonalityType(models.Model):
    name   = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class PersonalityQuestion(models.Model):
    question_text   = models.CharField(max_length=100)
    category        = models.ForeignKey(PersonalityType, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class TestQuestion(models.Model):
    question_text   = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text
    
    class Meta:
        ordering = ['?']


class TestChoice(models.Model):
    choice_text = models.CharField(max_length=100)
    question    = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    is_answer   = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class PersonalityData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_o = models.CharField(max_length=100)
    type_c = models.CharField(max_length=100)
    type_e = models.CharField(max_length=100)
    type_a = models.CharField(max_length=100)
    type_n = models.CharField(max_length=100)