from django.contrib import admin
from main.models import ClientService
from main.models import MessageMailing
from main.models import Mailing
from main.models import MailingAttempt
from blog.models import Blog


@admin.register(ClientService)
class ClientServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'comments')
    list_filter = ('email',)
    search_fields = ('name', 'comments')


@admin.register(MessageMailing)
class MessageMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_line', 'body')
    list_filter = ('subject_line',)
    search_fields = ('body',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date', 'period_mailing', 'status_mailing', 'client', 'message')
    list_filter = ('create_date',)
    search_fields = ('client', 'message')


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_last_mailing', 'status_mailing', 'server_response', 'mailing')
    list_filter = ('date_last_mailing',)
    search_fields = ('server_response', 'mailing')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'slug', 'image_preview', 'date_of_creation',
                    'publication_sign', 'views_count')
    list_filter = ('title',)
    search_fields = ('title', 'body')
