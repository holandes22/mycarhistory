from django.shortcuts import get_object_or_404

from rest_framework.exceptions import MethodNotAllowed, PermissionDenied
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from mycarhistory.cars.models import Car
from mycarhistory.treatments.models import Treatment
from mycarhistory.treatments.serializers import TreatmentSerializer
from mycarhistory.treatments.serializers import TreatmentByCarSerializer

from mycarhistory.users.permissions import TreatmentOwnerPermission
from mycarhistory.users.permissions import CarOwnerPermission


class TreatmentAPIViewMixin(object):

    def pre_save(self, obj):
        obj.car = self.get_car()


class TreatmentDetailAPIViewMixin(object):

    def put(self, *args, **kwargs):
        self.get_object()
        return super(TreatmentDetailAPIViewMixin, self).put(*args, **kwargs)


class TreatmentListByCarAPIView(TreatmentAPIViewMixin, ListAPIView):

    model = Treatment
    serializer_class = TreatmentByCarSerializer
    permission_classes = (IsAuthenticated, CarOwnerPermission)
    car = None

    def get_car(self):
        if not self.car:
            self.car = get_object_or_404(Car, pk=self.kwargs['car_pk'])
        self.check_object_permissions(self.request, self.car)
        return self.car

    def get_queryset(self):
        return Treatment.objects.filter(car=self.get_car())


class TreatmentDetailByCarAPIView(TreatmentAPIViewMixin,
                                  TreatmentDetailAPIViewMixin,
                                  RetrieveUpdateDestroyAPIView):

    model = Treatment
    permission_classes = (IsAuthenticated, TreatmentOwnerPermission)
    serializer_class = TreatmentByCarSerializer
    car = None

    def get_car(self):
        if not self.car:
            self.car = get_object_or_404(Car, pk=self.kwargs['car_pk'])
        if self.car.user != self.request.user:
            raise PermissionDenied()
        return self.car

    def get_object(self):
        car = self.get_car()
        pk = self.kwargs['pk']
        treatment = get_object_or_404(self.model, pk=pk, car=car)
        self.check_object_permissions(self.request, treatment)
        return treatment


class TreatmentListAPIView(TreatmentAPIViewMixin, ListCreateAPIView):

    model = Treatment
    serializer_class = TreatmentSerializer
    permission_classes = (IsAuthenticated, CarOwnerPermission)
    filter_fields = ['car']
    car = None

    def get_car(self):
        car_pk = None
        for attr in ['DATA', 'QUERY_PARAMS', 'POST']:
            car_pk = getattr(self.request, attr).get('car', None)
            if car_pk:
                self.car = get_object_or_404(Car, pk=car_pk)
                self.check_object_permissions(self.request, self.car)
                return self.car
        return None

    def get_queryset(self):
        car = self.get_car()
        if car:
            return Treatment.objects.filter(car=car)
        return Treatment.objects.filter(car__user=self.request.user)


class TreatmentDetailAPIView(TreatmentDetailAPIViewMixin,
                             RetrieveUpdateDestroyAPIView):

    model = Treatment
    permission_classes = (IsAuthenticated, TreatmentOwnerPermission)
    serializer_class = TreatmentSerializer
