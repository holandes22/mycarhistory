from rest_framework.serializers import ModelSerializer

from mycarhistory.treatments.models import Treatment


class TreatmentSerializer(ModelSerializer):

    class Meta:
        model = Treatment
        read_only_fields = ('car',)
