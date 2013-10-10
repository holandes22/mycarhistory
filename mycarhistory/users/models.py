from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

from rest_framework.authtoken.models import Token


class User(AbstractUser):

    full_name = models.CharField(max_length=150, default='')
    short_name = models.CharField(max_length=50, default='',
                                  help_text='How would you like to be addressed?')

    def get_full_name(self):
        return self.full_name


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
