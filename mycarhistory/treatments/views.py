from rest_framework import viewsets

from mycarhistory.cars.models import Car
from mycarhistory.treatments.models import Treatment
from mycarhistory.treatments.serializers import TreatmentSerializer


class TreatmentViewSet(viewsets.ModelViewSet):

    model = Treatment
    serializer_class = TreatmentSerializer


class TreatmentByCarViewSet(viewsets.ModelViewSet):

    model = Treatment
    serializer_class = TreatmentSerializer

    def get_car(self):
        return Car.objects.get(pk=self.kwargs['car_pk'])

    def get_queryset(self):
        return Treatment.objects.filter(car=self.get_car())

    def pre_save(self, obj):
        obj.car = self.get_car()
