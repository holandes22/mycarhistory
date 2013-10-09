from rest_framework.serializers import ModelSerializer

from mycarhistory.cars.models import Car
from mycarhistory.treatments.serializers import TreatmentSerializer


class CarSerializer(ModelSerializer):

    treatments = TreatmentSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        read_only_fields = ('user',)
