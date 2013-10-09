from rest_framework.serializers import HyperlinkedModelSerializer

from mycarhistory.users.models import User


class UserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'full_name', 'short_name')
