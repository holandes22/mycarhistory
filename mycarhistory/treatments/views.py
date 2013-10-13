from rest_framework import viewsets, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from mycarhistory.cars.models import Car
from mycarhistory.treatments.models import Treatment
from mycarhistory.treatments.serializers import TreatmentSerializer

from mycarhistory.users.permissions import TreatmentOwnerPermission


class TreatmentByCarViewSet(viewsets.ModelViewSet):

    model = Treatment
    serializer_class = TreatmentSerializer
    permission_classes = (IsAuthenticated, TreatmentOwnerPermission)

    def check_ownership(self, car):
        if car.user != self.request.user:
            raise PermissionDenied()

    def get_car(self):
        return Car.objects.get(pk=self.kwargs['car_pk'])

    def get_queryset(self):
        car = self.get_car()
        self.check_ownership(car)
        return Treatment.objects.filter(car=car)

    def pre_save(self, obj):
        obj.car = self.get_car()
