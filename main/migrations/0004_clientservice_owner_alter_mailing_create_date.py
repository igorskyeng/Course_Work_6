# Generated by Django 5.0.4 on 2024-05-13 07:14

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_clientservice_email_alter_mailing_create_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='clientservice',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Продавец'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 13, 15, 14, 11, 96959), verbose_name='Дата и время отправки рассылки'),
        ),
    ]