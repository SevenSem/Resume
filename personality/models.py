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
    type_o = models.DecimalField(max_digits=5, decimal_places=2)
    type_c = models.DecimalField(max_digits=5, decimal_places=2)
    type_e = models.DecimalField(max_digits=5, decimal_places=2)
    type_a = models.DecimalField(max_digits=5, decimal_places=2)
    type_n = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.id

class PersonalityResult(models.Model):
    category        = models.ForeignKey(PersonalityType, on_delete=models.CASCADE)
    best_result   = models.CharField(max_length=500)
    bad_result   = models.CharField(max_length=500)

    def __str__(self):
        return self.best_result