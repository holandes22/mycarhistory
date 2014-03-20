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
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))

    def test_list_returns_empty_list_if_no_treatments(self):
        car = CarFactory(user=self.user)
        response = self.client.get(
            reverse('treatment-list', kwargs={'car_pk': car.pk})
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(0, len(response.data))

    def test_list_shallow_filter_by_car_param(self):
        car1 = CarFactory(user=self.user)
        TreatmentFactory(car=car1)
        TreatmentFactory(car=car1)
        car2 = CarFactory(user=self.user)
        TreatmentFactory(car=car2)

        other_user = UserFactory(username='fake')
        other_car = CarFactory(user=other_user)
        other_treatment = TreatmentFactory(car=other_car)

        response = self.client.get(
            reverse('treatment-list-shallow'),
            data={'car': car1.pk},
        )

        self.assertEqual(2, len(response.data))
        ids = [_['id'] for _ in response.data]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(other_treatment.pk not in ids)

    def test_list_shallow_returns_empty_list_if_no_treatments(self):
        car = CarFactory(user=self.user)
        url = '{}?car={}'.format(reverse('treatment-list-shallow'), car.pk)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(0, len(response.data))

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

        url = reverse('treatment-list-shallow')
        response = self.client.get(url, data={'car': car2.pk})
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
            description='fake_description',
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
            'description': 'fake_description',
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
            description='fake_description',
            date=fake_date,
        )
        url = reverse('treatment-detail-shallow', kwargs={'pk': treatment.pk})
        response = self.client.get(url)
        expected = {
            'id': treatment.pk,
            'car': car.pk,
            'done_by': 'fake_done_by',
            'description': 'fake_description',
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

    def test_create_to_nested_endpoint_returns_405(self):
        # POST
        car = CarFactory(user=self.user)
        url = reverse('treatment-list', kwargs={'car_pk': car.pk})
        response = self.client.post(url, {})
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED,
            response.status_code
        )

    def test_create_shallow(self):
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
        url = reverse('treatment-list-shallow')
        response = self.client.post(url, payload)
        self.assertEqual(expected, response.data)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))
        self.assertEqual(expected, response.data[0])

        # Again
        expected = dict({'id': 2}, **payload)
        response = self.client.post(url, payload)
        self.assertEqual(expected, response.data)

    def test_create_shallow_disregards_query_param(self):
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
        url = '{}?car={}'.format(reverse('treatment-list-shallow'), car.pk)
        response = self.client.post(url, payload)
        self.assertEqual(expected, response.data)

        expected = dict({'id': 2}, **payload)
        url = '{}?car={}'.format(reverse('treatment-list-shallow'), '777')
        response = self.client.post(url, payload)
        self.assertEqual(expected, response.data)

    def test_create_shallow_returns_403_if_user_not_owner_of_car(self):
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
        url = reverse('treatment-list-shallow')
        response = self.client.post(url, payload)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_create_shallow_indicates_missing_or_null_fields(self):
        car = CarFactory(user=self.user)
        payload = {'car': car.pk, 'done_by': '""', 'description': ''}
        response = self.client.post(reverse('treatment-list-shallow'), payload)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertIn('kilometrage', response.data)
        self.assertIn('description', response.data)
        self.assertNotIn('done_by', response.data)

    def test_create_shallow_raises_error_with_bad_payload(self):
        car = CarFactory(user=self.user)
        payload = {
            'car': car.pk,
            'done_by': 'fake_done_by',
            'description': 'fake_description',
            'date': 'bad_formatted_date',
            'kilometrage': '1111.5',  # must be integer
        }
        response = self.client.post(
            reverse('treatment-list-shallow'),
            payload
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        expected = ['date', 'kilometrage']
        self.assertItemsEqual(expected, response.data.keys())

    def test_delete(self):
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        response = self.client.delete(
            reverse(
                'treatment-detail',
                kwargs={'car_pk': car.pk, 'pk': treatment.pk}
            )
        )
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_delete_shallow(self):
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        response = self.client.delete(
            reverse(
                'treatment-detail-shallow',
                kwargs={'pk': treatment.pk}
            )
        )
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_delete_returns_403_if_not_owner(self):
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        new_user = UserFactory(username='fake')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        response = self.client.delete(
            reverse(
                'treatment-detail',
                kwargs={'car_pk': car.pk, 'pk': treatment.pk},
            )
        )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_delete_shallow_returns_403_if_not_owner(self):
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        new_user = UserFactory(username='fake')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        response = self.client.delete(
            reverse(
                'treatment-detail-shallow',
                kwargs={'pk': treatment.pk},
            )
        )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_partial_update(self):
        # PATCH
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car, kilometrage=1)
        payload = {'kilometrage': 777}
        response = self.client.patch(
            reverse(
                'treatment-detail',
                kwargs={'car_pk': car.pk, 'pk': treatment.pk},
            ),
            payload,
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(777, response.data['kilometrage'])

    def test_partial_update_shallow(self):
        # PATCH
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car, kilometrage=1)
        payload = {'kilometrage': 777}
        response = self.client.patch(
            reverse(
                'treatment-detail-shallow',
                kwargs={'pk': treatment.pk},
            ),
            payload,
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(777, response.data['kilometrage'])

    def test_partial_update_returns_403_if_not_owner(self):
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        new_user = UserFactory(username='fake')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        payload = {'brand': 'fake_brand'}
        response = self.client.patch(
            reverse(
                'treatment-detail',
                kwargs={'car_pk': car.pk, 'pk': treatment.pk},
            ),
            payload,
        )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_partial_update_shallow_returns_403_if_not_owner(self):
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        new_user = UserFactory(username='fake')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        payload = {'brand': 'fake_brand'}
        response = self.client.patch(
            reverse(
                'treatment-detail-shallow',
                kwargs={'pk': treatment.pk},
            ),
            payload,
        )
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_head(self):
        pass

    def test_options(self):
        pass

    def test_update_treatment_detail(self):
        # PUT
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(
            car=car,
            done_by='not_fake',
            description='not_fake',
            kilometrage=11,
        )
        expected = 'fake'
        payload = {
            'done_by': expected,
            'description': expected,
            'kilometrage': 22,
        }
        response = self.client.put(
            reverse(
                'treatment-detail',
                kwargs={'car_pk': car.pk, 'pk': treatment.pk}
            ),
            payload,
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected, response.data['done_by'])
        self.assertEqual(expected, response.data['description'])
        self.assertEqual(22, response.data['kilometrage'])

    def test_update_treatment_detail_shallow(self):
        # PUT
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(
            car=car,
            done_by='not_fake',
            description='not_fake',
            kilometrage=11,
        )
        expected = 'fake'
        payload = {
            'car': car.pk,
            'done_by': expected,
            'description': expected,
            'kilometrage': 22,
        }
        response = self.client.put(
            reverse(
                'treatment-detail-shallow',
                kwargs={'pk': treatment.pk}
            ),
            payload,
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected, response.data['done_by'])
        self.assertEqual(expected, response.data['description'])
        self.assertEqual(22, response.data['kilometrage'])

    def test_update_treatment_detail_raises_400_if_missing_attrs(self):
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        expected = 'fake'
        payload = {
            'done_by': expected,
            'description': expected,
        }
        response = self.client.put(
            reverse(
                'treatment-detail',
                kwargs={'car_pk': car.pk, 'pk': treatment.pk}
            ),
            payload,
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertIn('kilometrage', response.data)

    def test_update_shallow_treatment_detail_raises_400_if_missing_attrs(self):
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        expected = 'fake'
        payload = {
            'car': car.pk,
            'done_by': expected,
            'description': expected,
        }
        response = self.client.put(
            reverse(
                'treatment-detail-shallow',
                kwargs={'pk': treatment.pk}
            ),
            payload,
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertIn('kilometrage', response.data)

    def test_update_detail_raises_404_if_no_such_car(self):
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        payload = {
            'done_by': 'fake',
            'description': 'fake',
            'kilometrage': 22,
        }
        response = self.client.put(
            reverse(
                'treatment-detail',
                kwargs={'car_pk': 777, 'pk': treatment.pk}),
            payload,
        )
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_update_detail_shallow_raises_400_if_no_such_car(self):
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        payload = {
            'car': 777,
            'done_by': 'fake',
            'description': 'fake',
            'kilometrage': 22,
        }
        response = self.client.put(
            reverse(
                'treatment-detail-shallow',
                kwargs={'pk': treatment.pk}),
            payload,
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertIn('car', response.data)

    def test_update_detail_raises_404_if_no_such_treatment(self):
        car = CarFactory(user=self.user)
        payload = {
            'done_by': 'fake',
            'description': 'fake',
            'kilometrage': 22,
        }
        response = self.client.put(
            reverse(
                'treatment-detail',
                kwargs={'car_pk': car.pk, 'pk': 777}),
            payload,
        )
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_update_detail_shallow_raises_404_if_no_such_treatment(self):
        car = CarFactory(user=self.user)
        payload = {
            'car': car.pk,
            'done_by': 'fake',
            'description': 'fake',
            'kilometrage': 22,
        }
        response = self.client.put(
            reverse(
                'treatment-detail-shallow',
                kwargs={'pk': 777}),
            payload,
        )
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_list_put_not_allowed(self):
        response = self.client.put(
            reverse('treatment-list', kwargs={'car_pk': 777})
        )
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED,
            response.status_code
        )

    def test_list_shallow_put_not_allowed(self):
        response = self.client.put(
            reverse('treatment-list-shallow')
        )
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED,
            response.status_code
        )

    def _test_detail_return_404_if_non_existing_car(self, method):
        methods = ['delete', 'get', 'patch']
        if method not in methods:
            raise Exception('HTTP Method not supported: {}'.format(method))
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        response = getattr(self.client, method)(
            reverse(
                'treatment-detail',
                kwargs={'car_pk': 777, 'pk': treatment.pk},
            )
        )
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def _test_detail_return_404_if_non_existing_treatment(self,
                                                          method,
                                                          shallow=False):
        methods = ['delete', 'get', 'patch']
        if method not in methods:
            raise Exception('HTTP Method not supported: {}'.format(method))
        car = CarFactory(user=self.user)
        if shallow:
            url = reverse('treatment-detail-shallow', kwargs={'pk': 777})
        else:
            url = reverse(
                'treatment-detail',
                kwargs={'car_pk': car.pk, 'pk': 777},
            )
        response = getattr(self.client, method)(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_detail_delete_return_404_if_non_existing_car(self):
        self._test_detail_return_404_if_non_existing_car('delete')

    def test_detail_get_return_404_if_non_existing_car(self):
        self._test_detail_return_404_if_non_existing_car('get')

    def test_detail_patch_return_404_if_non_existing_car(self):
        self._test_detail_return_404_if_non_existing_car('patch')

    def test_detail_delete_return_404_if_non_existing_treatment(self):
        self._test_detail_return_404_if_non_existing_treatment('delete')

    def test_detail_get_return_404_if_non_existing_treatment(self):
        self._test_detail_return_404_if_non_existing_treatment('get')

    def test_detail_patch_return_404_if_non_existing_treatment(self):
        self._test_detail_return_404_if_non_existing_treatment('patch')

    def test_detail_shallow_delete_return_404_if_non_existing_treatment(self):
        self._test_detail_return_404_if_non_existing_treatment(
            'delete', shallow=True
        )

    def test_detail_shallow_get_return_404_if_non_existing_treatment(self):
        self._test_detail_return_404_if_non_existing_treatment(
            'get', shallow=True
        )

    def test_detail_shallow_patch_return_404_if_non_existing_treatment(self):
        self._test_detail_return_404_if_non_existing_treatment(
            'patch', shallow=True
        )

    def _test_treatment_detail_return_403_if_not_owner(self,
                                                       method,
                                                       shallow=False):
        methods = ['delete', 'get', 'patch']
        if method not in methods:
            raise Exception('HTTP Method not supported: {}'.format(method))
        car = CarFactory(user=self.user)
        treatment = TreatmentFactory(car=car)
        new_user = UserFactory(username='fake')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(new_user.get_auth_token())
        )
        if shallow:
            url = reverse(
                'treatment-detail-shallow', kwargs={'pk': treatment.pk}
            )
        else:
            url = reverse(
                'treatment-detail',
                kwargs={'car_pk': car.pk, 'pk': treatment.pk}
            )
        response = getattr(self.client, method)(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_treatment_detail_delete_return_403_if_not_owner(self):
        self._test_treatment_detail_return_403_if_not_owner('delete')

    def test_treatment_detail_get_return_403_if_not_owner(self):
        self._test_treatment_detail_return_403_if_not_owner('get')

    def test_treatment_detail_patch_return_403_if_not_owner(self):
        self._test_treatment_detail_return_403_if_not_owner('patch')

    def test_treatment_detail_shallow_delete_return_403_if_not_owner(self):
        self._test_treatment_detail_return_403_if_not_owner(
            'delete', shallow=True
        )

    def test_treatment_detail_shallow_get_return_403_if_not_owner(self):
        self._test_treatment_detail_return_403_if_not_owner(
            'get', shallow=True
        )

    def test_treatment_detail_shallow_patch_return_403_if_not_owner(self):
        self._test_treatment_detail_return_403_if_not_owner(
            'patch', shallow=True
        )

    def test_treatment_detail_post_not_allowed(self):
        response = self.client.post(
            reverse('treatment-detail', kwargs={'car_pk': 777, 'pk': 777}),
            {},
        )
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED,
            response.status_code
        )

    def test_treatment_detail_shallow_post_not_allowed(self):
        response = self.client.post(
            reverse('treatment-detail-shallow', kwargs={'pk': 777}),
            {},
        )
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED,
            response.status_code
        )
