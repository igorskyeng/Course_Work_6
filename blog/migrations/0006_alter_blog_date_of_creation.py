# Generated by Django 5.0.4 on 2024-05-13 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_date_of_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 13, 16, 3, 52, 292479), max_length=100, verbose_name='Дата создания'),
        ),
    ]
