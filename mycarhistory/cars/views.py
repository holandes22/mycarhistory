from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from mycarhistory.cars.models import Car
from mycarhistory.cars.serializers import CarSerializer

from mycarhistory.users.permissions import CarOwnerPermission


class CarAPIViewMixin(object):

    def pre_save(self, obj):
        obj.user = self.request.user


class CarListAPIView(CarAPIViewMixin, ListCreateAPIView):

    model = Car
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)


class CarDetailAPIView(CarAPIViewMixin, RetrieveUpdateDestroyAPIView):

    model = Car
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated, CarOwnerPermission)

    def put(self, *args, **kwargs):
        self.get_object()  # Will raise 404 if doesn't exist
        return super(CarDetailAPIView, self).put(*args, **kwargs)
