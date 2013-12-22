from mock import patch

from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from django_browserid.base import BrowserIDException

from mycarhistory.users.factories import UserFactory


class AuthAPITests(APITestCase):

    def test_login_returns_400_if_no_assertion(self):
        response = self.client.post(reverse('login'), {})
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    @patch('mycarhistory.users.views.auth.authenticate')
    def test_login_returns_email_and_token_if_authenticated(self,
                                                            authenticate):
        with self.settings(PERSONA_AUDIENCES=('au1', 'au2')):
            user = UserFactory(email='fake_email')
            authenticate.return_value = user
            response = self.client.post(
                reverse('login'),
                data={'assertion': 'abc'},
                HTTP_REFERER='au1',
            )
            self.assertEqual(status.HTTP_200_OK, response.status_code)
            self.assertEqual(user.email, response.data['email'])
            self.assertEqual(user.get_auth_token(), response.data['token'])

    def test_login_returns_500_if_audience_is_missing_in_conf(self):
        response = self.client.post(reverse('login'), {'assertion': 'abc'})
        self.assertEqual(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            response.status_code,
        )
        self.assertIn('audience', response.data)

    @patch('mycarhistory.users.views.auth.authenticate')
    def test_login_returns_500_if_authentication_fails(self, authenticate):
        with self.settings(PERSONA_AUDIENCES=('fake_audience')):
            authenticate.side_effect = BrowserIDException('msg')
            response = self.client.post(
                reverse('login'),
                data={'assertion': 'abc'},
                HTTP_REFERER='fake_audience',
            )
            self.assertEqual(
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                response.status_code,
            )
            self.assertIn('Authentication failed', response.data)

    def _test_login_returns_405_if_method_not_allowed(self, method):
        func = getattr(self.client, method)
        response = func(reverse('login'))
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED,
            response.status_code
        )

    def test_login_returns_405_if_method_is_get(self):
        self._test_login_returns_405_if_method_not_allowed('get')

    def test_login_returns_405_if_method_is_patch(self):
        self._test_login_returns_405_if_method_not_allowed('patch')

    def test_login_returns_405_if_method_is_put(self):
        self._test_login_returns_405_if_method_not_allowed('put')

    def test_login_returns_405_if_method_is_delete(self):
        self._test_login_returns_405_if_method_not_allowed('delete')

    @patch('mycarhistory.users.views.auth.authenticate')
    def test_login_return_500_if_something_goes_wrong(self, authenticate):
        with self.settings(PERSONA_AUDIENCES=('fake_audience')):
            authenticate.side_effect = ValueError()
            response = self.client.post(
                reverse('login'),
                data={'assertion': 'abc'},
                HTTP_REFERER='fake_audience',
            )
            self.assertEqual(
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                response.status_code,
            )
            self.assertIn('unexpected', response.data)

    @patch('mycarhistory.users.views.auth.authenticate')
    def test_login_return_500_if_audience_not_is_authorized_list(self, authenticate):
        with self.settings(PERSONA_AUDIENCES=('audience1', 'audience2')):
            authenticate.side_effect = ValueError()
            response = self.client.post(
                reverse('login'),
                data={'assertion': 'abc'},
                HTTP_REFERER='malicious_audience',
            )
            self.assertEqual(
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                response.status_code,
            )
            self.assertIn('malicious_audience', response.data)

    @patch('mycarhistory.users.views.auth.authenticate')
    def test_login_audience_with_trailing_backslash(self, authenticate):
        with self.settings(PERSONA_AUDIENCES=('au1', 'au2')):
            user = UserFactory(email='fake_email')
            authenticate.return_value = user
            response = self.client.post(
                reverse('login'),
                data={'assertion': 'abc'},
                HTTP_REFERER='au1/',
            )
            self.assertEqual(status.HTTP_200_OK, response.status_code)
            self.assertEqual(user.email, response.data['email'])


class UserProfileTests(APITestCase):

    def test_get_returns_expected_details(self):
        # email, short_name, full_name
        pass

    def test_get_returns_currently_authenticated_user(self):
        pass

    def test_methods_returns_401_if_user_not_authenticated(self):
        pass

    def test_put_returns_405(self):
        pass

    def test_post_modifies_user(self):
        pass

    def test_patch_modifies_user_partially(self):
        pass

    def test_delete_removes_user_and_its_related_objects(self):
        # cars and treatments that belong to it should be removed
        pass
