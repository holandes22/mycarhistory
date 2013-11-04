from django.shortcuts import get_object_or_404

from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import ListCreateAPIView
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


class TreatmentListByCarAPIView(TreatmentAPIViewMixin, ListCreateAPIView):

    car = None
    model = Treatment
    serializer_class = TreatmentByCarSerializer
    permission_classes = (IsAuthenticated, CarOwnerPermission)

    def get_car(self):
        if not self.car:
            self.car = get_object_or_404(Car, pk=self.kwargs['car_pk'])
        self.check_object_permissions(self.request, self.car)
        return self.car

    def get_queryset(self):
        return Treatment.objects.filter(car=self.get_car())


class TreatmentDetailByCarAPIView():
    pass


class TreatmentListAPIView(TreatmentAPIViewMixin, ListCreateAPIView):

    model = Treatment
    serializer_class = TreatmentSerializer
    permission_classes = (IsAuthenticated, CarOwnerPermission)
    filter_fields = ['car']
    car = None

    def get_car(self):
        car_pk = self.request.POST.get('car', None)
        if not car_pk:
            car_pk = self.request.QUERY_PARAMS.get('car', None)
        if car_pk:
            self.car = get_object_or_404(Car, pk=car_pk)
            self.check_object_permissions(self.request, self.car)
        return self.car

    def get_queryset(self):
        car = self.get_car()
        if car:
            return Treatment.objects.filter(car=car)
        return Treatment.objects.filter(car__user=self.request.user)


class TreatmentDetailAPIView(RetrieveUpdateDestroyAPIView):

    model = Treatment
    serializer_class = TreatmentSerializer
    permission_classes = (IsAuthenticated, TreatmentOwnerPermission)

    def put(self, *args, **kwargs):
        raise MethodNotAllowed(method='PUT')
