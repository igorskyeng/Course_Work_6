from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import (ClientListView, ClientCreateView, ClientDetailtView, ClientUpdateView, ClientDeleteView,
                        MessageListView, MessageCreateView, MessageDetailtView, MessageUpdateView, MessageDeleteView,
                        MailingListView, MailingCreateView, MailingDetailtView, MailingUpdateView, MailingDeleteView,
                        disable_the_mailing, ReportListView, HomeListView)

app_name = MainConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home_list'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('add_client/', ClientCreateView.as_view(), name='create_client'),
    path('view_client/<int:pk>/', cache_page(60)(ClientDetailtView.as_view()), name='client_detail'),
    path('edit_client/<int:pk>', ClientUpdateView.as_view(), name='client_edit'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('view_message/<int:pk>/', cache_page(60)(MessageDetailtView.as_view()), name='message_detail'),
    path('edit_message/<int:pk>', MessageUpdateView.as_view(), name='message_edit'),
    path('delete_message/<int:pk>', MessageDeleteView.as_view(), name='delete_message'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('view_mailing/<int:pk>/', cache_page(60)(MailingDetailtView.as_view()), name='mailing_detail'),
    path('edit_mailing/<int:pk>', MailingUpdateView.as_view(), name='mailing_edit'),
    path('delete_mailing/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),
    path('activity/<int:pk>', disable_the_mailing, name='disable_the_mailing'),
    path('report_list/', ReportListView.as_view(), name='report_list'),
]
