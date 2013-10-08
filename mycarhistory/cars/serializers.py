from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from mycarhistory.cars.models import Car


class CarSerializer(HyperlinkedModelSerializer):

    user = HyperlinkedRelatedField(view_name='user-detail')
    treatments = HyperlinkedRelatedField(many=True, read_only=True, view_name='treatment-detail')

    class Meta:
        model = Car


class CarByUserSerializer(HyperlinkedModelSerializer):

    user = HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    treatments = HyperlinkedRelatedField(many=True, read_only=True, view_name='treatment-detail')

    class Meta:
        model = Car
