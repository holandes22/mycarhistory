from rest_framework.serializers import ModelSerializer

from mycarhistory.users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'full_name', 'short_name')
