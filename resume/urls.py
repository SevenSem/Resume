from django.urls import path , include
from . import views

urlpatterns = [
    
    path('', views.index, name = 'home'),
    path('createresume', views.resumeForm, name='resumeform'),
    path('choosetemplates',views.choosetemplates,name='choosetemplates'),
    path('apilist', views.apilist, name='apilist'),
    path('resume_Update/<id>',views.resume_Update,name='resume_Update'),
    path('templates/<id>',views.templates,name='templates'),
    path('pdf_view/<id>', views.ViewPDF.as_view(), name="pdf_view"),
    path('chart', views.chart, name='chart'),
    path('prediction/',include('prediction.urls'))

    ]