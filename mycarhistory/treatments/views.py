from rest_framework import viewsets

from mycarhistory.treatments.models import Treatment
from mycarhistory.treatments.serializers import TreatmentSerializer

class TreatmentViewSet(viewsets.ModelViewSet):

    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
