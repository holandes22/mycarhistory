from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from mycarhistory.users.factories import UserFactory
from mycarhistory.cars.factories import CarFactory


class CarTests(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)

    def test_list(self):
        car1 = CarFactory(user=self.user)
        car2 = CarFactory(user=self.user)
        response = self.client.get(reverse('car-list'))
        self.assertTrue(response.data['count'] == 2)
    
    def test_list_only_authenticated_user(self):
        car1 = CarFactory(user=self.user)
        car2 = CarFactory(user=self.user)
        new_user = UserFactory(username='fake')
        car3 = CarFactory(user=new_user)
        response = self.client.get(reverse('car-list'))
        self.assertTrue(response.data['count'] == 2)

    def test_list_user_not_authenticated(self):
        # NotAuthenticated
        pass

    def test_list_user_with_bad_credentials(self):
        # PermissionDenied
        pass

    def test_detail(self):
        pass

    def test_create(self):
        pass

    def test_delete(self):
        pass
    
    def test_update(self):
        pass


