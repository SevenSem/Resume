import datetime
from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from .utils import *
from django.views.generic import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer


# Create your views here.
def index(request):
    data = {
        'personalinfodata': PersonalInfo.objects.filter(author__username=request.user)
    }
    return render(request, 'pages/index.html', data)


def resumeForm(request):
    personalform = PersonalInfoForm(request.POST , request.FILES or None)
    personaldescform = PersonalDescriptionForm(request.POST or None)
    EduFormset = modelformset_factory(EducationalInfo, form=EducationalForm)
    eduform = EduFormset(request.POST or None, queryset=EducationalInfo.objects.none(), prefix='educationalInfo')
    ExpFormset = modelformset_factory(ExperienceInfo, form=ExperienceForm)
    experienceform = ExpFormset(request.POST or None, queryset=ExperienceInfo.objects.none(), prefix='experienceInfo')
    SkillFormset = modelformset_factory(Skills, form=SkillForm)
    skillsform = SkillFormset(request.POST or None, queryset=Skills.objects.none(), prefix='skills')
    certificateFormset = modelformset_factory(Certificate, form=CertificateForm)
    certificateform = certificateFormset(request.POST or None, queryset=Certificate.objects.none(),
                                         prefix='certificate')
    languageFormset = modelformset_factory(Language, form=LanguageForm)
    languageform = languageFormset(request.POST or None, queryset=Language.objects.none(), prefix='language')

    otherFormset = modelformset_factory(Others, form=OthersForm)
    otherform = otherFormset(request.POST or None, queryset=Others.objects.none(), prefix='other')

    if request.method == 'POST':
        if personalform.is_valid() and eduform.is_valid() \
                and experienceform.is_valid() and skillsform.is_valid() \
                and certificateform.is_valid() and languageform.is_valid() and otherform.is_valid():
            print("test completed")

            try:
                with transaction.atomic():
                    personalinfo = personalform.save(commit=False)
                    personalinfo.author = request.user
                    personalinfo.save()

                    aboutpersonal = personaldescform.save(commit=False)
                    aboutpersonal.personalinfo = personalinfo
                    aboutpersonal.save()

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

                    for other in otherform:
                        otherforms = other.save(commit=False)
                        otherforms.personalinfo = personalinfo
                        otherforms.save()

            except IntegrityError:
                print('error')

            return redirect('templates',personalinfo.pk)

    data = {
        'form': personalform,
        'personaldescform': personaldescform,
        'formset': eduform,
        'experienceform': experienceform,
        'skillform': skillsform,
        'certificateform': certificateform,
        'languageform': languageform,
        'others': otherform
    }
    return render(request, 'form/form.html', data)


def resume_Update(request,id):
    personaldata = PersonalInfo.objects.get(id=id)
    personaldescform = PersonalDescriptionForm(request.POST or None)
    personalform = PersonalInfoForm(request.POST or None, instance=personaldata)
    EduFormset = modelformset_factory(EducationalInfo, form=EducationalForm)
    eduform = EduFormset(request.POST or None, queryset=EducationalInfo.objects.filter(personalinfo__id=id),
                         prefix='educationalInfo')
    ExpFormset = modelformset_factory(ExperienceInfo, form=ExperienceForm)
    experienceform = ExpFormset(request.POST or None, queryset=ExperienceInfo.objects.filter(personalinfo__id=id),
                                prefix='experienceInfo')
    SkillFormset = modelformset_factory(Skills, form=SkillForm)
    skillsform = SkillFormset(request.POST or None, queryset=Skills.objects.filter(personalinfo__id=id),
                              prefix='skills')
    certificateFormset = modelformset_factory(Certificate, form=CertificateForm)
    certificateform = certificateFormset(request.POST or None, queryset=Certificate.objects.filter(personalinfo__id=id),
                                         prefix='certificate')
    languageFormset = modelformset_factory(Language, form=LanguageForm)
    languageform = languageFormset(request.POST or None, queryset=Language.objects.filter(personalinfo__id=id),
                                   prefix='language')
    otherFormset = modelformset_factory(Others, form=OthersForm)
    otherform = otherFormset(request.POST or None, queryset=Others.objects.filter(personalinfo__id=id), prefix='other')

    if request.method == 'POST':
        if personalform.is_valid() and eduform.is_valid() \
                and experienceform.is_valid() and skillsform.is_valid() \
                and certificateform.is_valid() and languageform.is_valid() and otherform.is_valid():
            print("test completed")
            try:
                with transaction.atomic():
                    personalinfo = personalform.save(commit=False)
                    personalinfo.author = request.user
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
                    for other in otherform:
                        otherforms = other.save(commit=False)
                        otherforms.personalinfo = personalinfo
                        otherforms.save()

            except IntegrityError:
                print('error')

            return redirect('resumeform')

    data = {
        'form': personalform,
        'personaldescform': personaldescform,
        'formset': eduform,
        'experienceform': experienceform,
        'skillform': skillsform,
        'certificateform': certificateform,
        'languageform': languageform,
        'others': otherform
    }
    return render(request, 'form/form.html', data)


def templates(request, id):
    if request.user.is_authenticated:
        data = templatesdata(id)
    else:
        return redirect('resumeform')
    return render(request, 'resumes/resume1.html', data)


def templatesdata(id):
    data = {
        'personalinfodata': PersonalInfo.objects.get(id=id),
        'educationalinfodata': EducationalInfo.objects.filter(personalinfo__id=id),
        'experienceinfodata': ExperienceInfo.objects.filter(personalinfo__id=id),
        'certificatedata': Certificate.objects.filter(personalinfo__id=id),
        'skilldata': Skills.objects.filter(personalinfo__id=id),
        'languagedata': Language.objects.filter(id=id),
    }
    return data

def storage(request):
    data = {
        'personalinfodata': PersonalInfo.objects.filter(author__username=request.user)
    }
    return render(request, 'pages/storage.html', data)


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class ViewPDF(View):
    def get(self, request, id, *args, **kwargs):
        data = templatesdata(id)
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


@api_view(['GET'])
def apilist(request):
    tasks = ExperienceInfo.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


def choosetemplates(request):
    return render(request, 'pages/choosetemplates.html')
