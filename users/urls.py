from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users.views import RegisterView, ProfileView, PasswordRecoveryView, UserLoginView, verification

from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/confirm/<str:token>/', verification, name='verification'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_recovery/', PasswordRecoveryView.as_view(), name='password_recovery'),
    path('message_verification/', TemplateView.as_view(template_name='users/message_verification.html'),
         name='message_verification'),
    path('successfully/', TemplateView.as_view(template_name='users/successfully.html'), name='successfully'),
    path('unsuccessfully/', TemplateView.as_view(template_name='users/unsuccessfully.html'), name='unsuccessfully'),
]
