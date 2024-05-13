from time import sleep
from django.apps import AppConfig
from django.core.management import call_command


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        sleep(2)
        call_command("start_mailing")
