import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView,  TemplateView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError

from users.forms import UserRegisterForm, UserProfileForm, PasswordRecoveryForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class UserLoginView(LoginView):
    model = User
    template_name = 'users/login.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Авторизация'

        return context_data


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:message_verification')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Регистрация'

        return context_data

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(12)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/register/confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет! Перейди по ссылке для подтверждения почты - {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def verification(request, token):
    user = User.objects.filter(token=token).first()

    if user:
        user.is_active = True
        user.save()

    return redirect('users:successfully')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('main:client_list')

    def get_object(self, queryset=None):
        return self.request.user


class PasswordRecoveryView(TemplateView):
    model = User
    template_name = 'users/password_recovery_form.html'
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy('users:login')

    code = secrets.token_hex(8)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        code = PasswordRecoveryView.code
        user.set_password(PasswordRecoveryView.code)
        user.save()

        host = self.request.get_host()
        url = f'http://{host}/users/login/'

        send_mail(
            'Восстановление пароля',
            f'Ваш новый пароль {code}, перейдите по ссылке {url}',
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

        return redirect(reverse('users:login'))
