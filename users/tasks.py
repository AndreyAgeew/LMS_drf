from celery import shared_task
from datetime import timedelta

from celery.app import task
from django.utils import timezone

from users.models import User

from django.core.mail import send_mail

from lms_drf import settings
from course.models import Subscription, Course


@shared_task()
def user_activity_check():
    '''Периодическая задача - проверка активности пользователя (если нет активности 30 дней - блокировка)'''
    users = User.objects.all()
    for user in users:
        if user.last_login:
            if timezone.now() - user.last_login > timedelta(days=30):  # если не активен более 30 дней
                user.is_active = False  # деактивировать
                user.save()


@shared_task
def send_email_course_update(course_pk):
    subscribers = Subscription.objects.filter(course=course_pk)
    course = Course.objects.get(pk=course_pk)
    for subscriber in subscribers:
        send_mail(
            subject=f'Обновление курса {course}',
            message='В курсе появились новые материалы',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscriber.user.email],
            fail_silently=False
        )
