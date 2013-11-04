from rest_framework.serializers import ModelSerializer

from mycarhistory.treatments.models import Treatment


class TreatmentByCarSerializer(ModelSerializer):

    class Meta:
        model = Treatment
        read_only_fields = ('car',)


class TreatmentSerializer(ModelSerializer):

    class Meta:
        model = Treatment
