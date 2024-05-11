from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='igorskyeng@sky.pro',
            first_name='Igor',
            last_name='Barbur',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('12345')
        user.save()
