from rest_framework import viewsets

from mycarhistory.cars.models import Car
from mycarhistory.cars.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
