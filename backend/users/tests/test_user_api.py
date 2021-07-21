from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .factories import UserFactory

OBTAIN_TOKEN_URL = reverse('users:token_obtain')
REFRESH_TOKEN_URL = reverse('users:token_refresh')
CREATE_USER_URL = reverse('users:create')


class UserApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()

    def test_obtain_token_success(self):
        payload = {
            'username': self.user.username,
            'password': '1234'
        }
        response = self.client.post(OBTAIN_TOKEN_URL, payload)

        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_obtain_token_without_password(self):
        payload = {
            'username': self.user.username,
        }
        response = self.client.post(OBTAIN_TOKEN_URL, payload)

        self.assertNotIn('access', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_obtain_refresh_token_success(self):
        payload = {
            'username': self.user.username,
            'password': '1234'
        }
        response = self.client.post(OBTAIN_TOKEN_URL, payload)

        response_refresh = self.client.post(REFRESH_TOKEN_URL, {
            'refresh': response.data['refresh']
        })

        self.assertIn('access', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_obtain_refresh_token_wrong_refresh_token(self):
        response = self.client.post(REFRESH_TOKEN_URL, {
            'refresh': 'wronggg'
        })

        self.assertNotIn('access', response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_create_success(self):
        payload = {
            'username': 'testuser',
            'password': 'superstrong'
        }

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_create_empty_password(self):
        payload = {
            'username': 'testuser'
        }

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
