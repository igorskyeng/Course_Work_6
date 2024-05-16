import random

from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory

from pytils.translit import slugify

from blog.models import Blog
from main.forms import ClientAddForm, MessageAddForm, MallingAddForm
from main.models import ClientService, MessageMailing, Mailing, MailingAttempt


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = ClientService
    form_class = ClientAddForm
    success_url = reverse_lazy('main:client_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Добавление клиента'

        return context_data

    def form_valid(self, form):
        client = form.save()
        client.user = self.request.user
        client.save()

        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    model = ClientService
    template_name = "main/clientservice_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        client = ClientService.objects.all()

        context_data['object_groups_user'] = str(self.request.user.groups.filter(name='manager'))
        context_data['object_groups'] = '<QuerySet [<Group: manager>]>'
        context_data['object_list'] = client
        context_data['title'] = 'Клиенты'

        return context_data


class ClientDetailtView(LoginRequiredMixin, DetailView):
    model = ClientService

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Просмотр клиента'

        return context_data


class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ClientService
    form_class = ClientAddForm

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Редактирование клиента'

        return context_data

    def test_func(self):
        if self.get_object().email == self.request.user or self.request.user.is_superuser:
            return True

        else:
            return self.handle_no_permission()

    def get_success_url(self):
        return reverse('main:client_detail', args=[self.kwargs.get('pk')])


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = ClientService
    success_url = reverse_lazy('main:client_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Удаление клиента'

        return context_data


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = MessageMailing
    form_class = MessageAddForm
    success_url = reverse_lazy('main:message_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Добавление сообщения'

        return context_data

    def form_valid(self, form):
        client = form.save()
        client.user = self.request.user
        client.save()

        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    model = MessageMailing
    template_name = "main/messagemailing_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        message = MessageMailing.objects.all()

        context_data['object_groups_user'] = str(self.request.user.groups.filter(name='manager'))
        context_data['object_groups'] = '<QuerySet [<Group: manager>]>'
        context_data['object_list'] = message
        context_data['title'] = 'Сообщения'

        return context_data


class MessageDetailtView(LoginRequiredMixin, DetailView):
    model = MessageMailing

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Просмотр сообщения'

        return context_data


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MessageMailing
    form_class = MessageAddForm

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Редактирование сообщения'

        return context_data

    def get_success_url(self):
        return reverse('main:message_detail', args=[self.kwargs.get('pk')])


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MessageMailing
    success_url = reverse_lazy('main:message_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Удаление сообщения'

        return context_data


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MallingAddForm
    success_url = reverse_lazy('main:mailing_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Добавление рассылки'

        return context_data

    def form_valid(self, form):
        client = form.save()
        client.user = self.request.user
        client.save()

        return super().form_valid(form)


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = "main/mailing_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        mailing = Mailing.objects.all()

        context_data['object_groups_user'] = str(self.request.user.groups.filter(name='manager'))
        context_data['object_groups'] = '<QuerySet [<Group: manager>]>'
        context_data['object_list'] = mailing
        context_data['title'] = 'Рассылки'

        return context_data


class MailingDetailtView(LoginRequiredMixin, DetailView):
    model = Mailing

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        mailing = Mailing.objects.all()

        for mailing_clients in mailing:
            context_data['object_client'] = mailing_clients.client.all()

        context_data['title'] = 'Просмотр рассылки'

        return context_data


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MallingAddForm

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Добавление рассылки'

        return context_data

    def get_success_url(self):
        return reverse('main:mailing_detail', args=[self.kwargs.get('pk')])


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('main:mailing_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['title'] = 'Удаление рассылки'

        return context_data


def disable_the_mailing(request, pk):
    mailin_item = get_object_or_404(Mailing, pk=pk)
    if mailin_item.status_mailing == "Запущена":
        mailin_item.status_mailing = "Завершена"

    elif mailin_item.status_mailing == "Завершена":
        mailin_item.status_mailing = "Запущена"

    mailin_item.save()

    return redirect(reverse('main:mailing_list'))


class ReportListView(LoginRequiredMixin, ListView):
    model = MailingAttempt
    template_name = "main/report_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        report = MailingAttempt.objects.all()

        context_data['object_groups_user'] = str(self.request.user.groups.filter(name='manager'))
        context_data['object_groups'] = '<QuerySet [<Group: manager>]>'
        context_data['object_list'] = report
        context_data['title'] = 'Отчет'

        return context_data


class HomeListView(ListView):
    model = Mailing
    template_name = 'main/home_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailing'] = Mailing.objects.all().count()
        context_data['active_mailing'] = Mailing.objects.filter(status_mailing='Запущена').count()
        blog_list = list(Blog.objects.all())
        random.shuffle(blog_list)
        context_data['object_list'] = blog_list[:3]
        context_data['clients_count'] = ClientService.objects.all().count()
        context_data['title'] = 'Главная'
        return context_data
