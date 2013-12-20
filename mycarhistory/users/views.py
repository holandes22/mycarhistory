from django.contrib import auth
from django.conf import settings

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.generics import RetrieveAPIView, ListAPIView
from django_browserid.base import BrowserIDException

from mycarhistory.users.models import User
from mycarhistory.users.serializers import UserSerializer


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login(request):
    assertion = request.POST.get('assertion', None)
    if not assertion:
        return Response(
            'assertion parameter is missing',
            status.HTTP_400_BAD_REQUEST
        )

    # TODO: Compare to referer??
    audience = getattr(settings, 'PERSONA_AUDIENCE', None)
    if not audience:
        return Response(
            'audience is missing. Check configuration',
            status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    try:
        user = auth.authenticate(
            assertion=assertion,
            audience=audience,
        )
        return Response({
            'email': user.email,
            'token': user.get_auth_token(),
        })
    except BrowserIDException:
        return Response(
            'Authentication failed',
            status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    except Exception:
        return Response(
            'An unexpected error occured while authenticating.',
            status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class UserListAPIView(ListAPIView):

    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.none()


class UserDetailAPIView(RetrieveAPIView):

    model = User
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
