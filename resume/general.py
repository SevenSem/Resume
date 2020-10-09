from .models import *

def send_data(request):

    data = {
        'personalinfodata' : PersonalInfo.objects.all(),
        'educationalinfodata' : EducationalInfo.objects.all(),
        'experienceinfodata' : ExperienceInfo.objects.all(),
        'skillsdata' : Skills.objects.all(),
        'certificatedata' : Certificate.objects.all(),
        'languagedata' : Language.objects.all(),
    }

    return data
