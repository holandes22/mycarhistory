import factory
from factory.django import DjangoModelFactory
from django.conf import settings


class UserFactory(DjangoModelFactory):
    FACTORY_FOR = settings.AUTH_USER_MODEL
    FACTORY_DJANGO_GET_OR_CREATE = ('username',)

    username = 'tata'
    first_name = 'Gerardo'
    last_name = 'Martino'
    full_name = 'Gerardo Daniel Martino'
    is_staff = False
    is_superuser = False
    email = factory.LazyAttribute(
        lambda a: '{}.{}@example.com'.format(
            a.first_name,
            a.last_name
        ).lower()
    )
