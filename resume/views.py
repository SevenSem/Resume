import datetime
from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from .utils import *
from django.views.generic import CreateView, UpdateView, DeleteView,TemplateView
from django.views.generic import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.urls import reverse_lazy
from personality.models import PersonalityData,PersonalityResult
from resume.models import *
from resume import  models
from resume import forms
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormView

# Create your views here.
class Home(CreateView):
    model = Messagebox
    form_class = forms.MessagesForm
    template_name = "pages/homee.html"
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["personalinfodata"] = PersonalInfo.objects.filter(author__username=self.request.user)
        return context
    
class Dashboard(TemplateView):
    template_name = "pages/index.html"
    
def index(request):
    data = {
        'personalinfodata': PersonalInfo.objects.filter(author__username=request.user)
    }
    if request.user.is_authenticated:
        return render(request, 'pages/index.html', data)
    else:
         return render(request, 'pages/homee.html', data)



def resumeForm(request):
    personalform = PersonalInfoForm(request.POST , request.FILES or None)
    personaldescform = PersonalDescriptionForm(request.POST or None)
    EduFormset = modelformset_factory(EducationalInfo, form=EducationalForm)
    eduform = EduFormset(request.POST or None, queryset=EducationalInfo.objects.none(
    ), prefix='educationalInfo')
    ExpFormset = modelformset_factory(ExperienceInfo, form=ExperienceForm)
    experienceform = ExpFormset(
        request.POST or None, queryset=ExperienceInfo.objects.none(), prefix='experienceInfo')
    SkillFormset = modelformset_factory(Skills, form=SkillForm)
    skillsform = SkillFormset(request.POST or None,
                              queryset=Skills.objects.none(), prefix='skills')
    certificateFormset = modelformset_factory(
        Certificate, form=CertificateForm)
    certificateform = certificateFormset(request.POST or None, queryset=Certificate.objects.none(),
                                         prefix='certificate')
    languageFormset = modelformset_factory(Language, form=LanguageForm)
    languageform = languageFormset(
        request.POST or None, queryset=Language.objects.none(), prefix='language')

    otherFormset = modelformset_factory(Others, form=OthersForm)
    otherform = otherFormset(request.POST or None,
                             queryset=Others.objects.none(), prefix='other')

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

            return redirect('templates', personalinfo.pk)

    data = {
        'form': personalform,
        'personaldescform': personaldescform,
        'formset': eduform,
        'experienceform': experienceform,
        'skillform': skillsform,
        'certificateform': certificateform,
        'languageform': languageform,
        'others': otherform,
        'templates': Templates.objects.all(),
    }
    return render(request, 'form/form.html', data)


class ResumeUpdate(UpdateView):
    model = models.PersonalInfo
    form_class = forms.PersonalInfoForm
    template_name = 'form/testform.html'
    success_url=reverse_lazy('home')

    def get_context_data(self, **kwargs):
        data = super(ResumeUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['educationalInfo'] = forms.EducationalFormset(self.request.POST, instance=self.object ,prefix='educationalInfo')
            data['experienceInfo'] = forms.ExperienceFormset(self.request.POST, instance=self.object,prefix='experienceInfo')
            data['skills'] = forms.SkillFormset(self.request.POST, instance=self.object,prefix='skills')
            data['certificate'] = forms.CertificateFormset(self.request.POST, instance=self.object,prefix='certificate')
            data['language'] = forms.LanguageFormset(self.request.POST, instance=self.object,prefix='language')
            data['others'] = forms.OthersFormset(self.request.POST, instance=self.object,prefix='others')
        else:
            data['educationalInfo'] = forms.EducationalFormset(instance=self.object,prefix='educationalInfo')
            data['experienceInfo'] = forms.ExperienceFormset(instance=self.object,prefix='experienceInfo')
            data['skills'] = forms.SkillFormset(instance=self.object,prefix='skills')
            data['certificate'] = forms.CertificateFormset(instance=self.object,prefix='certificate')
            data['language'] = forms.LanguageFormset(instance=self.object,prefix='language')
            data['others'] = forms.OthersFormset(instance=self.object,prefix='others')
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        education = context['educationalInfo']
        experience = context['experienceInfo']
        skill = context['skills']
        certificate = context['certificate']
        other = context['others']
        language = context['language']

        with transaction.atomic():
            self.object = form.save()
            if education.is_valid() and experience.is_valid() and skill.is_valid() and certificate.is_valid() and language.is_valid() and other.is_valid():
                education.instance = self.object
                education.save()
                experience.instance = self.object
                experience.save()
                skill.instance = self.object
                skill.save()
                certificate.instance = self.object
                certificate.save()
                language.instance = self.object
                language.save()
                other.instance = self.object
                other.save()
            else:
                return self.render_to_response(self.get_context_data(form=form))

        return super(ResumeUpdate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

  
def templates(request, id):
    if request.user.is_authenticated:
        data = templatesdata(id)
    else:
        return redirect('resumeform')
    return render(request, 'resumes/resume1.html', data)


def templates1(request, id):
    if request.user.is_authenticated:
        data = templatesdata(id)
    else:
        return redirect('resumeform1')
    return render(request, 'resumes/resume3.html', data)


def templates2(request, id):
    if request.user.is_authenticated:
        data = templatesdata(id)
    else:
        return redirect('resumeform')
    return render(request, 'resumes/resume2.html', data)


def templatesdata(id):
    data = {
        'personalinfodata': PersonalInfo.objects.get(id=id),
        'educationalinfodata': EducationalInfo.objects.filter(personalinfo__id=id),
        'experienceinfodata': ExperienceInfo.objects.filter(personalinfo__id=id),
        'certificatedata': Certificate.objects.filter(personalinfo__id=id),
        'skilldata': Skills.objects.filter(personalinfo__id=id),
        'languagedata': Language.objects.filter(personalinfo__id=id),
        'personaldesc': PersonalDescription.objects.get(personalinfo__id=id),
        'othersinfo': Others.objects.get(personalinfo__id=id),
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
    temp = Templates.objects.all()
    data= {
        'templates' : temp
    }
    return render(request, 'pages/choosetemplates.html',data)


def chart(request):
    data = {
        'avg' : PersonalityData.objects.filter(user__username= request.user).order_by('-id')[:1],
        'personalityresult' : PersonalityResult.objects.all()
    }
    return render(request, 'pages/chart.html', data)

class resumeDeleteView(DeleteView):
    template_name = 'pages/confirmdelete.html'
    model = models.PersonalInfo
    success_url = reverse_lazy('home')