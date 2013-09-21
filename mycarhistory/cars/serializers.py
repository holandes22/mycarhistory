from rest_framework.serializers import HyperlinkedModelSerializer

from mycarhistory.cars.models import Car


class CarSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Car
        fields = ('url', 'name', 'description', 'data_type', 'data')
