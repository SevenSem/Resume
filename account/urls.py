from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('reset-password', views.resetPassword, name = 'resetpassword'),
    path('logout', views.logout, name='logout'),
    ]