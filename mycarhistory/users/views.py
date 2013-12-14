from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status, exceptions

from mycarhistory.users.models import User
from mycarhistory.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def get_auth_token(request):

    if request.user.is_authenticated:
        return Response(
            request.user.get_auth_token(),
            status.HTTP_200_OK
        )
        raise exceptions.NotAuthenticated()
