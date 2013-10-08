from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from mycarhistory.treatments.models import Treatment


class TreatmentSerializer(HyperlinkedModelSerializer):

    car = HyperlinkedRelatedField(view_name='car-detail')

    class Meta:
        model = Treatment


class TreatmentByCarSerializer(HyperlinkedModelSerializer):

    car = HyperlinkedRelatedField(read_only=True, view_name='car-detail')

    class Meta:
        model = Treatment
