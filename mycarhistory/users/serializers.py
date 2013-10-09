from rest_framework.serializers import ModelSerializer

from mycarhistory.users.models import User
from mycarhistory.cars.serializers import CarSerializer


class UserSerializer(ModelSerializer):

    cars = CarSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'full_name', 'short_name', 'cars')
