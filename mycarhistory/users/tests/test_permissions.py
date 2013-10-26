import unittest
from mock import Mock

from mycarhistory.users.permissions import CarOwnerPermission
from mycarhistory.users.permissions import TreatmentOwnerPermission


class TestOwnerPermission(unittest.TestCase):

    def test_car_has_object_permission(self):
        car = Mock()
        user = Mock()
        request = Mock()
        request.user = user
        car.user = user
        permission = CarOwnerPermission()
        self.assertTrue(
            permission.has_object_permission(request, Mock(), car)
        )

    def test_treatment_has_object_permission(self):
        car = Mock()
        user = Mock()
        request = Mock()
        request.user = user
        car.user = user
        treatment = Mock()
        treatment.car = car
        permission = TreatmentOwnerPermission()
        self.assertTrue(
            permission.has_object_permission(request, Mock(), treatment)
        )
