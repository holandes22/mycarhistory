from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from mycarhistory.treatments.models import Treatment


class TreatmentSerializer(HyperlinkedModelSerializer):

    cars = PrimaryKeyRelatedField(many=True, read_only=True) 

    class Meta:
        model = Treatment
