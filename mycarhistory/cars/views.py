from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from mycarhistory.cars.models import Car
from mycarhistory.users.models import User
from mycarhistory.cars.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):

    model = Car
    serializer_class = CarSerializer


class CarByUserListView(ListAPIView):

    model = Car
    serializer_class = CarSerializer

    def get_user(self):
        return User.objects.get(pk=self.kwargs['user_pk'])

    def get_queryset(self):
        return Car.objects.filter(user=self.get_user())
