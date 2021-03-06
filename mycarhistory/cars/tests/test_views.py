import datetime

from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from mycarhistory.cars.models import Car
from mycarhistory.users.factories import UserFactory
from mycarhistory.cars.factories import CarFactory
from mycarhistory.treatments.factories import TreatmentFactory


class CarViewTests(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(self.user.get_auth_token())
        )

    def test_list(self):
        CarFactory(user=self.user)
        CarFactory(user=self.user)
        response = self.client.get(reverse('car-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))

    def test_list_returns_empty_list_if_no_cars(self):
        response = self.client.get(reverse('car-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(0, len(response.data))

    def test_list_only_authenticated_user(self):
        CarFactory(user=self.user)
        new_user = UserFactory(username='fake')
        CarFactory(user=new_user)
        response = self.client.get(reverse('car-list'))
        self.assertEqual(1, len(response.data))

    def test_list_user_returns_401_if_not_authenticated(self):
        # NotAuthenticated
        self.client.credentials()
        response = self.client.get(reverse('car-list'))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_list_user_returns_401_if_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token bad_token')
        response = self.client.get(reverse('car-list'))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_detail(self):
        car = CarFactory(
            user=self.user,
            brand='fake_brand',
            model='fake_model',
            year='2000',
        )
        response = self.client.get(
            reverse('car-detail', kwargs={'pk': car.pk})
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        expected = {
            'user': self.user.pk,
            'id': car.pk,
            'treatments': [],
            'brand': 'fake_brand',
            'model': 'fake_model',
            'year': 2000,
            'gearbox_type': Car.GEARBOX_AUTOMATIC,
            'amount_of_owners': 1,
        }
        self.assertDictEqual(expected, response.data)

    def test_detail_car_treatments_is_a_string_of_ids(self):
        car = CarFactory(user=self.user)
        treatment1 = TreatmentFactory(car=car)
        treatment2 = TreatmentFactory(car=car)

        expected = [treatment1.pk, treatment2.pk]

        response = self.client.get(
            reverse('car-detail', kwargs={'pk': car.pk})
        )
        self.assertListEqual(expected, response.data['treatments'])

    def test_detail_returns_403_if_user_not_owner(self):
        car = CarFactory(user=self.user)
        response = self.client.get(
            reverse('car-detail', kwargs={'pk': car.pk})
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        new_user = UserFactory(username='fake')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        response = self.client.get(
            reverse('car-detail', kwargs={'pk': car.pk})
        )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_create(self):
        # POST
        payload = {
            'brand': 'fake_brand',
            'model': 'fake_model',
            'year': 2000,
            'gearbox_type': Car.GEARBOX_MANUAL,
            'amount_of_owners': 3,
        }
        expected = dict(
            {'user': self.user.pk, 'id': 1, 'treatments': []},
            **payload
        )
        response = self.client.post(reverse('car-list'), payload)
        self.assertEqual(expected, response.data)
        response = self.client.get(reverse('car-list'))
        self.assertEqual(1, len(response.data))
        self.assertEqual(expected, response.data[0])

    def test_create_indicates_missing_fields(self):
        payload = {'brand': 'fake_brand'}  # model is missing
        response = self.client.post(reverse('car-list'), payload)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertIn('model', response.data)

    def test_create_raises_error_with_bad_payload(self):
        payload = {
            'brand': 'fake_brand',
            'model': 'fake_model',
            'year': 'bad_formatted_date',
            'gearbox_type': 'bad_selection',
            'amount_of_owners': 'bad_type',
        }
        response = self.client.post(reverse('car-list'), payload)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        expected = ['year', 'gearbox_type', 'amount_of_owners']
        self.assertItemsEqual(expected, response.data.keys())

    def test_delete(self):
        # DELETE
        car = CarFactory(user=self.user)
        response = self.client.delete(
            reverse('car-detail', kwargs={'pk': car.pk})
        )
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_delete_returns_403_if_not_owner(self):
        car = CarFactory(user=self.user)
        new_user = UserFactory(username='fake')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        response = self.client.delete(
            reverse('car-detail', kwargs={'pk': car.pk})
        )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_partial_update(self):
        # PATCH
        car = CarFactory(user=self.user)
        payload = {'brand': 'fake_brand'}
        response = self.client.patch(
            reverse('car-detail', kwargs={'pk': car.pk}),
            payload,
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('fake_brand', response.data['brand'])

    def test_partial_update_returns_403_if_not_owner(self):
        car = CarFactory(user=self.user)
        new_user = UserFactory(username='fake')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        payload = {'brand': 'fake_brand'}
        response = self.client.patch(
            reverse('car-detail', kwargs={'pk': car.pk}),
            payload,
        )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_head(self):
        pass

    def test_options(self):
        pass

    def test_car_detail_methods_return_404_for_non_existing_car(self):
        methods = ['delete', 'get', 'patch']
        for method in methods:
            response = getattr(self.client, method)(
                reverse('car-detail', kwargs={'pk': 777})
            )
            self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_car_detail_methods_return_403_if_not_owner(self):
        methods = ['delete', 'get', 'patch']
        car = CarFactory(user=self.user)
        new_user = UserFactory(username='fake')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        for method in methods:
            response = getattr(self.client, method)(
                reverse('car-detail', kwargs={'pk': car.pk})
            )
            self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_car_detail_post_not_allowed(self):
        response = self.client.post(
            reverse('car-detail', kwargs={'pk': 777})
        )
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED,
            response.status_code
        )

    def test_put_not_allowed_for_car_list(self):
        response = self.client.put(reverse('car-list'))
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED,
            response.status_code
        )

    def test_update_car_detail(self):
        # PUT
        car = CarFactory(
            user=self.user,
            brand='not_fake',
            model='not_fake',
            )
        expected = 'fake'
        payload = {'brand': expected, 'model': expected}
        response = self.client.put(
            reverse('car-detail', kwargs={'pk': car.pk}),
            payload,
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected, response.data['brand'])
        self.assertEqual(expected, response.data['model'])

    def test_update_car_detail_raises_400_if_missing_attrs(self):
        car = CarFactory(user=self.user)
        payload = {'brand': 'fake'}  # Missing model
        response = self.client.put(
            reverse('car-detail', kwargs={'pk': car.pk}),
            payload,
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertIn('model', response.data)

    def test_update_car_detail_raises_404_if_non_existent_car(self):
        payload = {'brand': 'fake', 'model': 'fake'}
        response = self.client.put(
            reverse('car-detail', kwargs={'pk': 777}),
            payload,
        )
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
