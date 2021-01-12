from django.urls import path, include
from . import views

urlpatterns = [
    path('prediction', views.prediction, name='prediction'),
    path('uploadcv', views.FileFieldView.as_view(), name='uploadcv'),
]
