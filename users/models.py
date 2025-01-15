from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    class Meta:
        verbose_name = 'Верификация'
        verbose_name_plural = 'Верификация'

    def __str__(self):
        return f'Подтверждение регистрации для {self.user.username}'

    def send_verification_email(self):
        link = reverse('users:verify', kwargs={
            'email': self.user.email,
            'code': self.code,
        })
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение учётной записи для {self.user.username}'
        message = f'Ссылка {verification_link}'
        send_mail(
            subject=subject,
            message=message,
            from_email='from@example.com',
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False
