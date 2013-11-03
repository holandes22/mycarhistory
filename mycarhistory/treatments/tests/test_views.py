import datetime

from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from mycarhistory.users.factories import UserFactory
from mycarhistory.cars.factories import CarFactory
from mycarhistory.treatments.factories import TreatmentFactory


class TreatmentViewTests(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(self.user.get_auth_token())
        )

    def test_list(self):
        car = CarFactory(user=self.user)
        TreatmentFactory(car=car)
        TreatmentFactory(car=car)
        response = self.client.get(
            reverse('treatment-list', kwargs={'car_pk': car.pk})
        )
        self.assertEqual(2, len(response.data))

    def test_list_shallow_filter_by_car_param(self):
        car1 = CarFactory(user=self.user)
        TreatmentFactory(car=car1)
        TreatmentFactory(car=car1)
        car2 = CarFactory(user=self.user)
        TreatmentFactory(car=car2)

        other_user = UserFactory(username='fake')
        other_car = CarFactory(user=other_user)
        other_treatment = TreatmentFactory(car=other_car)

        url = '{}?car={}'.format(reverse('treatment-list-shallow'), car1.pk)
        response = self.client.get(url)
        self.assertEqual(2, len(response.data))
        ids = [_['id'] for _ in response.data]
        self.assertTrue(other_treatment.pk not in ids)

    def test_list_shallow_returns_all_owner_treatments_if_no_car_filter(self):
        car1 = CarFactory(user=self.user)
        t1 = TreatmentFactory(car=car1)
        t2 = TreatmentFactory(car=car1)
        car2 = CarFactory(user=self.user)
        t3 = TreatmentFactory(car=car2)

        other_user = UserFactory(username='fake')
        other_car = CarFactory(user=other_user)
        TreatmentFactory(car=other_car)

        response = self.client.get(reverse('treatment-list-shallow'))
        self.assertEqual(3, len(response.data))
        ids = [_['id'] for _ in response.data]
        expected = [t1.pk, t2.pk, t3.pk]
        self.assertItemsEqual(expected, ids)

    def test_list_only_for_specified_car(self):
        car1 = CarFactory(user=self.user)
        TreatmentFactory(car=car1)
        new_user = UserFactory(username='fake')
        car2 = CarFactory(user=new_user)
        TreatmentFactory(car=car2)

        response = self.client.get(
            reverse('treatment-list', kwargs={'car_pk': car1.pk})
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))

    def test_list_returns_403_if_user_is_not_the_car_owner(self):
        car1 = CarFactory(user=self.user)
        TreatmentFactory(car=car1)
        new_user = UserFactory(username='fake')
        car2 = CarFactory(user=new_user)
        TreatmentFactory(car=car2)

        response = self.client.get(
            reverse('treatment-list', kwargs={'car_pk': car2.pk})
        )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_list_shallow_only_for_specified_car(self):
        car1 = CarFactory(user=self.user)
        treatment1 = TreatmentFactory(car=car1, done_by='faker')
        new_user = UserFactory(username='fake')
        car2 = CarFactory(user=new_user)
        TreatmentFactory(car=car2)

        url = '{}?car={}'.format(reverse('treatment-list-shallow'), car1.pk)
        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))
        self.assertEqual(treatment1.done_by, response.data[0]['done_by'])

    def test_list_shallow_returns_403_if_user_is_not_the_car_owner(self):
        car1 = CarFactory(user=self.user)
        TreatmentFactory(car=car1, done_by='faker')
        new_user = UserFactory(username='fake')
        car2 = CarFactory(user=new_user)
        TreatmentFactory(car=car2)

        url = '{}?car={}'.format(reverse('treatment-list-shallow'), car2.pk)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_list_returns_401_if_not_authenticated(self):
        car = CarFactory()
        self.client.credentials()
        response = self.client.get(
            reverse('treatment-list', kwargs={'car_pk': car.pk})
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_list_shallow_returns_401_if_not_authenticated(self):
        car = CarFactory()
        self.client.credentials()
        url = '{}?car={}'.format(reverse('treatment-list-shallow'), car.pk)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_list_returns_401_if_invalid_token(self):
        car = CarFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token bad_token')
        response = self.client.get(
            reverse('treatment-list', kwargs={'car_pk': car.pk})
        )
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_list_shallow_returns_401_if_invalid_token(self):
        car = CarFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Token bad_token')
        url = '{}?car={}'.format(reverse('treatment-list-shallow'), car.pk)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_detail(self):
        car = CarFactory(user=self.user)
        fake_date = datetime.date(2000, 1, 1)
        treatment = TreatmentFactory(
            car=car,
            done_by='fake_done_by',
            date=fake_date,
        )
        response = self.client.get(
            reverse(
                'treatment-detail',
                kwargs={'car_pk': car.pk, 'pk': treatment.pk},
            )
        )
        expected = {
            'id': treatment.pk,
            'car': car.pk,
            'done_by': 'fake_done_by',
            'description': '',
            'date': fake_date,
            'kilometrage': 1,
            'reason': 1,
            'category': 1,
            'parts_replaced': 'None',
        }
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertDictEqual(expected, response.data)

    def test_detail_shallow(self):
        car = CarFactory(user=self.user)
        fake_date = datetime.date(2000, 1, 1)
        treatment = TreatmentFactory(
            car=car,
            done_by='fake_done_by',
            date=fake_date,
        )
        url = reverse('treatment-detail-shallow', kwargs={'pk': treatment.pk})
        response = self.client.get(url)
        expected = {
            'id': treatment.pk,
            'car': car.pk,
            'done_by': 'fake_done_by',
            'description': '',
            'date': fake_date,
            'kilometrage': 1,
            'reason': 1,
            'category': 1,
            'parts_replaced': 'None',
        }
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertDictEqual(expected, response.data)

    def test_detail_returns_403_if_user_not_owner(self):
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        url = reverse(
            'treatment-detail',
            kwargs={'car_pk': car.pk, 'pk': treatment.pk}
        )
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        new_user = UserFactory(username='fakeo')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        response = self.client.get(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_detail_shallow_returns_403_if_user_not_owner(self):
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        url = reverse(
            'treatment-detail-shallow',
            kwargs={'pk': treatment.pk}
        )
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        new_user = UserFactory(username='fake_shallow')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        response = self.client.get(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_create(self):
        # POST
        car = CarFactory(user=self.user)
        fake_date = datetime.date(2000, 1, 1)
        payload = {
            'car': car.pk,
            'done_by': 'fake_done_by',
            'description': 'fake_description',
            'date': fake_date,
            'kilometrage': 10,
            'reason': 1,
            'category': 1,
            'parts_replaced': 'part1,part2',
        }
        expected = dict({'id': 1}, **payload)
        url = reverse('treatment-list', kwargs={'car_pk': car.pk})
        response = self.client.post(url, payload)
        self.assertEqual(expected, response.data)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))
        self.assertEqual(expected, response.data[0])

    def test_create_returns_403_if_user_not_owner_of_car(self):
        car = CarFactory(user=self.user)
        fake_date = datetime.date(2000, 1, 1)
        payload = {
            'car': car.pk,
            'done_by': 'fake_done_by',
            'description': 'fake_description',
            'date': fake_date,
            'kilometrage': 10,
            'reason': 1,
            'category': 1,
            'parts_replaced': 'part1,part2',
        }
        new_user = UserFactory(username='fake_username')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        url = reverse('treatment-list', kwargs={'car_pk': car.pk})
        response = self.client.post(url, payload)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def _test_create_indicates_missing_fields(self):
        payload = {'brand': 'fake_brand'}  # model is missing
        response = self.client.post(reverse('car-list'), payload)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertIn('model', response.data)

    def _test_create_raises_error_with_bad_payload(self):
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

    def _test_delete(self):
        # DELETE
        car = CarFactory(user=self.user)
        response = self.client.delete(
            reverse('car-detail', kwargs={'pk': car.pk})
        )
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def _test_delete_returns_404_if_not_owner(self):
        car = CarFactory(user=self.user)
        new_user = UserFactory(username='fake')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        response = self.client.delete(
            reverse('car-detail', kwargs={'pk': car.pk})
        )
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def _test_partial_update(self):
        # PATCH
        car = CarFactory(user=self.user)
        payload = {'brand': 'fake_brand'}
        response = self.client.patch(
            reverse('car-detail', kwargs={'pk': car.pk}),
            payload,
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual('fake_brand', response.data['brand'])

    def _test_partial_update_returns_404_if_not_owner(self):
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
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_head(self):
        pass

    def test_options(self):
        pass

    def _test_car_detail_methods_return_404_for_non_existing_car(self):
        methods = ['delete', 'get', 'put', 'patch']
        for method in methods:
            response = getattr(self.client, method)(
                reverse('car-detail', kwargs={'pk': 777})
            )
            self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def _test_car_detail_methods_return_404_if_not_owner(self):
        methods = ['delete', 'get', 'put', 'patch']
        car = CarFactory(user=self.user)
        new_user = UserFactory(username='fake')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        for method in methods:
            response = getattr(self.client, method)(
                reverse('car-detail', kwargs={'pk': car.pk})
            )
            self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def _test_car_detail_post_not_allowed(self):
        response = self.client.post(
            reverse('car-detail', kwargs={'pk': 777})
        )
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED,
            response.status_code
        )

    def _test_put_not_allowed_for_car_list(self):
        response = self.client.put(reverse('car-list'))
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED,
            response.status_code
        )
