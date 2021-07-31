from django.contrib import admin

from .models import AgeAndGender, PersonalityQuestion, PersonalityType, TestQuestion, TestChoice,PersonalityData,PersonalityResult

class PersonalityQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'category')

admin.site.register(PersonalityQuestion, PersonalityQuestionAdmin)

admin.site.register(PersonalityType)
admin.site.register(AgeAndGender)


class TestChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question')

admin.site.register(TestChoice, TestChoiceAdmin)

admin.site.register(TestQuestion)

class DataAdmin(admin.ModelAdmin):
    list_display = ('user','age', 'gender','type_o','type_c','type_e','type_a','type_n')

admin.site.register(PersonalityData,DataAdmin)
admin.site.register(PersonalityResult)
