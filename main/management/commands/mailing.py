import smtplib
from datetime import datetime, timedelta
import pytz
from apscheduler.schedulers.background import BackgroundScheduler

from django.conf import settings
from django.core.mail import send_mail
from django.db.models import F

from main.models import Mailing, MessageMailing, MailingAttempt


def send_mailing():
    period_mailing = ["Раз в день", "Раз в неделю", "Раз в месяц"]
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = Mailing.objects.filter(status_mailing="Запущена")

    for mailing in mailings:
        if mailing.create_date < current_datetime + timedelta(hours=3):
            status = False
            server_response = "Нет ответа"

            try:
                send_mail(
                        subject=mailing.message.subject_line,
                        message=mailing.message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email for client in mailing.client.all()],
                        fail_silently=False
                )
                if mailing.period_mailing == period_mailing[0]:
                    mailing.create_date = F('create_date') + timedelta(days=1)

                elif mailing.period_mailing == period_mailing[1]:
                    mailing.create_date = F('create_date') + timedelta(days=7)

                elif mailing.period_mailing == period_mailing[2]:
                    mailing.create_date = F('create_date') + timedelta(days=30)

                mailing.save()

                status = True
                server_response = "Успешно"

            except smtplib.SMTPResponseException as response:
                status = False
                server_response = str(response)

            finally:
                MailingAttempt.objects.create(
                    mailing=mailing,
                    status_mailing=status,
                    server_response=server_response,
                )


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, "interval", seconds=60)
    scheduler.start()
