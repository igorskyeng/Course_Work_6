from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import ClientListView

app_name = MainConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
]
