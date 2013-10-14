import factory
from factory.django import DjangoModelFactory

from mycarhistory.cars.models import Car
from mycarhistory.users.tests.factories import UserFactory


class CarFactory(DjangoModelFactory):
    FACTORY_FOR = Car

    user = factory.SubFactory(UserFactory)
    brand = 'Bat'
    model = 'Mobile'
