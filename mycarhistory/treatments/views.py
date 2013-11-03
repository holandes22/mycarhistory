from django.http import Http404

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from mycarhistory.cars.models import Car
from mycarhistory.treatments.models import Treatment
from mycarhistory.treatments.serializers import TreatmentSerializer

from mycarhistory.users.permissions import TreatmentOwnerPermission


class TreatmentOwnerMixin(object):

    def check_ownership(self, car):
        if car.user != self.request.user:
            raise PermissionDenied()

    def pre_save(self, obj):
        obj.car = self.get_car()


class TreatmentByCarViewSet(TreatmentOwnerMixin, ModelViewSet):

    def get_car(self):
        return Car.objects.get(pk=self.kwargs['car_pk'])

    def get_queryset(self):
        car = self.get_car()
        self.check_ownership(car)
        return Treatment.objects.filter(car=car)

    model = Treatment
    serializer_class = TreatmentSerializer
    permission_classes = (IsAuthenticated, TreatmentOwnerPermission)


class TreatmentListCreateAPIView(TreatmentOwnerMixin, ListCreateAPIView):

    model = Treatment
    serializer_class = TreatmentSerializer
    filter_fields = ['car']

    def get_car(self):
        car_pk = self.request.QUERY_PARAMS.get('car', None)
        if car_pk:
            return Car.objects.get(pk=car_pk)
        return None

    def get_queryset(self):
        car = self.get_car()
        if car:
            self.check_ownership(car)
            return Treatment.objects.filter(car=car)
        return Treatment.objects.filter(car__user=self.request.user)


class TreatmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    model = Treatment
    serializer_class = TreatmentSerializer
    permission_classes = (IsAuthenticated, TreatmentOwnerPermission)

