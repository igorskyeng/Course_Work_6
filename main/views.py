from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory

from pytils.translit import slugify

from main.models import ClientService, MessageMailing, Mailing, MailingAttempt
from main.services import get_date_from_cache


class ClientListView(LoginRequiredMixin, ListView):
    model = ClientService
    template_name = "main/client_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        client = ClientService.objects.all()

        context_data['object_list'] = client
        context_data['title'] = 'Клиенты'

        return context_data
