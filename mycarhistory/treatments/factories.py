import factory
from factory.django import DjangoModelFactory

from mycarhistory.treatments.models import Treatment
from mycarhistory.cars.factories import CarFactory


class TreatmentFactory(DjangoModelFactory):
    FACTORY_FOR = Treatment

    car = factory.SubFactory(CarFactory)
    kilometrage = 1

