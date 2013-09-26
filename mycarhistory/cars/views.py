from django.contrib.auth.models import User

from rest_framework import viewsets

from mycarhistory.cars.models import Car
from mycarhistory.cars.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarByUserViewSet(viewsets.ModelViewSet):

    model = Car
    serializer_class = CarSerializer

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['user_pk'])
        return Car.objects.filter(user=user)
