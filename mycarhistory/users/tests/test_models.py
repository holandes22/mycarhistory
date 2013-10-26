from django.test import TestCase

from mycarhistory.users.factories import UserFactory
from rest_framework.authtoken.models import Token


class TestUserModel(TestCase):

    def test_get_full_name(self):
        # We test that default Django implementation
        # for fullname is overriden (fname + lname)
        fake_full_name = 'Jorge Lopez Vicario'
        user = UserFactory(
            first_name='Jorge',
            last_name='Lopez',
            full_name=fake_full_name,
        )
        self.assertEqual(
            fake_full_name,
            user.get_full_name(),
        )

    def test_get_auth_token_is_created_on_first_access(self):
        user = UserFactory()

        with self.assertRaises(Token.DoesNotExist):
            token = Token.objects.get(user=user)
        token = user.get_auth_token()
        self.assertEqual(
            token,
            Token.objects.get(user=user).key
        )
