from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.test import (
    APITestCase,
    APIClient,
)
from auths.models import CustomUser
# from django.urls import reverse
# from django.contrib.auth import get_user_model


class CabinetViewSetTest(APITestCase):
    """CabinetViewSetTest."""

    def setUp(self):
        self.url = 'http://localhost:8000/api/v1/cabinet'
        self.auth_url = 'http://localhost:8000/api/token/'

    def test_cabinet_list(self):

        # Генерируем юзера для БД-теста
        #
        test_user = CustomUser.objects.create_user(
            email='rustem-k@mail.ru',
            password='As123456!'
        )
        test_user.is_active = True
        test_user.save()

        # Отправляем запрос на авторизацию JWT
        #
        response = self.client.post(
            self.auth_url,
            {
                'email': 'rustem-k@mail.ru',
                'password': 'As123456!'
            },
            format='json'
        )
        self.assertTrue('access' in response.data)

        token = response.data['access']

        self.assertEqual(len(token), 228)

        # Отправляем запрос на метод - LIST
        #
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {token}')

        response = self.client.get(self.url, data={'format': 'json'})

        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_cabinet_list_inactive_user(self):

        # Генерируем юзера для БД-теста
        #
        test_user = CustomUser.objects.create_user(
            email='user@foo.com',
            password='299792458'
        )
        test_user.is_active = False
        test_user.save()

        # Отправляем запрос на авторизацию JWT
        #
        response = self.client.post(
            self.auth_url,
            {
                'email': 'user@foo.com',
                'password': '299792458'
            },
            format='json'
        )
        self.assertFalse('access' in response.data)
