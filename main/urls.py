from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import (ClientListView, ClientCreateView, ClientDetailtView, ClientUpdateView, ClientDeleteView,
                        MessageListView, MessageCreateView, MessageDetailtView, MessageUpdateView, MessageDeleteView)

app_name = MainConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('add_client/', ClientCreateView.as_view(), name='create_client'),
    path('view_client/<int:pk>/', cache_page(60)(ClientDetailtView.as_view()), name='client_detail'),
    path('edit_client/<int:pk>', ClientUpdateView.as_view(), name='client_edit'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('view_message/<int:pk>/', cache_page(60)(MessageDetailtView.as_view()), name='message_detail'),
    path('edit_message/<int:pk>', MessageUpdateView.as_view(), name='message_edit'),
    path('delete_message/<int:pk>', MessageDeleteView.as_view(), name='delete_message')
]
