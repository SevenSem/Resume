from django.urls import path
from django.contrib.auth import views as auth_views
# from users import views as user_views

from . import views

urlpatterns = [
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name='logout'),
    path('profile/', views.profile, name = 'profile'),
    path('profileupdate/', views.profile_update, name = 'profileupdate'),


      path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="pages/resetpassword.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="pages/password_reset_done.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="pages/password_reset_confirm.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="pages/password_reset_complete.html"), 
        name="password_reset_complete"),
    ]