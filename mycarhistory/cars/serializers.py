from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import PrimaryKeyRelatedField

from mycarhistory.cars.models import Car
from mycarhistory.treatments.serializers import TreatmentSerializer


class CarSerializer(ModelSerializer):

    treatments = PrimaryKeyRelatedField(many=True)
    class Meta:
        model = Car
        read_only_fields = ('user',)
