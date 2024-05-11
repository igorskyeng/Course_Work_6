from datetime import datetime, timezone

from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class ClientService(models.Model):
    email = models.EmailField(max_length=150, unique=True, verbose_name='Почта')
    name = models.CharField(max_length=100, verbose_name='ФИО')
    comments = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('id',)


class MessageMailing(models.Model):
    subject_line = models.CharField(max_length=150, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Текс сообщения', **NULLABLE)

    def __str__(self):
        return self.subject_line

    class Meta:
        verbose_name = 'Сообщение рассылки'
        verbose_name_plural = 'Сообщения рассылки'
        ordering = ('id',)


class Mailing(models.Model):

    class PeriodMailing(models.TextChoices):
        ONE_DAY = "Раз в день", "Раз в день"
        ONE_WEEK = "Раз в неделю", "Раз в неделю"
        ONE_MONTH = "Раз в месяц", "Раз в месяц"

    class StatusMailing(models.TextChoices):
        STARTED = "Запущена", "Запущена"
        CREATED = "Создана", "Создана"
        COMPLETED = "Завершена", "Завершена"

    create_date = models.DateTimeField(default=datetime.now(), verbose_name='Дата и время первой '
                                                                            'отправки рассылки')
    period_mailing = models.CharField(max_length=50, choices=PeriodMailing, verbose_name='Периодичность рассылки')
    status_mailing = models.CharField(max_length=50, choices=StatusMailing, verbose_name='Статус рассылки ')
    client = models.ForeignKey(ClientService, on_delete=models.CASCADE, verbose_name='Клиенты рассылки')
    message = models.OneToOneField(MessageMailing, on_delete=models.SET_NULL, verbose_name='Рассылка', **NULLABLE)

    def __str__(self):
        return self.status_mailing

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ('id',)


class MailingAttempt(models.Model):
    date_last_mailing = models.DateField(verbose_name='Дата и время последней рассылки', auto_now_add=True)
    status_mailing = models.BooleanField(verbose_name='Статус рассылки')
    server_response = models.CharField(verbose_name='Ответ почтового сервера', **NULLABLE)
    mailing = models.ForeignKey(Mailing, verbose_name='Рассылки', on_delete=models.CASCADE)

    def __str__(self):
        return self.date_last_mailing

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылок'
        ordering = ('id',)
