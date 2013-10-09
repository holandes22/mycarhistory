
from rest_framework import viewsets

from mycarhistory.users.models import User
from mycarhistory.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
