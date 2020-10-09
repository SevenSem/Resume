from django.shortcuts import render,redirect
from .forms import *
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def resumeForm(request):
    personalform = PersonalInfoForm(request.POST or None)
    EduFormset = modelformset_factory(EducationalInfo, form=EducationalForm)
    eduform = EduFormset(request.POST or None ,queryset = EducationalInfo.objects.none(), prefix = 'educationalInfo')
    ExpFormset = modelformset_factory(ExperienceInfo, form=ExperienceForm)
    experienceform = ExpFormset(request.POST or None, queryset = ExperienceInfo.objects.none(),prefix = 'experienceInfo')
    SkillFormset = modelformset_factory(Skills, form= SkillForm )
    skillsform = SkillFormset(request.POST or None, queryset = Skills.objects.none(), prefix = 'skills')
    certificateFormset = modelformset_factory(Certificate, form=CertificateForm)
    certificateform = certificateFormset(request.POST or None, queryset = Certificate.objects.none(), prefix ='certificate')
    languageFormset = modelformset_factory(Language, form = LanguageForm)
    languageform = languageFormset(request.POST or None, queryset = Language.objects.none(),prefix = 'language')

    if request.method == 'POST':
        if personalform.is_valid() and eduform.is_valid() \
                and experienceform.is_valid() and skillsform.is_valid() \
                and certificateform.is_valid() and languageform.is_valid():

            print("test complited")
            try:
                with transaction.atomic():
                    personalinfo = personalform.save(commit=False)
                    personalinfo.save()

                    for educationalInfo in eduform:
                        data = educationalInfo.save(commit=False)
                        data.personalinfo = personalinfo
                        data.save()

                    for experienceInfo in experienceform:
                        experienceforms = experienceInfo.save(commit=False)
                        experienceforms.personalinfo = personalinfo
                        experienceforms.save()

                    for skills in skillsform:
                        skillsforms = skills.save(commit=False)
                        skillsforms.personalinfo = personalinfo
                        skillsforms.save()

                    for certicate in certificateform:
                        certificateforms = certicate.save(commit=False)
                        certificateforms.personalinfo = personalinfo
                        certificateforms.save()

                    for language in languageform:
                        languageforms = language.save(commit=False)
                        languageforms.personalinfo = personalinfo
                        languageforms.save()

            except IntegrityError:
                print('error')

            return redirect('resumeform')


    data = {
        'form': personalform,
        'formset': eduform,
        'experienceform': experienceform,
        'skillform': skillsform,
        'certificateform': certificateform,
        'languageform': languageform
    }
    return render(request, 'form/testform.html', data)
