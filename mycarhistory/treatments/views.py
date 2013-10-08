from rest_framework import viewsets

from mycarhistory.treatments.models import Treatment
from mycarhistory.treatments.serializers import TreatmentSerializer, TreatmentByCarSerializer

class TreatmentViewSet(viewsets.ModelViewSet):

    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class TreatmentByCarViewSet(viewsets.ModelViewSet):

    model = Treatment
    serializer_class = TreatmentByCarSerializer

    def get_queryset(self):
        car = Treatment.objects.get(car=self.kwargs['car_pk'])
        return Treatment.objects.filter(car=car)

    def pre_save(self, obj):
        obj.car = Treatment.objects.get(car=self.kwargs['car_pk'])
