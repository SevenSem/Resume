from django.urls import path, include
from resume import views

urlpatterns = [ 
    # path('', views.index, name='home'),
    path('createresume', views.resumeForm, name='resumeform'),
    path('choosetemplates', views.choosetemplates, name='choosetemplates'),
    path('apilist', views.apilist, name='apilist'),
    path('templates/<id>', views.templates, name='templates'),
    path('update-resume/<int:pk>/', views.ResumeUpdate.as_view(), name="update_resume"),
    path('delete_resume/<int:pk>/', views.resumeDeleteView.as_view(), name="delete_resume"),


    path('templates1/<id>', views.templates1, name='templates1'),
    path('templates2/<id>', views.templates2, name='templates2'),
    path('templates4/<id>', views.templates4, name='templates4'),

    path('templates5/<id>', views.templates5, name='templates5'),


    path('pdf_view/<id>', views.ViewPDF.as_view(), name="pdf_view"),
    path('chart', views.chart, name='chart'),
    path('prediction/', include('prediction.urls'), name="prediction"),
    path('', views.Home.as_view(), name='home'),
    path('dashboard', views.Dashboard.as_view(), name='dashboard'),
    
]
