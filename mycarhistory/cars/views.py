from django.http import Http404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import MethodNotAllowed

from mycarhistory.cars.models import Car
from mycarhistory.cars.serializers import CarSerializer

from mycarhistory.users.permissions import CarOwnerPermission


class CarByUserViewSet(viewsets.ModelViewSet):

    model = Car
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated, CarOwnerPermission)

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)

    def pre_save(self, obj):
        obj.user = self.request.user

    def get_object_or_none(self):
        # Override DRF implementation to avoid PUT as create on object
        return self.get_object()
