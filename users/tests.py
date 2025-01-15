from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import EmailVerification, User


class UserRegistrationViewTestCase(TestCase):

    def setUp(self) -> None:
        self.path = reverse('users:registration')
        self.data = {
            'first_name': 'Андрей',
            'last_name': 'Семкин',
            'username': 'puhsem',
            'email': 'puhsem@ro.ru',
            'password1': 'QazxcvB123',
            'password2': 'QazxcvB123',
        }
        self.username = self.data['username']

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_post_success(self):
        email = EmailVerification.objects.filter(user__username=self.username)
        self.assertFalse(User.objects.filter(username=self.username).exists())
        self.assertFalse(email.exists())

        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=self.username).exists())
        self.assertTrue(email.exists())

    def test_user_registration_post_error(self):
        User.objects.create(username=self.username)

        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)
