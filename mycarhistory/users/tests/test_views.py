from contextlib import contextmanager

from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from mycarhistory.users.factories import UserFactory


@contextmanager
def credentials(client, user):
        client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(user.get_auth_token())
        )
        yield
        client.credentials()


class CarViewTests(APITestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_get_auth_token_returns_200_if_authenticated(self):
        with credentials(self.client, self.user):
            response = self.client.get(reverse('get-auth-token'))
            self.assertEqual(status.HTTP_200_OK, response.status_code)
            self.assertEqual(self.user.get_auth_token(), response.data)

    def test_get_auth_token_returns_401_if_not_authenticated(self):
        response = self.client.get(reverse('get-auth-token'))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_get_auth_token_raises_405_if_method_is_not_get(self):
        methods = ['post', 'put', 'patch', 'delete']
        with credentials(self.client, self.user):
            for method in methods:
                func = getattr(self.client, method)
                response = func(reverse('get-auth-token'))
                self.assertEqual(
                    status.HTTP_405_METHOD_NOT_ALLOWED,
                    response.status_code
                )
