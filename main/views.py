from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory

from pytils.translit import slugify

from main.forms import ClientAddForm, MessageAddForm
from main.models import ClientService, MessageMailing, Mailing, MailingAttempt
from main.services import get_date_from_cache


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = ClientService
    form_class = ClientAddForm
    success_url = reverse_lazy('main:client_list')


class ClientListView(LoginRequiredMixin, ListView):
    model = ClientService
    template_name = "main/clientservice_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        client = ClientService.objects.all()

        context_data['object_list'] = client
        context_data['title'] = 'Клиенты'

        return context_data


class ClientDetailtView(LoginRequiredMixin, DetailView):
    model = ClientService


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = ClientService
    form_class = ClientAddForm

    def get_success_url(self):
        return reverse('main:client_detail', args=[self.kwargs.get('pk')])


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = ClientService
    success_url = reverse_lazy('main:client_list')


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = MessageMailing
    form_class = MessageAddForm
    success_url = reverse_lazy('main:message_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = MessageMailing
    template_name = "main/messagemailing_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        message = MessageMailing.objects.all()

        context_data['object_list'] = message
        context_data['title'] = 'Сообщения'

        return context_data


class MessageDetailtView(LoginRequiredMixin, DetailView):
    model = MessageMailing


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MessageMailing
    form_class = MessageAddForm

    def get_success_url(self):
        return reverse('main:message_detail', args=[self.kwargs.get('pk')])


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MessageMailing
    success_url = reverse_lazy('main:message_list')
