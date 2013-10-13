from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from mycarhistory.cars.models import Car
from mycarhistory.users.models import User
from mycarhistory.cars.serializers import CarSerializer

from mycarhistory.users.permissions import CarOwnerPermission


class CarByUserViewSet(viewsets.ModelViewSet):

    model = Car
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated, CarOwnerPermission)

    def check_ownership(self, user):
        if user != self.request.user:
            raise PermissionDenied()

    def get_user(self):
        return User.objects.get(pk=self.kwargs['user_pk'])

    def get_queryset(self):
        user = self.get_user()
        self.check_ownership(user)
        return Car.objects.filter(user=user)

    def pre_save(self, obj):
        obj.user = self.get_user()
