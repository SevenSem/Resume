from django.contrib import admin
from .models import *

class PersonalDescription(admin.TabularInline):
    model = PersonalDescription
    extra = 0

class EducationalInfo(admin.TabularInline):
    model = EducationalInfo
    extra = 0

class ExperienceInfo(admin.TabularInline):
    model = ExperienceInfo
    extra = 0

class Skills(admin.TabularInline):
    model = Skills
    extra = 0

class Certificate(admin.TabularInline):
    model = Certificate
    extra = 0

class Language(admin.TabularInline):
    model = Language
    extra = 0

class Others(admin.TabularInline):
    model = Others
    extra = 0


class Resume(admin.ModelAdmin):
    model   = PersonalInfo
    inlines = [PersonalDescription,EducationalInfo,ExperienceInfo,Skills,Certificate,Language,Others]
# Register your models here.
admin.site.register(PersonalInfo,Resume)

admin.site.register(Templates)




@admin.register(Messagebox)
class ContactDetails(admin.ModelAdmin):
    list_display = ['full_Name', 'subject','created_date']