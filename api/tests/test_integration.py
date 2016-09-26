from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from api.models import Cat


class IntegrationTests(TestCase):
    ADMIN_PASSWORD = 'kjsbdkfcsbnedfkd'

    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', self.ADMIN_PASSWORD)

    @staticmethod
    def get_token(username, password):
        user = authenticate(username=username, password=password)
        payload = jwt_payload_handler(user)
        return jwt_encode_handler(payload)

    def test_adding_cat_without_token(self):
        response = self.client.post(reverse('cat-list'), {'url': 'http://example.com/kitty.jpg'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(len(Cat.objects.all()), 0)

    def test_adding_cat_with_valid_token(self):
        token = self.get_token(self.superuser.username, self.ADMIN_PASSWORD)
        response = self.client.post(reverse('cat-list'), {'url': 'http://example.com/kitty.jpg'},
                                    HTTP_AUTHORIZATION='Bearer ' + token)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(Cat.objects.all()), 1)
        created = Cat.objects.first()
        self.assertEqual(created.creator, self.superuser.username)

    def test_adding_cat_with_invalid_token(self):
        token = self.get_token(self.superuser.username, self.ADMIN_PASSWORD) + 'a'
        response = self.client.post(reverse('cat-list'), {'url': 'http://example.com/kitty.jpg'},
                                    HTTP_AUTHORIZATION='Bearer ' + token)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(len(Cat.objects.all()), 0)
